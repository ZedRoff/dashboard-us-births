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
        [
            dcc.Graph(id="age_graph", figure=age_glob.generate()),
            dcc.Graph(id="mother_age_graph", figure=mother_age_glob.generate()),
        ]
    )
