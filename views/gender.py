"""
This module defines the layout for the gender-related graph on the dashboard.
It includes a graph showing gender data.
"""

from dash import html, dcc
from components import gender_glob


def show() -> html.Div:
    """
    Returns the layout for the gender graph.

    The graph displays gender-related data using data from the genderGlob component.

    Returns:
        html.Div: The layout containing the gender graph.
    """
    return html.Div([ 
        html.H2("Graphic about genders", className="graph_part_title"),
        html.H1("This page features ring charts showing the distribution of births by gender (Male: M, Female: F) from 2016 to 2021.", className="desc"),
        html.Div([
                html.H3("📊👶 Distribution of births sex for each year"),
                dcc.Graph(
                id="education-gender-graph", figure=gender_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("This series of ring charts shows the gender distribution (M: Male, F: Female) from 2016 to 2021. The gender proportions are consistent across the years, with a slight male majority. In 2016, the distribution was M: 51.1% and F: 48.9%, and remained nearly the same in the following years. The variations are minimal, ranging from 0.1% to 0.2%, indicating a stable gender distribution over the six years. The data highlights a slight male majority with no significant gender imbalances during the period analyzed.")
                ], className="footer_graph")
            ], className="graph_block")
    ], className="graphs_block")
