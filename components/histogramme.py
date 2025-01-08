import pandas as pd
import plotly.express as px

# Charger les données
file_path = '../data/us_births_2016_2021.csv'
df = pd.read_csv(file_path)

# Créer une fonction pour afficher l'histogramme
def plot_births_by_state(selected_state):
    # Filtrer les données pour l'état sélectionné
    df_state = df[df['State'] == selected_state]
    
    # Agréger le nombre de naissances par année pour l'état sélectionné
    births_by_year = df_state.groupby('Year')['Number of Births'].sum().reset_index()

    # Créer un histogramme avec Plotly
    fig = px.bar(
        births_by_year,
        x='Year',  # Utiliser la colonne 'Year' pour l'axe des X
        y='Number of Births',  # Utiliser la colonne 'Number of Births' pour l'axe des Y
        labels={'Year': 'Year', 'Number of Births': 'Number of births'},
        title=f'Number of births per year in {selected_state}',
        color_discrete_sequence=["#4A7B9D"]  # Spécification de la couleur
    )
    
    # Afficher le graphique
    return fig

