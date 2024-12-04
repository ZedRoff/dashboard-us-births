import dash
import numpy as np
import pandas as pd
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
#from deep_translator import GoogleTranslator

# Initialisation de l'application
app = dash.Dash(__name__)
app.title = "Dashboard Global Country Information"

# Charger le fichier world-data.csv
df = pd.read_csv('world-data-2023.csv')


# Filtrer les colonnes numériques
numeric_df = df.select_dtypes(include=['number'])

# Calcul des statistiques
statistics = pd.DataFrame({
    'Variable': numeric_df.columns,
    'Moyenne': numeric_df.mean(),
    'Médiane': numeric_df.median(),
    'Écart type': numeric_df.std()
}).reset_index(drop=True)

# Initialisation de l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='stats-table',
        columns=[{"name": col, "id": col} for col in statistics.columns],
        data=statistics.to_dict('records'),
        style_table={'margin': 'auto', 'width': '80%'},
        style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'},
        style_cell={'textAlign': 'center', 'padding': '5px'}
    )
])

#if __name__ == "__main__":
    #app.run_server(debug=True)

# Fonction pour compter les pays en fonction de la langue
def count_countries_by_language(language):
    # Utilisation de query pour filtrer les pays dont la langue est mentionnée
    filtered_countries = df[df["Official language"].str.contains(language, case=False, na=False)]
    return len(filtered_countries)

# Interaction via `input`
language = input("Entrez une langue : ").strip()
count = count_countries_by_language(language)

print(f"Nombre de pays parlant {language} : {count}")
