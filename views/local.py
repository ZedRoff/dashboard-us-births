"""
This module defines the layout for the "Local Data" page of the US Births dashboard.
It displays a map for US births from 2016 to 2021 along with a dropdown to filter by year.
"""

from dash import html, dcc


def local():
    """
    Generates the layout for the "Local Data" page, which includes a dropdown to select 
    the year and a map that visualizes US births data from 2016 to 2021.

    Returns:
        html.Div: The layout for the "Local Data" page.
    """
    return html.Main(
        [
            html.Div(
                [
                    html.H1("US Births map (2016-2021)"),
                    dcc.Dropdown(
                        id="year-dropdown",
                        options=[
                            {"label": str(year), "value": year}
                            for year in range(2016, 2022)
                        ],
                        value=2016,
                        clearable=False,
                    ),
                    dcc.Graph(
                        id="map-plotly",
                        style={"height": "600px", "margin-top": "20px"}
                    ),
                ],
                id="map_part",
            ),
            html.Div([], id="local_graphs"),
        ],
        id="container_local",
    )
