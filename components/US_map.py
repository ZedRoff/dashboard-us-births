import pandas as pd
import json
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from shapely.geometry import shape

# Charger les données
birth_data = pd.read_csv("data/us_births_2016_2021.csv")

# Charger le fichier GeoJSON
geojson_file = "data/us-states.json"
with open(geojson_file, 'r') as f:
    geojson_data = json.load(f)

# Liste des petits États pour lesquels on veut déporter l'affichage
small_states = ["RI", "CT", "DE", "NJ", "MD", "MA", "VT", "NH"]

# Fonction pour créer une carte Plotly
def create_plotly_map(year):
    # Filtrer les données pour l'année choisie
    birth_data_year = birth_data[birth_data['Year'] == year]
    
    # Agréger les données par État pour calculer le nombre total de naissances
    state_births_year = birth_data_year.groupby(['State', 'State Abbreviation'])['Number of Births'].sum().reset_index()

    # Créer une carte choroplèthe avec Plotly
    fig = px.choropleth(
        state_births_year,
        geojson=geojson_data,
        locations="State",  # Colonne correspondant au nom des États
        featureidkey="properties.name",  # Clé correspondant au GeoJSON
        color="Number of Births",
        color_continuous_scale="OrRd",
        scope="usa",
        labels={"Number of Births": "Naissances"}
    )

    # Ajouter des annotations pour les petits États
    for feature in geojson_data['features']:
        state_name = feature['properties']['name']
        state_data = state_births_year[state_births_year['State'] == state_name]
        if not state_data.empty:
            state_abbr = state_data['State Abbreviation'].values[0]
            centroid = shape(feature['geometry']).centroid

            if state_abbr in small_states:
                font_size = 11
            elif state_abbr == "DC":
                font_size = 5
            else:
                font_size = 14

            x_offset = 0.5 if state_abbr == "FL" else 0

            # Ajouter une annotation au centre de l'État en utilisant des coordonnées géographiques
            fig.add_trace(go.Scattergeo(
                lon=[centroid.x + x_offset],  # Utiliser la longitude
                lat=[centroid.y],            # Utiliser la latitude
                text=[state_abbr],
                mode="text",
                showlegend=False,
                textfont=dict(size=font_size, color="black"),
                hoverinfo="none"
                
            ))
  
    # Modifier la position de la légende
    fig.update_layout(
        coloraxis_colorbar=dict(
            orientation="h",  # Orientation horizontale de la barre de couleurs
            y=-0.3,  # Positionner légèrement en bas
            title="Nombre de naissances"  # Titre de la légende
        )
    )

    # Ajuster les limites et l'apparence de la carte
    fig.update_geos( visible=False, subunitcolor="red")

    return fig

# Créer l'application Dash
app = Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    html.H1("Carte des naissances aux États-Unis (2016-2021)"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(year), "value": year} for year in range(2016, 2022)],
        value=2016,
        clearable=False,
    ),
    dcc.Graph(id="map-plotly", style={"height": "600px", "margin-top": "20px"})
])

# Callback pour mettre à jour la carte
@app.callback(
    Output("map-plotly", "figure"),
    Input("year-dropdown", "value")
)
def update_plotly_map(year):
    return create_plotly_map(year)

# Exécuter l'application
if __name__ == "__main__":
    app.run_server(debug=True)
