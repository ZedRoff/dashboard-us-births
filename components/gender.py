import pandas as pd
import plotly.express as px

# Charger les données depuis le fichier CSV
file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(file_path)

# Calculer le nombre total de naissances par sexe pour chaque année
gender_year_counts = df.groupby(['Year', 'Gender'])['Number of Births'].sum().reset_index()

# Créer un graphique à secteurs pour chaque année
fig = px.pie(
    gender_year_counts,
    names="Gender",  # Sexe du bébé
    values="Number of Births",  # Nombre de naissances par sexe
    title="Répartition des Naissances par Sexe pour Chaque Année",
    labels={"Number of Births": "Nombre de Naissances", "Gender": "Sexe"},
    template="plotly_dark",  # Thème sombre
    facet_col="Year",  # Créer un sous-graphique pour chaque année
    facet_col_wrap=3,  # Afficher 3 années par ligne
    color="Gender",  # Utiliser la colonne 'Gender' pour définir les couleurs
    color_discrete_map={
        "M": "blue",  # Bleu pour les garçons
        "F": "pink",  # Rose pour les filles
    }
)

# Ajuster l'apparence pour améliorer la lisibilité
fig.update_layout(
    height=1000,  # Hauteur pour une meilleure lisibilité
    width=1500,  # Largeur pour s'assurer que tout est visible
    paper_bgcolor="#1A1A1A",  # Fond sombre
    plot_bgcolor="#2F4F4F",  # Fond du graphique
    title="Répartition des Naissances par Sexe pour Chaque Année",
)

# Afficher le graphique
fig.show()
