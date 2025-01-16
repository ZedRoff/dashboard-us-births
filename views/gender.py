"""
This module defines the layout for the gender-related graph on the dashboard.
It includes a graph showing gender data.
"""

from dash import html, dcc
from components import gender_glob


def show():
    """
    Returns the layout for the gender graph.

    The graph displays gender-related data using data from the genderGlob component.

    Returns:
        html.Div: The layout containing the gender graph.
    """
    return html.Div([dcc.Graph(id="gender-graph", figure=gender_glob.generate())])
