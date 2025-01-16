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
            html.H2("Graphics about education", className="graph_part_title"),
            html.Div([
                html.H3("🧒 Average number of births by mother's level of education"),
                dcc.Graph(
                id="education-gender-graph", figure=education_gender_glob.generate()
            ),
                 dcc.Graph(id="legend-graph", figure=legend_code.generate()),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("Mothers that are High School graduate or that have a GED completed overall give birth to more childrens than average. Thus, the higher the education background, the lower the amount of childrens from a mother")
                ], className="footer_graph")
            ], className="graph_block"),
            
             html.Div([
                html.H3("🎂 Average age of mothers grouped by education level"),
                dcc.Graph(
                id="education-gender-graph", figure=education_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("Doctorate or Professional Degree mothers tend to make childrens later than those who studied till their 9th through 12th. Thus, the higher the education background, the later they make the childrens.")
                ], className="footer_graph")
            ], className="graph_block")
            
            
        ], className="graphs_block"
    )
