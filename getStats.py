import pandas as pd
def run():
    df = pd.read_csv('world-data-2023.csv')
    numeric_df = df.select_dtypes(include=['number'])
    statistics = pd.DataFrame({
    'Variable': numeric_df.columns,
    'Moyenne': numeric_df.mean(),
    'Médiane': numeric_df.median(),
    'Écart type': numeric_df.std()
    }).reset_index(drop=True)
    return statistics