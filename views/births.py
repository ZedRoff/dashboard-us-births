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
            html.H1("US Births map (2016-2021)"),
            dcc.Dropdown(
                id="year-dropdown",
                options=[
                    {"label": str(year), "value": year} for year in range(2016, 2022)
                ],
                value=2016,
                clearable=False,
            ),
            dcc.Graph(id="map-plotly", style={"height": "600px", "margin-top": "20px"}),
            dcc.Graph(id="test1", figure=tendance_glob.generate()),
        ]
    )
