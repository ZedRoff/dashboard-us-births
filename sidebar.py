import dash
from dash import dcc, html, Input, Output, ctx
import carte 
import os
import demography
import dash_bootstrap_components as dbc


# Initialiser l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

country_selected = "France"


# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div([
    html.Div([
        html.Iframe(srcDoc="", id="map-frame")
    ],  id="iframe-container"),

    html.Div([
        # Header
        html.Header([
            html.Div(country_selected),
            html.Div("Dashboard World Data 2023"),
            html.Button([
                html.I(className = "fa-solid fa-map-marker-alt")
            ], id="bouton")
        ]),
        # Main container
        html.Main([
            # Sidebar
            html.Aside([
                html.I(className="fa-solid fa-people-group", id="one"),
                html.I(className="fa-solid fa-coins"),
                html.I(className="fa-solid fa-graduation-cap"),
                html.I(className="fa-solid fa-leaf"),
                html.I(className="fa-solid fa-language")
            ],className="Nav"),

            # Content area
            html.Div([
              html.Div(id="content"),
              dcc.Graph(id="demography")

            ],className="content")
        ],)
    ], className="test2")
],)
@app.callback(
        Output("demography", "figure"),
        Input("one", "n_clicks"),
        prevent_initial_call=True
)
def test(one_clicks):
    return demography.run()

# Callback for the content div
@app.callback(
    Output("content", "children"),
    Input("one", "n_clicks"),
    prevent_initial_call=True
)
def update_content(one_clicks):
    global country_selected
    country_selected = "Senegal"
    return html.P("COUCOUU")


# Callback pour gérer le clic sur le bouton
# Callback for the map-frame
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
def test(_):
    return "carte"

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=False)
