import pandas as pd
import utils.helpers as helpers
def run():
<<<<<<< HEAD:utils/getStats.py
    df = helpers.load_data()
=======
    df = pd.read_csv('world-data-2023.csv')
    if 'Calling Code' in df.columns:
        df = df.drop(columns=['Calling Code'])
    if 'Latitude'  in df.columns:
        df = df.drop(columns=['Latitude'])
    if 'Longitude'  in df.columns:
        df = df.drop(columns=['Longitude'])
    

>>>>>>> bfafe5d (feat: creating cards and processing data):getStats.py
    numeric_df = df.select_dtypes(include=['number'])
    statistics = pd.DataFrame({
    'Variable': numeric_df.columns,
    'Moyenne': numeric_df.mean(),
    }).reset_index(drop=True)
    return statistics