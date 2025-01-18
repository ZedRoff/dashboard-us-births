"""
This module defines the layout for the US Births map dashboard.
It includes a dropdown for selecting years, a map to visualize the data,
and a graph for showing trends.
"""

from dash import html, dcc
from src.components import tendance_glob


def show() -> html.Div:
    """
    Returns the layout for the US Births map dashboard with a year dropdown,
    map, and trend graph.

    Returns:
        html.Div: The layout with a header, dropdown, map, and graphs.
    """
    return html.Div(
        [ 
         html.H2("Graphics about births", className="graph_part_title"),
         html.H1("This page features visualizations related to birth statistics in the United States, including a map showing the distribution of births by state from 2016 to 2021 and a chart displaying the number of births per year from 2016 to 2021.", className="desc"),
            html.Div([
                html.H3("🗺️ US Births map (2016-2021)"),
                dcc.Dropdown(
                id="year-dropdown",
                options=[
                    {"label": str(year), "value": year} for year in range(2016, 2022)
                ],
                value=2016,
                clearable=False,
            ),
            dcc.Graph(id="map-plotly", style={"height": "600px", "margin-top": "20px"}),
           
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("This image depicts a map of the United States, with states colored based on the number of births in each state. The color scale ranges from light beige (low birth numbers) to dark red (high birth numbers), with the scale at the bottom indicating value ranges from 50k to over 450k births. The most populous states, such as Texas (TX) and California (CA), are marked in dark red, indicating a very high number of births (likely above 400k). Florida (FL) and New York (NY) also have darker shades, reflecting significant birth numbers. On the other hand, states like Wyoming (WY), South Dakota (SD), Vermont (VT), and Alaska (AK) appear in light beige, suggesting much lower birth numbers, likely below 50k. Geographically, densely populated states on the East and West coasts tend to have higher birth numbers, while less populated states in the Midwest and Rocky Mountains show lower figures.")
                ], className="footer_graph"),
            ], className="graph_block"),
             html.Div([
                html.H3("👶📅 Number of births per year"),
                dcc.Graph(
                id="education-gender-graph", figure=tendance_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P("From 2016 to 2020, the number of births steadily decreased each year, likely reflecting a drop in birth rates and influenced by socio-economic and demographic factors. In 2016, births were around 4 million, but by 2020, the number had fallen to approximately 3.5 million. However, in 2021, there was a slight recovery, suggesting a potential shift in demographic behavior or social conditions, such as post-pandemic effects or birth rate support policies. This decline could be linked to a broader global trend of decreasing birth rates, economic impacts like the late-2010s crisis, and sociocultural shifts, such as the delay in having the first child. The small increase in 2021 deserves further analysis, as it might reflect a recovery after the pandemic.")
                ], className="footer_graph")
            ], className="graph_block")
            
        ], className="graphs_block"
    )
