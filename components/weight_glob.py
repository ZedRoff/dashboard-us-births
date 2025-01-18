"""
Generates a weighted histogram of the distribution of average birth weights
by gender using the US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.express as px


def generate(file_path : str ="data/us_births_2016_2021.csv") -> px.Figure:
    """
    Generates a weighted histogram of the distribution of average birth weights
    by gender.
    
    Args:
        file_path (str): Path to the CSV file containing the birth data.
    
    Returns:
        plotly.graph_objects.Figure: The generated histogram figure.
    """
    # Charger les données
    birth_data = pd.read_csv(file_path)

    # Créer une nouvelle colonne pondérée (poids multiplié par le nombre de naissances)
    birth_data["Weighted Birth Weight"] = (
        birth_data["Average Birth Weight (g)"] * birth_data["Number of Births"]
    )

    # Créer un histogramme avec les données pondérées
    fig = px.histogram(
        birth_data,
        x="Average Birth Weight (g)",  # L'axe X montre les poids moyens
        y="Weighted Birth Weight",  # L'axe Y montre les poids pondérés
        color="Gender",  # Colorier selon le genre
        labels={
            "Average Birth Weight (g)": "Average Birth Weight (g)",
            "Weighted Birth Weight": "Weighted Total Birth Weight (g)",
        },
        nbins=30,
        color_discrete_sequence=["#B31942", "#0A3161"],  # Couleurs personnalisées
        text_auto=True,
    )

    # Personnaliser la mise en page
    fig.update_layout(
        xaxis_title="Average Birth Weight (g)",
        yaxis_title="Weighted Total Birth Weight (g)",
        title_font_size=20,
        plot_bgcolor="#FFFFFF",  # Fond blanc
        font={"size": 14},
        showlegend=False,  # Désactiver la légende
        xaxis={"showline": True, "linecolor": "black", "linewidth": 2},
        yaxis={
            "showline": True,
            "linecolor": "black",
            "linewidth": 2,
            "showgrid": True,
            "gridcolor": "lightgrey",
            "gridwidth": 1,
            "ticks": "outside",
            "griddash": "dash",
            "tickwidth": 2,
            "tickcolor": "black",
        },
    )

    # Ajouter une bordure aux barres
    fig.update_traces(
        marker_line_color="black",  # Bordure noire autour des barres
        marker_line_width=1.5,  # Épaisseur de la bordure
    )

    # Retourner le graphique
    return fig
