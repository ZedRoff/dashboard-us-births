"""
Generates a line plot showing the trend of the total number of births per year 
using the US births data from 2016 to 2021.
Displays the number of births over time.
"""

import pandas as pd
import plotly.express as px


def generate() -> px.line :
    """
    Generates a line plot of the total number of births per year.
    
    Returns:
        plotly.graph_objects.Figure: The generated line plot.
    """
    # Charger les données
    birth_data = pd.read_csv("data/cleaned/us_births_2016_2021.csv")

    # Calculer le nombre total de naissances par année
    births_per_year = birth_data.groupby("Year")["Number of Births"].sum().reset_index()

    # Créer un graphique de tendance pour l'évolution du nombre de naissances par année
    fig = px.line(
        births_per_year,
        x="Year",  # L'axe des abscisses représente l'année
        y="Number of Births",  # L'axe des ordonnées représente le nombre de naissances
        labels={"Number of Births": "Number of births", "Year": "Year"},
    )

    # Appliquer le style des autres graphiques
    fig.update_layout(
        title_font={"size": 18, "color": "black"},  # Taille et couleur du titre
        title_x=0.5,  # Centrer le titre
        xaxis={
            "title": "Year",  # Titre de l'axe X
            "showline": True,  # Ajouter une ligne pour l'axe X
            "linecolor": "black",  # Couleur de la ligne
            "linewidth": 2,  # Épaisseur de la ligne
            "showgrid": True,  # Activer les lignes de la grille
            "gridcolor": "lightgrey",  # Couleur des lignes de la grille
            "gridwidth": 1,  # Épaisseur des lignes de la grille
            "griddash": "dash",  # Style des lignes de la grille
            "ticks": "outside",
            "tickwidth": 2,
            "tickcolor": "black",
        },
        yaxis={
            "rangemode": "tozero",  # Bien définir la plage de l'axe Y
            "ticks": "outside",
            "tickwidth": 2,
            "tickcolor": "black",
            "title": "Number of births",  # Titre de l'axe Y
            "showline": True,  # Ajouter une ligne pour l'axe Y
            "linecolor": "black",  # Couleur de la ligne
            "linewidth": 2,  # Épaisseur de la ligne
            "showgrid": True,  # Activer les lignes de la grille
            "gridcolor": "lightgrey",  # Couleur des lignes de la grille
            "gridwidth": 1,  # Épaisseur des lignes de la grille
            "griddash": "dash",  # Style des lignes de la grille
            "tickfont": {"size": 14, "color": "black"},  # Style des ticks
        },
        plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
        margin={"l": 50, "r": 50, "t": 50, "b": 50},  # Marges
    )

    # Personnaliser la ligne
    fig.update_traces(
        line_color="#0A3161",  # Couleur de la ligne
        line_width=3,  # Largeur de la ligne
    )

    # Afficher le graphique
    return fig
