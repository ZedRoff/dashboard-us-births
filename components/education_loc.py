"""
Generates a bar chart visualizing the average age of mothers by education level,
filtered by a specific state, using US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.express as px


def generate(state):
    """
    Creates a bar chart showing the average age of mothers by education level 
    in the specified state.
    
    Args:
        state (str): The state for which the data will be filtered.
    
    Returns:
        plotly.graph_objects.Figure: The generated bar chart.
    """
    # Load data
    file_path = "data/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)

    # Filter data for the specific state
    birth_data_state = birth_data[birth_data["State"] == state]

    # Calculate the mean age of mothers by education level for the selected state
    mean = (
        birth_data_state.groupby("Education Level of Mother")["Average Age of Mother (years)"]
        .mean()
        .sort_values()
    )

    # Create a horizontal bar chart
    fig = px.bar(
        mean,
        x=mean.values,
        y=mean.index,
        orientation="h",
        title=f"Average Age of Mothers in {state} Grouped by Education Level",
        labels={"x": "Average Age of Mother (years)", "y": "Education Level of Mother"},
        text=mean,
    )

    # Customize bar colors
    fig.update_traces(marker_color="#0A3161")

    # Customize layout
    fig.update_layout(
        xaxis={
            "title": "Average Age of Mother (years)",
            "showline": True,
            "linecolor": "black",  # X-axis line color
            "linewidth": 2,  # X-axis line thickness
            "showgrid": True,  # Show grid lines
            "gridcolor": "lightgrey",  # Grid line color
            "gridwidth": 1,  # Grid line thickness
            "griddash": "dash",  # Dashed grid lines
            "ticks": "outside",  # Ticks outside the axis
            "tickwidth": 2,
            "tickcolor": "black",  # Tick color
        },
        yaxis={
            "title": "Education Level of Mother",
            "showline": True,
            "linecolor": "black",  # Y-axis line color
            "linewidth": 2,  # Y-axis line thickness
        },
        title_font_size=18,
        title_x=0.5,  # Center title
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        bargap=0.5,  # Space between bars
    )

    # Return the figure
    return fig
