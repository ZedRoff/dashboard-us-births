import dash
from dash import html, Input, Output, ctx, callback_context
import utils.carte as carte 
import os
import dash_bootstrap_components as dbc
import utils.getStats as getStats

import views.demography as demography
import views.economy as economy
import views.environment as environment
import views.education as education
import views.language as language

from components.navbar import create_navbar
from components.sidebar import create_sidebar

import plotly.graph_objects as go

from callbacks import register_callbacks
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
        create_navbar(),
        html.Main([
            create_sidebar(),
            html.Div([
             html.P(stats["Moyenne"])

            ],className="content", id="content")
        ])
    ], className="test2")
],)

register_callbacks(app)

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=False)
