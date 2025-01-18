# age.py

"""
This module contains the logic for displaying global age and mother age graphs.
"""

from dash import html, dcc
from src.components import age_glob, mother_age_glob


def show() -> html.Div:
    """
    Returns the layout for displaying global age and mother age graphs.

    This function renders two graphs:
    - One for global age data
    - One for global mother age data
    """
    return html.Div(
        [ html.H2("Graphics about age", className="graph_part_title"),
          html.H1('''This page displays visualizations related to the distribution of mothers'
                  ages and their birth statistics. It includes a breakdown of births by age 
                  range and a box plot of the average age of mothers, offering insights
                  into the most common age groups for childbirth.''', className="desc"),
         html.Div([
                html.H3("👩‍🍼🔢📊 Breakdown of mothers' average age"),
                dcc.Graph(
                id="education-gender-graph", figure=age_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P('''This graph shows the distribution of births by mother's age,
                           grouped into age ranges. The dominant range is [26, 28], 
                           with 6,511,376 births, likely representing an ideal age 
                           for motherhood in many socio-economic contexts.
                           Other significant ranges include [30, 32] with 
                           4,789,040 births and [28, 30] with 4,298,360,
                           both showing a slight decrease compared to the
                           dominant range but still notable. Lower birth
                           numbers appear in the [24, 26] range with 3,026,823
                           births and [32, 34] with 3,540,036, reflecting 
                           a decline in births as age increases. The extremes,
                           [22, 24] and [34, 36], show the fewest births, indicating
                           that women at these ages either delay motherhood for personal
                           or career reasons or face fertility challenges.
                           This suggests that the optimal period for childbirth is between 26 and 32 years,
                           with younger women deferring motherhood for education or career, 
                           and older women experiencing a decrease in fertility
                           or having already started families.''')
                ], className="footer_graph")
            ], className="graph_block"),
         html.Div([
                html.H3("🎂 Box plot of average age of mothers"),
                dcc.Graph(
                id="education-gender-graph", figure=mother_age_glob.generate()
            ),
                html.Div([
                    html.I(className="fa-solid fa-info-circle"),
                    html.P('''This boxplot represents the average age of mothers.
                           The median is at 29.6 years, meaning half of the mothers
                           are younger than 29.6 years and half are older. The box 
                           shows the interquartile range (IQR) between the 1st quartile
                           (27 years) and the 3rd quartile (32 years), covering the central
                           50% of ages. The whiskers extend from about 24 years (lower whisker) 
                           to 36 years (upper whisker), indicating the range of ages outside the central 50%,
                           excluding outliers. The plot appears slightly skewed to the right, suggesting 
                           a positive asymmetry (more higher ages). There are no outliers, indicating 
                           a fairly uniform distribution of ages between the extremes. Overall, this 
                           shows a moderate distribution of ages with a median around 30 years 
                           and a range from 24 to 36 years.''')
                ], className="footer_graph")
            ], className="graph_block")
        ], className="graphs_block"
    )
