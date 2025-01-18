"""
This module defines the layout for the "Weight Data" page of the US Births dashboard.
It displays a graph related to weight data using the `weightGlob` component.
"""

from dash import html, dcc
from components import weight_glob

def show() -> html.Div :
    """
    Generates the layout for the "Weight Data" page, which includes a graph 
    visualizing weight data from the `weightGlob` component.

    Returns:
        html.Div: The layout for the "Weight Data" page.
    """
    return html.Div([ 
        html.H2("Graphics about weight", className="graph_part_title"),
          html.H1("This page presents a histogram displaying the distribution of average birth weights by gender (girls in red, boys in blue).", className="desc"),
        html.Div([
                html.H3("⚖️👶 Distribution of average birth weight by gender (weighted)"),
                dcc.Graph(
                id="education-gender-graph", figure=weight_glob.generate()
            ),
                html.Div([
                    html.H3("Legend", className="legend_title"),
                    html.Ul([
                        html.Li([
                            html.Div("", className="square-1"),
                            html.P("Male")
                        ], className="legend_element"),
                          html.Li([
                            html.Div("", className="square-2"),
                            html.P("Female")
                        ], className="legend_element")
                    ], className="legend_list")
                ], className="legend_block"),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("The histogram, divided into red bars (girls) and blue bars (boys), shows the distribution of average birth weights, ranging from 2600 g to 3600 g, with a concentration between 3200 g and 3400 g. Boys tend to dominate the higher weight ranges, especially between 3400 g and 3600 g, while girls are more common in the 3000 g to 3400 g range. The highest total weighted birth weight is centered around 3200 g to 3300 g, with girls having slightly higher weights in this range. Overall, most births have an average weight between 3100 g and 3400 g, with boys being slightly heavier in the higher weight ranges.")
                ], className="footer_graph")
            ], className="graph_block")
        
        ], className="graphs_block")
