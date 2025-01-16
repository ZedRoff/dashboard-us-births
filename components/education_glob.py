"""
Generates a bar chart visualizing the average age of mothers by education level,
using US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.express as px


def generate():
    """
    Creates a bar chart showing the average age of mothers by education level.
    """
    # Load the data
    file_path = "data/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)

    # Calculate the mean age of mothers by education level
    mean = (
        birth_data.groupby("Education Level of Mother")["Average Age of Mother (years)"]
        .mean()
        .sort_values()
    )

    # Create a horizontal bar chart
    fig = px.bar(
        mean,
        x=mean.values,
        y=mean.index,
        orientation="h",
        title="Average Age of Mothers Grouped by Education Level",
        labels={"x": "Average Age of Mother (years)", "y": "Education Level of Mother"},
        text=mean,
    )

    # Customize bar appearance
    fig.update_traces(
        marker_color="#0A3161",
        marker={"line": {"color": "black", "width": 2}}  # Bar borders
    )

    # Customize layout
    fig.update_layout(
        xaxis={
            "title": "Average Age of Mother (years)",
            "showline": True,
            "linecolor": "black",  # X-axis line color
            "linewidth": 2,
            "showgrid": True,  # Grid lines
            "gridcolor": "lightgrey", 
            "gridwidth": 1,
            "ticks": "outside",
            "tickwidth": 2,
            "tickcolor": "black",
            "griddash": "dash",  # Dashed grid lines
        },
        yaxis={
            "title": "Education Level of Mother",
            "showline": True,
            "linecolor": "black",  # Y-axis line color
            "linewidth": 2,
        },
        title_font_size=18,
        title_x=0.5,  # Center title
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        bargap=0.5,  # Bar gap
    )

    # Return the figure
    return fig
