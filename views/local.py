from dash import html, dcc
import components.US_map as US_map
import components.ageLoc as ageLoc
def local(state):
    return html.Main([
        html.Div([
           
             html.H1("US Births map (2016-2021)"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(year), "value": year} for year in range(2016, 2022)],
        value=2016,
        clearable=False,
    ),
    dcc.Graph(id="map-plotly", style={"height": "600px", "margin-top": "20px"})
        ], id="map_part"),
        html.Div([
            
        ], id="local_graphs")


    ], id="container_local")