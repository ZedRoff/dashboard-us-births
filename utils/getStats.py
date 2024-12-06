import pandas as pd
import utils.helpers as helpers
def run():
    df = helpers.load_data()
    numeric_df = df.select_dtypes(include=['number'])
    statistics = pd.DataFrame({
    'Variable': numeric_df.columns,
    'Moyenne': numeric_df.mean(),
    'Médiane': numeric_df.median(),
    'Écart type': numeric_df.std()
    }).reset_index(drop=True)
    return statistics