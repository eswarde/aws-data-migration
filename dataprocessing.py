import os
import json

# Define the directory where your JSON files are located
directory = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\datamigration\\JSON'  # Replace with your actual directory path

# Initialize an empty list to store the loaded data from specific JSON files
selected_data = []

# List of specific file names you want to process
specific_files = [
    'CIK0000001750.json',
    'CIK0000001800.json',
    'CIK0000001961.json',
    'CIK0000002034.json',
    'CIK0000002098.json',
    'CIK0000002110.json',
    'CIK0000002178.json',
    'CIK0000002186.json',
    'CIK0000002488.json',
    'CIK0000002491.json'

    # Add the names of the 10 JSON files you want to process here
]

# Initialize a counter to keep track of the number of files processed
files_processed = 0

# Iterate through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json') and filename in specific_files:
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as json_file:
            # Read and process the JSON data line by line (streaming)
            for line in json_file:
                try:
                    data = json.loads(line)
                    # Process the data as needed
                    selected_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {file_path}: {str(e)}")

        # Increment the counter
        files_processed += 1

        # Check if we have processed the desired 10 files
        if files_processed == 10:
            break

# Check the structure of the loaded JSON data
if isinstance(selected_data, list):
    print("The JSON data is structured as a list of objects.")
elif isinstance(selected_data, dict):
    print("The JSON data is structured as a single object (dictionary).")
else:
    print("The JSON data does not have a recognized structure.")
