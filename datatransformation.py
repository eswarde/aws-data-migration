import os
import json
import boto3

# Define the directory where your JSON files are located
directory = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\datamigration\\JSON'  # Replace with your actual directory path

s3 = boto3.client('s3', aws_access_key_id='AKIAVTR6ILLCURHTBRWD',
                  aws_secret_access_key='QfFw2+mXJMWlLkq05zQGjKTMJZGcPp6GF2kCJzAv', region_name='ap-south-1')

# List of specific file names you want to process (replace with your 10 file names)
specific_files = [
    'CIK0001584104.json',
    'CIK0001464623.json',
    'CIK0001268236.json',
    'CIK0001548281.json'
    # Add the names of the 10 JSON files you want to process here
]

# Initialize an empty list to store the transformed data
list_of_dictionaries = []

# Iterate through the specific files
for filename in specific_files:
    # Check if the file exists in the directory
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            try:
                # Load JSON data from the file
                data = json.load(json_file)

                # Append the loaded JSON data as a dictionary to the list
                list_of_dictionaries.append(data)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {file_path}: {str(e)}")
    else:
        print(f"File {filename} does not exist in the directory.")

# Now, list_of_dictionaries contains the data from the 10 specific JSON files as a list of dictionaries

# Print a summary of the resulting list of dictionaries
for idx, dictionary in enumerate(list_of_dictionaries, start=1):
    print(f"Dictionary {idx} Summary:")
    print(f"Keys: {list(dictionary.keys())}")  # Print the keys in the dictionary
    print(f"Number of Items: {len(dictionary)}")  # Print the number of items in the dictionary
    print("\n")

# Add the code to store the data in Amazon S3 using Boto3 here
s3_bucket_name = "my-fp-datamigration-bucket1"  # Replace with your S3 bucket name
s3_object_key = "data.json"  # Replace with the desired object key

# Initialize the S3 client
s3_client = boto3.client('s3')

# Serialize the list of dictionaries to JSON format
json_data = json.dumps(list_of_dictionaries)

try:
    # Upload the JSON data to Amazon S3
    s3_client.put_object(
        Bucket=s3_bucket_name,
        Key=s3_object_key,
        Body=json_data,
        ContentType='application/json'  # Set the content type if needed
    )
    print(f"Data uploaded to S3 bucket: {s3_bucket_name}, object key: {s3_object_key}")

except Exception as e:
    print(f"Error uploading data to S3: {str(e)}")
