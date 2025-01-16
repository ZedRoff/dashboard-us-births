"""
This module contains the global statistics for US births from 2016 to 2021.
It calculates and displays various statistics such as the year with the most births,
the highest and lowest maternal ages, and the highest recorded average birth weight.
"""

from dash import html
import pandas as pd

# Load the dataset
df = pd.read_csv("data/us_births_2016_2021.csv")

# Calculate various statistics
max_weight_row = df.loc[df["Average Birth Weight (g)"].idxmax()]
max_weight = df["Average Birth Weight (g)"].max()
state = max_weight_row["State"]

total_births_by_year = df.groupby("Year")["Number of Births"].sum()
max_births_year = total_births_by_year.idxmax()
max_births_value = total_births_by_year.max()

max_age_row = df.loc[df["Average Age of Mother (years)"].idxmax()]
max_age = max_age_row["Average Age of Mother (years)"]
state_with_max_age = max_age_row["State"]

min_age_row = df.loc[df["Average Age of Mother (years)"].idxmin()]
min_age = min_age_row["Average Age of Mother (years)"]
state_with_min_age = min_age_row["State"]


def show():
    """
    Returns the global statistics layout as HTML components for the dashboard.

    The function generates the layout containing global statistics, including the year
    with the most births, the highest recorded birth weight, and the highest and lowest
    maternal ages, along with the corresponding states.

    Returns:
        html.Div: The layout for the global statistics section.
    """
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H3(
                                "Year with Most Births", className="stat_global_title"
                            ),
                            html.Div(
                                [
                                    html.I(className="fa-solid fa-birthday"),
                                    html.P(f"{max_births_year}", className="stat_data"),
                                ],
                                className="data_splitter",
                            ),
                            html.Hr(),
                            html.H3("Value", className="stat_global_title"),
                            html.Div(
                                [
                                    html.I(className="fa-solid fa-birthday"),
                                    html.P(
                                        f"{max_births_value} births",
                                        className="stat_data",
                                    ),
                                ],
                                className="data_splitter",
                            ),
                        ],
                        className="section",
                    ),
                ],
                className="stat_global",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.H3(
                                "Highest Recorded Average Birth Weight",
                                className="stat_global_title",
                            ),
                            html.Div(
                                [
                                    html.I(className="fa-solid fa-birthday"),
                                    html.P(f"{max_weight} kg", className="stat_data"),
                                ],
                                className="data_splitter",
                            ),
                            html.Hr(),
                            html.H3("State", className="stat_global_title"),
                            html.Div(
                                [
                                    html.I(className="fa-solid fa-birthday"),
                                    html.P(f"{state}", className="stat_data"),
                                ],
                                className="data_splitter",
                            ),
                        ],
                        className="section",
                    ),
                ],
                className="stat_global",
            ),
            html.Div(
                [
                    html.H2("Maternal Age Overview"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H3(
                                        "Highest Average Age of Mother",
                                        className="stat_global_title",
                                    ),
                                    html.Div(
                                        [
                                            html.I(className="fa-solid fa-birthday"),
                                            html.P(f"{max_age}", className="stat_data"),
                                        ],
                                        className="data_splitter",
                                    ),
                                    html.Hr(),
                                    html.H3("State", className="stat_global_title"),
                                    html.Div(
                                        [
                                            html.I(className="fa-solid fa-birthday"),
                                            html.P(
                                                f"{state_with_max_age}",
                                                className="stat_data",
                                            ),
                                        ],
                                        className="data_splitter",
                                    ),
                                ],
                                className="section",
                            ),
                            html.Div(id="bar"),
                            html.Div(
                                [
                                    html.H3(
                                        "Lowest Average Age of Mother",
                                        className="stat_global_title",
                                    ),
                                    html.Div(
                                        [
                                            html.I(className="fa-solid fa-birthday"),
                                            html.P(f"{min_age}", className="stat_data"),
                                        ],
                                        className="data_splitter",
                                    ),
                                    html.Hr(),
                                    html.H3("State", className="stat_global_title"),
                                    html.Div(
                                        [
                                            html.I(className="fa-solid fa-birthday"),
                                            html.P(
                                                f"{state_with_min_age}",
                                                className="stat_data",
                                            ),
                                        ],
                                        className="data_splitter",
                                    ),
                                ],
                                className="section",
                            ),
                        ],
                        id="special_stat_global",
                    ),
                ],
                className="stat_global",
            ),
        ],
        id="stats_global",
    )
