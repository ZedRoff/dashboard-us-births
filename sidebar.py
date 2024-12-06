import dash
from dash import dcc, html, Input, Output, ctx, callback_context
import carte 
import os
import demography
import dash_bootstrap_components as dbc
import fertility
import getStats



import plotly.graph_objects as go
# Initialiser l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

country_selected = "France"

stats = getStats.run()
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
                html.I(className="fa-solid fa-coins", id="two"),
                html.I(className="fa-solid fa-graduation-cap", id="three"),
                html.I(className="fa-solid fa-leaf", id="four"),
                html.I(className="fa-solid fa-language", id="five")
            ],className="Nav"),

            # Content area
            html.Div([
             html.P(stats["Moyenne"])

            ],className="content", id="content")
        ],)
    ], className="test2")
],)
print(stats)
@app.callback(
    Output("content", "children"),
    [Input("one", "n_clicks"), Input("two", "n_clicks"), Input("three", "n_clicks"), Input("four", "n_clicks"), Input("five", "n_clicks")],
    prevent_initial_call=True
)
def update_content(one_clicks, two_clicks, three_clicks, four_clicks, five_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return html.P("No button clicked")
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == "one":
        return [
            dcc.Graph(id="demography", figure=demography.run()),
            dcc.Graph(id="fertility", figure=fertility.run())
        ]
    elif button_id == "two":
        return html.P("deuxieme ecran")
    elif button_id == "three":
        return html.P("troisieme ecran")
    elif button_id == "four":
        return html.P("quatrieme ecran")
    elif button_id == "five":
        return html.P("cinquieme ecran")






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
def f(_):
    return "carte"

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=False)
