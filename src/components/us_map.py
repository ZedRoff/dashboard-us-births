"""
Generates the US map from 2016 to 2021
"""

import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from shapely.geometry import shape


def create_plotly_map(year : int) -> go.Figure:
    """
    Creates a choropleth map of US birth data for a given year, with annotations
    for state abbreviations and a color scale representing the number of births.

    Args:
        year (int): The year for which to generate the map.

    Returns:
        plotly.graph_objects.Figure: The generated Plotly figure containing the map.
    """
    # Charger les données
    birth_data = pd.read_csv("data/cleaned/us_births_2016_2021.csv")

    # Charger le fichier GeoJSON
    geojson_file = "data/us-states.json"
    with open(geojson_file, "r", encoding="utf-8") as file:
        geojson_data = json.load(file)

    # Liste des petits États pour lesquels on veut déporter l'affichage
    small_states = ["RI", "CT", "DE", "NJ", "MD", "MA", "VT", "NH"]


    # Agréger les données par État pour calculer le nombre total de naissances
    state_births_year = (
        birth_data[birth_data["Year"] == year]
        .groupby(["State", "State Abbreviation"])["Number of Births"]
        .sum()
        .reset_index()
    )

    # Créer une carte choroplèthe avec Plotly
    fig = px.choropleth(
        state_births_year,
        geojson=geojson_data,
        locations="State",  # Colonne correspondant au nom des États
        featureidkey="properties.name",  # Clé correspondant au GeoJSON
        color="Number of Births",
        color_continuous_scale="OrRd",
        scope="usa",
        labels={"Number of Births": "Naissances"},
    )

    # Ajouter des annotations pour les petits États
    for feature in geojson_data["features"]:
        state_name = feature["properties"]["name"]
        state_data = state_births_year[state_births_year["State"] == state_name]
        if not state_data.empty:
            state_abbr = state_data["State Abbreviation"].values[0]
            centroid = shape(feature["geometry"]).centroid

            # Ajuster la taille de la police pour les petits États et DC
            if state_abbr in small_states:
                font_size = 11
            elif state_abbr == "DC":
                font_size = 5
            else:
                font_size = 14

            # Ajustement pour éviter le chevauchement de l'annotation sur la carte
            x_offset = 0.5 if state_abbr == "FL" else 0

            # Ajouter une annotation au centre de l'État en utilisant des coordonnées géographiques
            fig.add_trace(
                go.Scattergeo(
                    lon=[centroid.x + x_offset],  # Utiliser la longitude
                    lat=[centroid.y],  # Utiliser la latitude
                    text=[state_abbr],
                    mode="text",
                    showlegend=False,
                    textfont={"size": font_size, "color": "black"},
                    hoverinfo="none",  # Empêcher l'affichage d'informations au survol
                )
            )

    # Modifier la position de la légende
    fig.update_layout(
        coloraxis_colorbar={"orientation": "h", "y": -0.3, "title": "Number of Births"}
    )

    # Ajuster les limites et l'apparence de la carte
    fig.update_geos(visible=False, subunitcolor="red")  # Le sous-ensemble est colorié en rouge

    return fig
