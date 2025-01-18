import subprocess
def getdata() -> None:
    subprocess.run(['curl', '-L', '-o', '../../data/raw/us_births_2016_2021.zip', 'https://www.kaggle.com/api/v1/datasets/download/danbraswell/temporary-us-births'])
    subprocess.run(['tar', '-xf', '../../data/raw/us_births_2016_2021.zip', '-C', '../../data/raw'])
    subprocess.run(['rm', '-rf', '../../data/raw/us_births_2016_2021.zip'])
    subprocess.run(['cp', '../../data/raw/us_births_2016_2021.csv', '../../data/cleaned'])
if __name__ == "__main__":
    getdata()