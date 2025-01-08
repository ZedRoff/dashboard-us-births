import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/us_births_2016_2021.csv')
def generate():
    # Calculer le nombre total de naissances par année
    births_per_year = df.groupby('Year')['Number of Births'].sum().reset_index()

    # Créer un graphique de tendance pour l'évolution du nombre de naissances par année
    fig = px.line(
        births_per_year,
        x="Year",  # L'axe des abscisses représente l'année
        y="Number of Births",  # L'axe des ordonnées représente le nombre de naissances
        title="Number of births per year",
        labels={"Number of Births": "Number of births", "Year": "Year"},
    )

    # Ajuster l'apparence pour améliorer la lisibilité
    fig.update_layout(
        height=800,
        width=1500,
        title="Number of births per year",
        xaxis_title="Year",
        yaxis_title="Number of births",
        yaxis=dict(
            rangemode="tozero",  # Bien définir la plage de l'axe Y
        )
    )
    fig.update_traces(line_color='#3AABF6', line_width=3)

    return fig

