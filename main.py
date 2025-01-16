
from dash import html, Output, Input, Dash, callback_context

import dash_bootstrap_components as dbc
from views.homepage import homepage
from views.header import header
from views.local import local
from views.glob import glob
import views.globalStats as globalStats
import views.education as education
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
        content = glob()
    if len(triggered_id) == 0:
        return header("home"), content
    return header(triggered_id), content

@app.callback(
        [Output('main_global', 'children')],
        [Input('Education', 'n_clicks'), Input('Statistiques globales', 'n_clicks')]
)
def update_global(n_clicks_education, n_clicks_stats):
    ctx = callback_context 
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == 'Education':
        return [education.show()]
    elif triggered_id == 'Statistiques globales':
        return [globalStats.show()]
    return [globalStats.show()]
    

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
