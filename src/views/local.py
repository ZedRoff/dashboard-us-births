"""
This module defines the layout for the "Local Data" page of the US Births dashboard.
It displays a map for US births from 2016 to 2021 along with a dropdown to filter by year.
"""

from dash import html, dcc


def local() -> html.Main:
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
            html.Div([
                html.H2("🌍 Local Graphs", id="title_city"),
                html.P('''The page features a set of interactive graphs
                       that update based on the selected state.
                       When the user clicks on a specific state,
                       the graphs at the top of the page are 
                       immediately modified to reflect the data
                       related to that state. This interaction
                       allows users to personalize the graph
                       view according to the information they wish
                       to explore.''', className="desc"),
                html.Div([], id="local_graphs"),
                html.Div([
                    html.I(className="fa-solid fa-sticky-note info_scroll_icon"),
                    html.P("Scroll down to see more graphs", id="info_scroll_data")
                ], id="info_scroll_block")
            ], id="container_right_local")
        ],
        id="container_local",
    )
