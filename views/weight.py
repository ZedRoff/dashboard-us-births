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
    return html.Div([ 
        html.H2("Graphics about weight", className="graph_part_title"),
        html.Div([
                html.H3("⚖️👶 Distribution of average birth weight by gender (weighted)"),
                dcc.Graph(
                id="education-gender-graph", figure=weight_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("test")
                ], className="footer_graph")
            ], className="graph_block")
        
        ], className="graphs_block")
