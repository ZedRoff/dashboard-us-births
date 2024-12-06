import pandas as pd
import utils.helpers as helpers
def count_countries_by_language(language):
    # Utilisation de query pour filtrer les pays dont la langue est mentionnée
    df = helpers.load_data()
    filtered_countries = df[df["Official language"].str.contains(language, case=False, na=False)]
    return len(filtered_countries)
