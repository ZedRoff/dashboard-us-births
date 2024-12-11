import pandas as pd
import utils.helpers as helpers
def run():
    df = helpers.load_data()
    if 'Calling Code' in df.columns:
        df = df.drop(columns=['Calling Code'])
    if 'Latitude'  in df.columns:
        df = df.drop(columns=['Latitude'])
    if 'Longitude'  in df.columns:
        df = df.drop(columns=['Longitude'])
    

    numeric_df = df.select_dtypes(include=['number'])
    statistics = pd.DataFrame({
    'Variable': numeric_df.columns,
    'Moyenne': numeric_df.mean(),
    }).reset_index(drop=True)
    return statistics