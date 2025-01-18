"""
    Permits to get the external data from kaggle and save it into 
    raw and cleaned folders inside the data folder
"""
import subprocess
def getdata() -> None:
    """
    Downloads a dataset from Kaggle, extracts it, and saves the necessary files 
    into the 'raw' and 'cleaned' folders inside the 'data' directory.

    This function:
    1. Downloads a zip file from Kaggle.
    2. Extracts the contents into the 'raw' folder.
    3. Removes the zip file.
    4. Copies the CSV file to the 'cleaned' folder.

    Returns:
        None
    """
    url = 'https://www.kaggle.com/api/v1/datasets/download/danbraswell/temporary-us-births'
    subprocess.run(['curl', '-L', '-o', '../../data/raw/us_births_2016_2021.zip',
                    url],
                   check=True)
    subprocess.run(['tar',
                    '-xf',
                    '../../data/raw/us_births_2016_2021.zip',
                    '-C',
                    '../../data/raw'], check=True)
    subprocess.run(['cp',
                    '../../data/raw/us_births_2016_2021.csv',
                    '../../data/cleaned'], check=True)
    
    subprocess.run(['rm',
                    '-rf',
                    '../../data/raw/us_births_2016_2021.zip'], check=True)
if __name__ == "__main__":
    getdata()
