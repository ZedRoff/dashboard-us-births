import dash
from dash import html, dcc, Output, Input

import dash_bootstrap_components as dbc
import utils.getStats as getStats



from components.navbar import create_navbar
from components.sidebar import create_sidebar

from callbacks import register_callbacks
# Initialiser l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

country_selected = "France"

stats = getStats.run()
# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div([
    html.Div([
        html.Iframe(src="", id="map-frame")
    ],  id="iframe-container"),
    html.Div([
        create_navbar(),
        html.Main([
            create_sidebar(),
            html.Div([
             html.Button("Change location", id="change-location"),
             dcc.Store(id="location-store", data="France"),
             html.P(id="location-display")
            ],className="content", id="content")
        ])
    ], className="test2")
])




register_callbacks(app)

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=False)
