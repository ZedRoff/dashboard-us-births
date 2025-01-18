"""
Generates a weighted histogram of the distribution of average birth weights by gender
for a selected state using data from the US birth dataset (2016-2021).
"""
import pandas as pd
import plotly.express as px


def generate(selected_state: str) -> px.histogram:
    """
    Generates a weighted histogram of the distribution of average birth weights by gender
    for a given state from the US birth dataset.

    Args:
        selected_state (str): The state for which the data will be filtered.

    Returns:
        plotly.graph_objects.Figure: A Plotly figure object containing the weighted histogram.
    """
    # Charger les données
    file_path = "data/cleaned/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)

    # Créer une nouvelle colonne pondérée (poids multiplié par le nombre de naissances)
    birth_data["Weighted Birth Weight"] = (
        birth_data["Average Birth Weight (g)"] * birth_data["Number of Births"]
    )

    # Filtrer les données pour un état spécifique
    df_state = birth_data[birth_data["State"] == selected_state]

    # Créer un histogramme pondéré avec Plotly
    fig = px.histogram(
        df_state,
        x="Average Birth Weight (g)",
        y="Weighted Birth Weight",  # Utiliser les poids pondérés pour l'axe Y
        color="Gender",
        title=f"In {selected_state}",
        labels={
            "Average Birth Weight (g)": "Average weight of birth (g)",
            "Weighted Birth Weight": "Weighted Total Birth Weight (g)",
        },
        nbins=30,
        color_discrete_sequence=["#B31942", "#0A3161"],
        text_auto=True,
    )

    # Personnaliser la mise en page
    fig.update_layout(
        xaxis_title="Average weight of birth (g)",
        yaxis_title="Weighted Total Birth Weight (g)",
        title_font_size=20,
        plot_bgcolor="#FFFFFF",
        font={"size": 14},
        showlegend=False,
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
    fig.update_traces(marker_line_color="black", marker_line_width=1.5)

    # Afficher le graphique
    return fig
