import pandas as pd
import plotly.express as px

# Charger le fichier CSV
df = pd.read_csv('../data/us_births_2016_2021.csv')

def generate():
    # Définir les intervalles pour l'âge moyen des mères
    age_intervals = pd.cut(df['Average Age of Mother (years)'], bins=range(22, 38, 2))
    
    # Calculer le nombre de mères dans chaque tranche d'âge
    age_counts = df.groupby(age_intervals, observed=False)['Number of Births'].sum()

    # Créer un histogramme avec Plotly
    fig = px.bar(
        x=age_counts.index.astype(str),  # Tranches d'âge
        y=age_counts.values,  # Nombre de mères dans chaque tranche
        labels={'x': 'Tranche d\'âge des mères', 'y': 'Nombre de mères'},
        title="Répartition de l'âge moyen des mères",
        text=age_counts.values,  # Ajouter le nombre sur les barres
    )

    # Afficher le graphique
    fig.show()

# Appeler la fonction pour générer l'histogramme
generate()
