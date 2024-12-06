

from dash import Output, Input
from utils import carte
import os
def register(app):
    @app.callback(
    Output("map-frame", "srcDoc"),
    Input("bouton", "n_clicks"),
    prevent_initial_call=True
    )
    def display_map(_):
    # Générer la carte avec le fichier `carte.py`
        carte.generate_map()

    # Charger le contenu du fichier `map.html`
        if os.path.exists("map.html"):
            with open("map.html", "r", encoding="utf-8") as f:
                return f.read()
        return "Erreur : la carte n'a pas été générée."

    @app.callback(
    Output("iframe-container", "id"),
    Input("bouton", "n_clicks"),
    prevent_initial_call=True
    )
    def f(_):
        return "carte"