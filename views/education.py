"""
This module defines the layout for the education-related graphs on the dashboard.
It includes graphs for education by gender, education, and a legend.
"""

from dash import html, dcc

from components import education_gender_glob, education_glob, legend_code


def show():
    """
    Returns the layout for the education-related graphs, including education by gender,
    education, and a legend graph.

    Returns:
        html.Div: The layout with the three graphs.
    """
    return html.Div(
        [
            dcc.Graph(
                id="education-gender-graph", figure=education_gender_glob.generate()
            ),
            dcc.Graph(id="legend-graph", figure=legend_code.generate()),
            dcc.Graph(id="education-graph", figure=education_glob.generate()),
        ]
    )
