import boto3
import json
import time
import botocore.exceptions


bucket_name = 'my-fp-datamigration-bucket1'
table_name = 'fpdata_migration'

s3_client = boto3.client('s3', region_name='ap-south-1', aws_access_key_id="AKIAVTR6ILLCURHTBRWD",
                         aws_secret_access_key="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")
dynamodb_client = boto3.client('dynamodb', region_name='ap-south-1', aws_access_key_id="AKIAVTR6ILLCURHTBRWD",
                               aws_secret_access_key="QfFw2+mXJMWlLkq05zQGjKTMJZGcPp6GF2kCJzAv")

response = s3_client.list_objects(Bucket=bucket_name)

max_retries = 5
batch_size = 10  # Adjust the batch size based on your needs

for obj in response.get('Contents', []):
    object_key = obj['Key']

    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    json_content = response['Body'].read().decode('utf-8')
    data = json.loads(json_content)

    if isinstance(data, list):
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            items = []
            for item in batch:
                attribute_map = {}
                for key, value in item.items():
                    attribute_map[key] = {
                        'S': str(value) if isinstance(value, (str, int, float)) else json.dumps(value)
                    }
                items.append({'PutRequest': {'Item': attribute_map}})

            # Retry logic
            for retry in range(max_retries):
                try:
                    dynamodb_client.batch_write_item(
                        RequestItems={
                            table_name: items
                        }
                    )
                    print(f"Uploaded data from {object_key} to DynamoDB")
                    break  # Success, exit the retry loop
                except botocore.exceptions.ClientError as e:
                    if 'ValidationException' in str(e):
                        # Handle ValidationException (item size exceeded)
                        print(f"Item size exceeded. Retrying in {2 ** retry} seconds.")
                        time.sleep(2 ** retry)
                    elif e.response['Error']['Code'] == 'ProvisionedThroughputExceededException':
                        # Handle throughput exceeded exception
                        print(f"Throughput exceeded. Retrying in {2 ** retry} seconds.")
                        time.sleep(2 ** retry)
                    elif e.response['Error']['Code'] == 'ThrottlingException':
                        # Handle throttling exception
                        print(f"Throttling. Retrying in {2 ** retry} seconds.")
                        time.sleep(2 ** retry)
                    else:
                        # Handle other exceptions
                        print(f"Error: {e}")
                        break
