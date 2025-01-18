import requests
import zipfile
import os
import shutil

def getdata() -> None:
    """
    Downloads a dataset, extracts it, and organizes the files into 'raw' and 'cleaned' folders.
   

    Returns:
        None
    """
    # Define paths
    raw_folder = os.path.abspath('../../data/raw')
    cleaned_folder = os.path.abspath('../../data/cleaned')
    zip_file_path = os.path.join(raw_folder, 'us_births_2016_2021.zip')
    csv_file_name = 'us_births_2016_2021.csv'

    # Create directories if they don't exist
    os.makedirs(raw_folder, exist_ok=True)
    os.makedirs(cleaned_folder, exist_ok=True)

    # Download the zip file
    url = 'https://www.kaggle.com/api/v1/datasets/download/danbraswell/temporary-us-births'
    print("Downloading dataset...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(zip_file_path, 'wb') as f:
            f.write(response.content)
        print("Download completed.")
    else:
        raise Exception(f"Failed to download the dataset. Status code: {response.status_code}")

    # Extract the zip file
    print("Extracting files...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(raw_folder)
    print("Extraction completed.")

    # Move the CSV file to the cleaned folder
    print("Moving CSV file to the cleaned folder...")
    csv_file_path = os.path.join(raw_folder, csv_file_name)
    if os.path.exists(csv_file_path):
        shutil.copy(csv_file_path, cleaned_folder)
        print("CSV file moved successfully.")
    else:
        print(f"CSV file '{csv_file_name}' not found in the raw folder.")

    # Remove the zip file
    print("Cleaning up...")
    os.remove(zip_file_path)
    print("Cleanup completed.")

if __name__ == "__main__":
    getdata()