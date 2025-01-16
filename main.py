"""
Dash web application for visualizing and interacting with US state data.
"""

from dash import html, Output, Input, Dash, callback_context, dcc, no_update

import dash_bootstrap_components as dbc

from views import (
    gender,
    global_stats,
    weight,
    births,
    education,
    age,
)
from views.homepage import homepage
from views.header import header
from views.local import local
from views.glob import glob

from components import (
    age_loc,
    education_gender_loc,
    education_loc,
    gender_loc,
    heatmap_loc,
    histogramme_loc,
    mother_age_loc,
    tendance_loc,
    weight_loc,
    us_map,
)

# Initialiser l'application Dash
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP], 
    suppress_callback_exceptions=True
)

# Layout de l'application avec la sidebar et contenu principal
app.layout = html.Div(
    [
        dcc.Store(id="current-location-store", storage_type="memory", data="Texas"),
        html.Div(header("home"), id="header"),
        html.Div(homepage(), id="content"),
    ],
    className="container_main",
)


# Callback pour détecter le clic sur un État
@app.callback(
    Output(
        "current-location-store", "data"
    ),  # Update the Store with the current location
    Input("map-plotly", "clickData")
)
def update_current_location(click_data):
    """
    Returns the location from a map click event or `dash.no_update` if no location is clicked.

    Parameters:
    - click_data (dict): The map click event data.

    Returns:
    - str or dash.no_update: Location code or `dash.no_update`.
    """
    if click_data and click_data["points"][0]["location"]:
        return click_data["points"][0]["location"]
    return no_update


@app.callback(
    Output("local_graphs", "children"),
    Input(
        "current-location-store", "data"
    )
)
def display_click_data(current_location):
    """
    Returns the payload of graphs based on the provided location.

    If no location is provided, returns an empty list.
    Otherwise, generates graphs using the location.

    Parameters:
    - current_location (str or None): The current location (state) or None.

    Returns:
    - list: A list of graphs if a valid location is provided, otherwise an empty list.
    """
    if current_location is None:
        return []
    return payload(current_location)


def payload(state):
    """
    Generates a list of graphs based on the provided state.

    Each graph is associated with different metrics and generated using respective functions.

    Parameters:
    - state (str): The state or location to generate the graphs for.

    Returns:
    - list: A list of `dcc.Graph` components for different metrics based on the state.
    """
    return [
        dcc.Graph(id="age_loc", figure=age_loc.generate(state)),
        dcc.Graph(id="education_loc", figure=education_loc.generate(state)),
        dcc.Graph(id="education_gender_loc", figure=education_gender_loc.generate(state)),
        dcc.Graph(id="heatmap_loc", figure=heatmap_loc.generate(state)),
        dcc.Graph(id="histogramme_loc", figure=histogramme_loc.generate(state)),
        dcc.Graph(id="mother_age_loc", figure=mother_age_loc.generate(state)),
        dcc.Graph(id="tendance_loc", figure=tendance_loc.generate(state)),
        dcc.Graph(id="weight_loc", figure=weight_loc.generate(state)),
        dcc.Graph(id="gender_loc", figure=gender_loc.generate(state)),
    ]


@app.callback(
    [Output("header", "children"), Output("content", "children")],
    [
        Input("home", "n_clicks"),
        Input("local", "n_clicks"),
        Input("global", "n_clicks"),
    ]
)
def update_header(*_):
    """
    Updates the header and content based on the triggered callback.

    The content displayed is determined by which button (home, local, or global) was clicked.

    Parameters:
    - *_ (unused): The arguments passed from the callback inputs (unused in the function).

    Returns:
    - tuple: A tuple containing the updated header and content.
    The header is updated based on the triggered button,
    and the corresponding content is returned (homepage, local, or global).
    """
    content = homepage()
    ctx = callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if triggered_id == "home":
        content = homepage()
    elif triggered_id == "local":
        content = local()
    elif triggered_id == "global":
        content = glob()
    else:
        content = homepage()
    if len(triggered_id) == 0:
        return header("home"), content
    return header(triggered_id), content


@app.callback(
    [Output("main_global", "children")],
    [
        Input("education", "n_clicks"),
        Input("global_statistics", "n_clicks"),
        Input("age", "n_clicks"),
        Input("gender", "n_clicks"),
        Input("weight", "n_clicks"),
        Input("births", "n_clicks"),
    ]
)
def update_global(*_):
    """
    Updates the content displayed in the global section based on the triggered callback.

    The content displayed is determined by which button (
        Education, Global statistics, Age, Gender, Weight, Births) was clicked.

    Parameters:
    - *_ (unused): The arguments passed from the callback inputs (unused in the function).

    Returns:
    - list: A list containing the corresponding content to
    display based on the triggered button.
            If no specific button is triggered, the 'Global statistics'
            content is returned by default.
    """
    print("test")
    ctx = callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
    corr = {
        "education": education.show(),
        "global_statistics": global_stats.show(),
        "age": age.show(),
        "gender": gender.show(),
        "weight": weight.show(),
        "births": births.show(),
    }
    if triggered_id in corr:
        return [corr[triggered_id]]
    return [global_stats.show()]


# Callback pour mettre à jour la carte
@app.callback(Output("map-plotly", "figure"), Input("year-dropdown", "value"))
def update_plotly_map(year):
    """
    Updates the Plotly map based on the selected year.

    This function takes the selected year from the dropdown and generates a new Plotly map using
    data corresponding to that year.

    Parameters:
    - year (str or int): The year selected by the user to update the map visualization.

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure object representing
    the updated map for the selected year.
    """
    return us_map.create_plotly_map(year)


# Exécution du serveur
if __name__ == "__main__":
    app.run_server(debug=True)
