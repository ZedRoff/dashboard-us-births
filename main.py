
from dash import html, Output, Input, Dash, callback_context, dcc

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

import components.ageLoc as ageLoc
import components.educationGenderLoc as educationGenderLoc
import components.educationLoc as educationLoc
import components.genderLoc as genderLoc
import components.heatmapLoc as heatmapLoc
import components.histogrammeLoc as histogrammeLoc
import components.motherAgeLoc as motherAgeLoc
import components.tendanceLoc as tendanceLoc
import components.weightLoc as weightLoc
import components.US_map as US_map
from callbacks import register_callbacks
# Initialiser l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div([html.Div(header("home"), id="header"), html.Div(homepage(), id="content")], className="container_main")

current_location = "Texas"
# Callback pour détecter le clic sur un État
@app.callback(
    Output('local_graphs', 'children'),
    Input('map-plotly', 'clickData')
)

def display_click_data(click_data):
    global current_location
    if click_data is None or click_data['points'][0]['location'] is None:
        pass
    else:
        # Extraire le nom de l'État cliqué
        current_location = click_data['points'][0]['location']
    return payload(current_location)

def payload(state):
    '''
    
import components.educationGenderLoc as educationGenderLoc
import components.educationLoc as educationLoc
import components.genderLoc as genderLoc
import components.heatmapLoc as heatmapLoc
import components.histogrammeLoc as histogrammeLoc
import components.motherAgeLoc as motherAgeLoc
import components.tendanceLoc as tendanceLoc
import components.weightLoc as weightLoc
    '''
    return [
        dcc.Graph(id="age_loc", figure=ageLoc.generate(state)), 
        dcc.Graph(id="education_loc", figure=educationLoc.generate(state)),
        dcc.Graph(id="education_gender_loc", figure=educationGenderLoc.generate(state)),
        dcc.Graph(id="heatmap_loc", figure=heatmapLoc.generate(state)),
        dcc.Graph(id="histogramme_loc", figure=histogrammeLoc.generate(state)),
        dcc.Graph(id="mother_age_loc", figure=motherAgeLoc.generate(state)),
        dcc.Graph(id="tendance_loc", figure=tendanceLoc.generate(state)),
        dcc.Graph(id="weight_loc", figure=weightLoc.generate(state))
    ]

@app.callback(
    [Output('header', 'children'), Output('content', 'children')],
    [Input('home', 'n_clicks'), Input('local', 'n_clicks'), Input('global', 'n_clicks')]
)

def update_header(n_clicks_home, n_clicks_local, n_clicks_global):
    global current_location
    content = homepage()
    ctx = callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if triggered_id == "home":
        content = homepage()
    elif triggered_id == "local":
        content = local(current_location)
    elif triggered_id == "global":
        content = glob()
    else:
        content = local(current_location)
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
