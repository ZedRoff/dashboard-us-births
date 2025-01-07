import dash
from dash import html, dcc, Output, Input

import dash_bootstrap_components as dbc

from callbacks import register_callbacks
# Initialiser l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])






# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div([

     html.Header([
        html.A([
            html.I(className="fa-solid fa-map-marker-alt"),
            html.H1("US Births", id="title_main"),
            
     ], className="element_header", href="#"),
     html.Div([
        html.A("Accueil", className="nav_item nav_item_active"),
        html.A("Données Locales", className="nav_item"),
        html.A("Données Globales", className="nav_item"),
 html.I(className="fa-solid fa-moon", id="theme_switch")
     ], id="navbar")
], className="header_main"),

    html.Main([
            html.Div([
                html.H2("US Births from 2016 to 2021", id="subtitle_main"),
                html.P("A minimalist dashboard developed for a ESIEE course that showcase US births data", id="description_main"),
                 html.Div([

        html.Div([
            html.I(className="fa-solid fa-flag icon_stat"),
            html.H3("States", id="stat_title"),
            html.P("51", className="stat_data")

        ], className="stat_card"),

        html.Div([
            html.I(className="fa-solid fa-chart-bar icon_stat"),
            html.H3("Graphs", id="stat_title"),
            html.P("15", className="stat_data")

        ], className="stat_card"),

    ], id="stats_main")
            ], id="block_left"),
            html.Img(src="./assets/image.png", id="image_main")
    ], id="block_main"),

html.Div(
html.Div([
            html.H3(
                "Data source", id="source_title"
            ),
            html.P("The data in this dataset was obtained using CDC's WONDER retrieval tool on the CDC Natality page"),
            html.Div([
                html.A("Kaggle", className="source_button"),
                html.A("CSV", className="source_button")
            ], id="source_buttons")
], id="source"), id="source_section"
)
        
    
    
], className="container_main")



register_callbacks(app)

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
