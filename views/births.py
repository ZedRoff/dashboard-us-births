"""
This module defines the layout for the US Births map dashboard.
It includes a dropdown for selecting years, a map to visualize the data,
and a graph for showing trends.
"""

from dash import html, dcc
from components import tendance_glob


def show():
    """
    Returns the layout for the US Births map dashboard with a year dropdown,
    map, and trend graph.

    Returns:
        html.Div: The layout with a header, dropdown, map, and graphs.
    """
    return html.Div(
        [ 
         html.H2("Graphics about births", className="graph_part_title"),
            html.Div([
                html.H3("🗺️ US Births map (2016-2021)"),
                dcc.Dropdown(
                id="year-dropdown",
                options=[
                    {"label": str(year), "value": year} for year in range(2016, 2022)
                ],
                value=2016,
                clearable=False,
            ),
            dcc.Graph(id="map-plotly", style={"height": "600px", "margin-top": "20px"}),
           
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("test")
                ], className="footer_graph"),
            ], className="graph_block"),
             html.Div([
                html.H3("👶📅 Number of births per year"),
                dcc.Graph(
                id="education-gender-graph", figure=tendance_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("test")
                ], className="footer_graph")
            ], className="graph_block")
            
        ], className="graphs_block"
    )
