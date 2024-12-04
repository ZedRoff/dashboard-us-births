import dash
from dash import dcc, html, Input, Output
import carte 
import os

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div([
    # Conteneur global pour simuler le "body"
    html.Div([
        html.Iframe(srcDoc="", id="map-frame")
    ], className="iframe-container"),

    html.Div([
        # Header
        html.Header([
            html.Div("France"),
            html.Div("Dashboard World Data 2023"),
            html.Button([
                html.I(className = "fa-solid fa-map-marker-alt")
            ], id="bouton")
        ]),
        # Main container
        html.Main([
            # Sidebar
            html.Aside([
                html.I(className="fa-solid fa-people-group"),
                html.I(className="fa-solid fa-coins"),
                html.I(className="fa-solid fa-graduation-cap"),
                html.I(className="fa-solid fa-leaf"),
                html.I(className="fa-solid fa-language")
            ],className="Nav"),

            # Content area
            html.Div([
              html.P("COUCOUU")
            ],className="content")
        ],)
    ], className="test2")
],)

# Callback pour gérer le clic sur le bouton
@app.callback(
    Output("map-frame", "srcDoc"),
    Input("bouton", "n_clicks"),  # Détection des clics sur le bouton
    prevent_initial_call=True)  # N'exécute pas au démarrage

def display_map(_):
    # Générer la carte avec le fichier `carte.py`
    carte.generate_map()

    # Charger le contenu du fichier `map.html`
    if os.path.exists("map.html"):
        with open("map.html", "r", encoding="utf-8") as f:
            return f.read()
    return "Erreur : la carte n'a pas été générée."

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
