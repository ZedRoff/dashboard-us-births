

from dash import Output, Input
from utils import carte
import os
def register(app):
    @app.callback(
    Output("map-frame", "src"),
    Input("bouton", "n_clicks"),
    prevent_initial_call=True
    )
    def display_map(_):
    # Générer la carte avec le fichier `carte.py`
        carte.generate_map()

    # Charger le contenu du fichier `map.html`
        if os.path.exists("assets/map.html"):
            # Serve the map.html file as a URL
            return "assets/map.html"
        return "Erreur : la carte n'a pas été générée."

    @app.callback(
    Output("iframe-container", "id"),
    Input("bouton", "n_clicks"),
    prevent_initial_call=True
    )
    def f(_):
        return "carte"