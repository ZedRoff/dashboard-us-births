"""
Generates a box plot of the average age of mothers for a selected state 
using the US births data from 2016 to 2021.
Displays the distribution of the average age of mothers for that specific state.
"""

import pandas as pd
import plotly.express as px


def generate(state: str) -> px.box :
    """
    Generates a box plot of the average age of mothers for a selected state.
    
    Args:
        state (str): The state for which the average age of mothers box plot is generated.
    
    Returns:
        plotly.graph_objects.Figure: The generated box plot.
    """
    # Charger les données
    birth_data = pd.read_csv("data/cleaned/us_births_2016_2021.csv")

    # Filtrer les données pour l'état sélectionné
    df_filtered = birth_data[birth_data["State"] == state]

    # Créer un box plot pour l'état sélectionné
    fig = px.box(
        df_filtered,
        x="State",  # L'état comme catégorie sur l'axe X
        y="Average Age of Mother (years)",  # Âge moyen des mères
        title=f"In {state}",
        labels={
            "State": "State",
            "Average Age of Mother (years)": "Average Age of Mothers (years)",
        },
        color_discrete_sequence=["#0A3161"],  # Couleur personnalisée
    )

    # Appliquer un style cohérent
    fig.update_layout(
        title_font={"size": 18, "color": "black"},  # Taille et couleur du titre
        title_x=0.5,  # Centrer le titre
        xaxis={
            "title": "State",  # Titre de l'axe X
            "showline": True,  # Ajouter une ligne pour l'axe X
            "linecolor": "black",  # Couleur de la ligne
            "linewidth": 2,  # Épaisseur de la ligne
            "ticks": "outside",
            "tickwidth": 2,
            "tickcolor": "black",
        },
        yaxis={
            "title": "Average Age of Mothers (years)",  # Titre de l'axe Y
            "showline": True,  # Ajouter une ligne pour l'axe Y
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
        plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
    )

    # Retourner le graphique
    return fig
