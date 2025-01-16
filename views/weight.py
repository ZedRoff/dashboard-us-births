"""
This module defines the layout for the "Weight Data" page of the US Births dashboard.
It displays a graph related to weight data using the `weightGlob` component.
"""

from dash import html, dcc
from components import weight_glob

def show():
    """
    Generates the layout for the "Weight Data" page, which includes a graph 
    visualizing weight data from the `weightGlob` component.

    Returns:
        html.Div: The layout for the "Weight Data" page.
    """
    return html.Div([dcc.Graph(id="test", figure=weight_glob.generate())])
