import requests

# Define the URL of the zip file
url = "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip"

# Define custom headers (replace these with actual headers from Chrome if needed)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Referer": "https://www.sec.gov/",
    # Add any other headers as needed
}

# Function to download a zip file
def download_zip(url, headers, filename):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Zip file '{filename}' downloaded successfully.")
    else:
        print(f"Failed to download '{filename}'. Status code: {response.status_code}")

# Download the zip file with custom headers
download_zip(url, headers, "downloaded.zip")
