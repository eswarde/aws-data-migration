**aws-data-migration**

Extract the data from a zip file that is available at a URL and load it into Amazon S3 and Amazon DynamoDB (NoSQL)
This project is designed to download a zip file from a specified URL, extract data from multiple JSON files within the zip, and seamlessly migrate and transform it into Amazon S3 and Amazon DynamoDB using Python.

**Technologies Used**

Python
Requests: For downloading the zip file.
Zipfile: For extracting data from the zip file.
boto3: For interacting with Amazon S3.
Amazon S3: Cloud storage for the extracted data.
Amazon DynamoDB: NoSQL database for storing the transformed data.
Problem Statement
You are provided with a URL pointing to a zip file containing multiple JSON files, each with varying data structures. The objective is to download, extract, and transform this data using Python, and then store it in Amazon S3 and Amazon DynamoDB.

**Approach**

Download the Zip File: Utilize the requests library to download the zip file from the specified URL.
Extract Data from Zip: Use the zipfile module to extract data from the downloaded zip file.
Store in Amazon S3: Use the boto3 library to upload the extracted data to Amazon S3 for efficient storage.
Load into Amazon DynamoDB: Utilize Python to load the data from Amazon S3 into Amazon DynamoDB.


**Results**

Upon successful execution, the tool will yield a list of dictionaries (if using Python) representing each document from the JSON files within the zip. Each dictionary or DataFrame row corresponds to a document.

**How to Use**

Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/your-username/your-repo.git
Install the required Python libraries.
bash
Copy code
pip install -r requirements.txt
Execute the Python script.
bash
Copy code
python data_migration_tool.py
