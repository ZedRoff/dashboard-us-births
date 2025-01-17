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
            html.H1("This page features visualizations that explore the relationship between a mother's education level and birth statistics. It includes data on the average number of births by education level and the average age of mothers grouped by their level of education.", className="desc"),
            html.Div([
                html.H3("🧒 Average number of births by mother's level of education"),
                dcc.Graph(
                id="education-gender-graph", figure=education_gender_glob.generate()
            ),
                 dcc.Graph(id="legend-graph", figure=legend_code.generate()),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("The data reveals a strong relationship between education levels and birth rates. Level 3 has the highest number of births, with 5,775,918. This could be because this education level represents a significant portion of the general population, many of whom are in age groups where starting families is common. Level 6 follows with 4,653,184 births, reflecting a group that balances career progression with family planning. Level 4 is close behind with 4,425,269 births, possibly indicating individuals who paused education to focus on family life. In contrast, lower education levels (1, 2) have fewer births, suggesting socioeconomic challenges or smaller population sizes within these groups. Higher education levels (7, 8) also show fewer births, with level 8 (doctorate) at just 627,705, likely due to delayed childbearing as individuals prioritize extended education and careers. This pattern highlights that intermediate education levels dominate births, potentially due to a combination of demographic prevalence and life circumstances conducive to starting families.")
                ], className="footer_graph")
            ], className="graph_block"),
            
             html.Div([
                html.H3("🎂 Average age of mothers grouped by education level"),
                dcc.Graph(
                id="education-gender-graph", figure=education_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("This graph shows the relationship between a mother’s education level and her average age at childbirth. The trend is clear: the higher the education level, the older the mother is at childbirth. Mothers with a doctorate or professional degree have the highest average age at 33.7 years, followed by master’s degree at 32.8 years and bachelor’s degree at 31.2 years. Mothers with an associate degree average 29.9 years, while those with lower education levels, like high school graduates, average 26.5 years, and those without a diploma are the youngest at 25.1 years. This suggests that higher education delays parenthood, likely due to extended studies and career focus, while lower education levels are linked to earlier childbirth, possibly due to economic or cultural factors.")
                ], className="footer_graph")
            ], className="graph_block")
            
            
        ], className="graphs_block"
    )
