
from dash import html, Output, Input, Dash, callback_context

import dash_bootstrap_components as dbc
from views.homepage import homepage
from views.header import header
from views.local import local
from views.glob import glob
import views.globalStats as globalStats
import views.education as education
import views.age as age
import views.gender as gender
import views.weight as weight
import views.births as births
import components.US_map as US_map
from callbacks import register_callbacks
# Initialiser l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div([html.Div(header("home"), id="header"), html.Div(homepage(), id="content")], className="container_main")




@app.callback(
    [Output('header', 'children'), Output('content', 'children')],
    [Input('home', 'n_clicks'), Input('local', 'n_clicks'), Input('global', 'n_clicks')]
)

def update_header(n_clicks_home, n_clicks_local, n_clicks_global):
    content = homepage()
    ctx = callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == "home":
        content = homepage()
    elif triggered_id == "local":
        content = local()
    elif triggered_id == "global":
        content = glob()
    else:
        content = local()
    if len(triggered_id) == 0:
        return header("home"), content
    return header(triggered_id), content

@app.callback(
        [Output('main_global', 'children')],
        [Input('Education', 'n_clicks'), Input('Global statistics', 'n_clicks'), Input('Age', 'n_clicks'), Input('Gender', 'n_clicks'), Input('Weight', 'n_clicks'), Input('Births', 'n_clicks')]
)
def update_global(n_clicks_education, n_clicks_stats, n_clicks_age, n_clicks_gender, n_clicks_weight, n_clicks_births):
    ctx = callback_context 
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == 'Education':
        return [education.show()]
    elif triggered_id == 'Global statistics':
        return [globalStats.show()]
    elif triggered_id == 'Age':
        return [age.show()]
    elif triggered_id == 'Gender':
        return [gender.show()]
    elif triggered_id == 'Weight':
        return [weight.show()]
    elif triggered_id == 'Births':
        return [births.show()]
    return [globalStats.show()]
# Callback pour mettre à jour la carte
@app.callback(
    Output("map-plotly", "figure"),
    Input("year-dropdown", "value")
)
def update_plotly_map(year):
    return US_map.create_plotly_map(year)


# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
