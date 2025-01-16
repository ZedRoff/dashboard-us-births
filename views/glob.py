"""
This module defines the layout for the global statistics page in the dashboard.
It includes the sidebar with different sections such as Global statistics, Education, etc.,
and the main content displaying the global statistics.
"""

from dash import html
import pandas as pd
from views import global_stats

# Read the dataset
df = pd.read_csv("data/us_births_2016_2021.csv")


def glob():
    """
    Returns the layout for the global statistics page.

    This function constructs the layout containing the sidebar with navigation options
    and the main content area displaying the global statistics.

    Returns:
        html.Main: The layout for the global statistics page.
    """
    return html.Main(
        [
            html.Div(
                [
                    html.Div(
                        [
                            sidebar_element("Global statistics"),
                            sidebar_element("Education"),
                            sidebar_element("Age"),
                            sidebar_element("Gender"),
                            sidebar_element("Weight"),
                            sidebar_element("Births"),
                        ],
                        id="elements_sidebar",
                    )
                ],
                id="sidebar",
            ),
            html.Div([global_stats.show()], id="main_global"),
        ],
        id="container_global",
    )


def sidebar_element(title):
    """
    Generates a sidebar element for a given section title.

    The sidebar element consists of a title and an icon indicating a collapsible section.

    Parameters:
        title (str): The title of the sidebar section.

    Returns:
        html.Div: A `Div` containing the sidebar section with title and icon.
    """
    return html.Div(
        [
            html.P(title, className="element_sidebar_title"),
            html.I(className="fa-chevron-right fa-solid"),
        ],
        className="element_sidebar",
        id=f"{title.replace(' ', '_').lower()}",  # More consistent ID
    )
