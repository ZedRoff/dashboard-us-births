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
    return html.Div([ 
        html.H2("Graphic about genders", className="graph_part_title"),
        html.Div([
                html.H3("📊👶 Distribution of births sex for each year"),
                dcc.Graph(
                id="education-gender-graph", figure=gender_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("test")
                ], className="footer_graph")
            ], className="graph_block")
    ], className="graphs_block")
