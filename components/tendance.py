import pandas as pd
import plotly.express as px

# Charger les données depuis le fichier CSV
file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(file_path)

# Calculer le nombre total de naissances par année
births_per_year = df.groupby('Year')['Number of Births'].sum().reset_index()

# Créer un graphique de tendance pour l'évolution du nombre de naissances par année
fig = px.line(
    births_per_year,
    x="Year",  # L'axe des abscisses représente l'année
    y="Number of Births",  # L'axe des ordonnées représente le nombre de naissances
    title="Évolution du Nombre de Naissances par Année",
    labels={"Number of Births": "Nombre de Naissances", "Year": "Année"},
    template="plotly_dark",  # Thème sombre
)

# Ajuster l'apparence pour améliorer la lisibilité
fig.update_layout(
    height=800,
    width=1500,
    paper_bgcolor="#1A1A1A",  # Fond sombre
    plot_bgcolor="#2F4F4F",  # Fond du graphique
    title="Évolution du Nombre de Naissances par Année",
    xaxis_title="Année",
    yaxis_title="Nombre de Naissances",
)

# Afficher le graphique
fig.show()
