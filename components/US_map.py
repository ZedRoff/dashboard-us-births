import pandas as pd
import json
import folium
from dash import Dash, html, dcc, Input, Output
from shapely.geometry import shape
birth_data = pd.read_csv("../data/us_births_2016_2021.csv")

# Charger le fichier GeoJSON
geojson_file = "../data/us-states.json"
with open(geojson_file, 'r') as f:
    geojson_data = json.load(f)

# Liste des petits États pour lesquels on veut déporter l'affichage
small_states = ["RI", "CT", "DE", "DC", "NJ", "MD", "MA", "VT", "NH"]

# Fonction pour créer une carte folium
def create_map(year):
    # Filtrer les données pour l'année choisie
    birth_data_year = birth_data[birth_data['Year'] == year]
    
    # Agréger les données par État pour calculer le nombre total de naissances
    state_births_year = birth_data_year.groupby(['State', 'State Abbreviation'])['Number of Births'].sum().reset_index()
    
    # Créer une carte centrale
    us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4, tiles="cartodbpositron")
    
    # Ajouter une couche choroplèthe pour représenter les naissances par État
    folium.Choropleth(
        geo_data=geojson_file,
        name="choropleth",
        data=state_births_year,
        columns=["State", "Number of Births"],
        key_on="feature.properties.name",
        fill_opacity=0.7,
        bins=[0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],
        fill_color="OrRd",
        line_weight=2,
        highlight=True,
        legend_name=f"Number of Births in {year}",
    ).add_to(us_map)
    
    # Ajouter les abréviations directement au centre géographique de chaque État
    for feature in geojson_data['features']:
        state_name = feature['properties']['name']
        state_data = state_births_year[state_births_year['State'] == state_name]
        
        # Récupérer l'abréviation de l'État
        state_abbr = state_data['State Abbreviation'].values[0]

        
        
        # Calculer le centroïde géométrique de l'État
        polygon = shape(feature['geometry'])
        centroid = polygon.centroid

       
        fontSize = 0
        if state_abbr in small_states:
            fontSize = 10
        else:
            fontSize = 14
        x = 0
        y = 0
        if state_abbr == "FL":
            x = centroid.x+0.5
            y = centroid.y 
        else:
            x = centroid.x
            y = centroid.y

        # Ajouter l'abréviation comme texte au centre géographique de l'État
        folium.Marker(
            location=[y, x],
            icon=folium.DivIcon(html=f"<div style='font-size:{fontSize}px; color:black; font-weight:bold; text-align:center'>{state_abbr}</div>")
        ).add_to(us_map)
    
    # Sauvegarder la carte temporairement
    us_map.save("../assets/temp_map.html")
    with open("../assets/temp_map.html", "r") as file:
        map_html = file.read()
    return map_html

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
    html.Div(id="map-container", style={"height": "600px", "margin-top": "20px"})
])

# Callback pour mettre à jour la carte
@app.callback(
    Output("map-container", "children"),
    Input("year-dropdown", "value")
)
def update_map(year):
    map_html = create_map(year)
    return html.Iframe(srcDoc=map_html, style={"width": "100%", "height": "600px", "border": "none"})

# Exécuter l'application
if __name__ == "__main__":
    app.run_server(debug=True)
