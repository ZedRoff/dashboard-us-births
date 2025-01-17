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
                            """A minimalist dashboard developed for an 
                            ESIEE course that showcases US births data""",
                            id="description_main",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.I(className="fa-solid fa-flag icon_stat"),
                                        html.H3("States", className="stat_title"),
                                        html.P("51", className="stat_data"),
                                    ],
                                    className="stat_card",
                                ),
                                html.Div(
                                    [
                                        html.I(
                                            className="fa-solid fa-chart-bar icon_stat"
                                        ),
                                        html.H3("Graphs", className="stat_title"),
                                        html.P("15", className="stat_data"),
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
        src='assets/test_video.mp4',  # Path to the video file (e.g., in the 'assets' folder)
        controls=True,  # Adds play/pause, volume, and other controls
        width=600,  # Set the width of the video player
        height=400,  # Set the height of the video player
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
                            html.A("Kaggle", className="source_button", target="_blank", href="https://kaggle.com/datasets/danbraswell/temporary-us-births/discussion/407750"),
                            
                        ],
                        id="source_buttons",
                    ),
                ],
                id="source",
            ),
            id="source_section",
        ),
    )
