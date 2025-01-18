"""
This module contains the homepage layout for the US Births dashboard. It includes
a brief introduction to the project, key statistics, and links to the data sources.
"""

from dash import html


def homepage():
    """
    Generates the homepage layout for the dashboard, including a description of the project,
    key statistics, and links to the data sources.

    Returns:
        tuple: A tuple containing the main content and the data source section.
    """
    return (
        html.Main(
            [
                html.Div(
                    [
                        html.H2("US Births from 2016 to 2021", id="subtitle_main"),
                        html.P(
                            """This minimalist dashboard, created for an ESIEE course, visualizes U.S. birth data.
                                It offers interactive features, allowing users to explore data by region or state, 
                                providing a clear and simple way to analyze birth distribution across the U.S.""",
                            id="description_main",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.I(className="fa-solid fa-location-dot"),
                                        html.H3("Graphs on local data", className="stat_title"),
                                        html.P("9", className="stat_data"),
                                    ],
                                    className="stat_card",
                                ),
                                html.Div(
                                    [
                                        html.I(
                                            className="fa-solid fa-earth-americas"
                                        ),
                                        html.H3("Graphs on global data", className="stat_title"),
                                        html.P("8", className="stat_data"),
                                    ],
                                    className="stat_card",
                                ),
                            ],
                            id="stats_main",
                        ),
                    ],
                    id="block_left",
                ),
                html.Video(
        src='/video.mp4', 
        controls=True, 
        width=600,  
        height=400, 
        id="image_main"
    ),
            ],
            id="block_main",
        ),
        html.Div(
            html.Div(
                [
                    html.H3("Data source", id="source_title"),
                    html.P(
                        '''The data in this dataset was obtained using CDC's 
                        WONDER retrieval tool on the CDC Natality page'''
                    ),
                    html.Div(
                        [
                            html.A("Kaggle", className="source_button", target="_blank", href="https://www.kaggle.com/datasets/danbraswell/temporary-us-births/data"),
                            
                        ],
                        id="source_buttons",
                    ),
                ],
                id="source",
            ),
            id="source_section",
        ),
    )
