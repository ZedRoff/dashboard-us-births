# age.py

"""
This module contains the logic for displaying global age and mother age graphs.
"""

from dash import html, dcc
from components import age_glob, mother_age_glob


def show():
    """
    Returns the layout for displaying global age and mother age graphs.

    This function renders two graphs:
    - One for global age data
    - One for global mother age data
    """
    return html.Div(
        [ html.H2("Graphics about age", className="graph_part_title"),
         html.Div([
                html.H3("👩‍🍼🔢📊 Breakdown of mothers' average age"),
                dcc.Graph(
                id="education-gender-graph", figure=age_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("test")
                ], className="footer_graph")
            ], className="graph_block"),
         html.Div([
                html.H3("🎂 Box plot of average age of mothers"),
                dcc.Graph(
                id="education-gender-graph", figure=mother_age_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("test")
                ], className="footer_graph")
            ], className="graph_block")
          
        ], className="graphs_block"
    )
