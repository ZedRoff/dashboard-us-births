"""
This module contains the header component for the US Births dashboard. It generates
the top navigation bar with links to various pages (Home, Local Data, Global Data)
and a theme switch icon.
"""

from dash import html


def header(page):
    """
    Generates the header section of the webpage with navigation and theme switch.

    Args:
        page (str): The name of the current page. It can be "home", "local", or "global".
                    This is used to highlight the active navigation item.

    Returns:
        html.Header: The HTML structure for the header section with navigation.
    """
    return html.Header(
        [
            html.A(
                [
                    html.I(className="fa-solid fa-map-marker-alt"),
                    html.H1("US Births", id="title_main"),
                ],
                className="element_header",
                href="#",
            ),
            html.Div(
                [
                    html.A(
                        "Home",
                        className=(
                            "nav_item nav_item_active" if page == "home" else "nav_item"
                        ),
                        id="home",
                    ),
                    html.A(
                        "Local Data",
                        className=(
                            "nav_item nav_item_active"
                            if page == "local"
                            else "nav_item"
                        ),
                        id="local",
                    ),
                    html.A(
                        "Global Data",
                        className=(
                            "nav_item nav_item_active"
                            if page == "global"
                            else "nav_item"
                        ),
                        id="global",
                    ),
                      ],
                id="navbar",
            ),
        ],
        className="header_main",
    )
