import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv('../data/us_births_2016_2021.csv')

# Définir l'état sélectionné
selected_state = 'California'  # Remplacer par l'état de ton choix

# Filtrer les données pour l'état sélectionné
df_state = df[df['State'] == selected_state]

# Calculer le nombre total de naissances par année pour l'état sélectionné
births_per_year = df_state.groupby('Year')['Number of Births'].sum().reset_index()

# Créer un graphique de tendance pour l'évolution du nombre de naissances par année
fig = px.line(
    births_per_year,
    x="Year",  # L'axe des abscisses représente l'année
    y="Number of Births",  # L'axe des ordonnées représente le nombre de naissances
    title=f"Number of births per year in {selected_state}",
    labels={"Number of Births": "Number of births", "Year": "Year"},
)

# Ajuster l'apparence pour améliorer la lisibilité
fig.update_layout(
    height=800,
    width=1500,
    title=f"Number of births per year in {selected_state}",
    xaxis_title="Year",
    yaxis_title="Number of births",
    yaxis=dict(
        rangemode="tozero",  # Bien définir la plage de l'axe Y
    )
)

# Personnaliser l'apparence de la ligne
fig.update_traces(line_color='#3AABF6', line_width=3)

# Afficher le graphique
fig.show()
