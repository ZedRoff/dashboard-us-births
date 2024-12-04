import folium
import pandas as pd
from folium.plugins import MarkerCluster


def generate_map():

    #Coordonnées du milieu de la France pour le départ
    coords = (46.227638,2.213749)

    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' 
    attribution = 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'

    map = folium.Map(location=coords, tiles=tiles, attr=attribution, zoom_start=2, no_wrap=True,min_zoom=2, zoom_control=False)

    # Créer un MarkerCluster
    marker_cluster = MarkerCluster().add_to(map)

    # Définir les bornes de la carte pour empêcher le déplacement hors de ces bornes
    map.options['maxBounds'] = [[-85, -180], [85, 180]]  # Empêcher le déplacement au-delà des limites géographiques
    map.options['maxBoundsViscosity'] = 1.0  # Rendre la contrainte des bornes géographiques stricte


    df = pd.read_csv('world-data-2023.csv')

    for i in range(len(df)):
        name = df.values[i][0]
        x = df.values[i][33]
        y = df.values[i][34]
        coords=[x,y]
        icone = folium.Icon(color="blue", icon="globe")
        folium.Marker(location=coords, popup=name ,tooltip = name, icon=icone).add_to(marker_cluster)
 

        
    map.save(outfile='map.html')


