"""
Generates a heatmap showing the average birth weight by year
using US births data (2016-2021).
"""

import pandas as pd
import plotly.express as px


def generate(selected_state: str) -> px.imshow :
    """
    Creates a heatmap displaying the average birth weight by year for the specified state.
    
    Args:
        selected_state (str): The state to filter the data by.
    
    Returns:
        plotly.graph_objects.Figure: The generated heatmap with a bottom color bar.
    """
    # Load the data from CSV
    birth_data = pd.read_csv("data/cleaned/us_births_2016_2021.csv")

    # Filter the data for the selected state
    df_state = birth_data[birth_data["State"] == selected_state]

    # Create a pivot table for average birth weight by year
    heatmap_data = df_state.pivot_table(
        values="Average Birth Weight (g)",
        index="State",  # Only one state, but keeps structure
        columns="Year",  # Year
        aggfunc="mean",  # Average birth weight
    )

    # Create the heatmap
    fig = px.imshow(
        heatmap_data,
        color_continuous_scale="Jet",  # Choose a color scale
        labels={"x": "Year", "y": "State", "color": "Average weight (grams)"},
        title=f"Average Birth Weight by Year in {selected_state}",
    )

    # Customize heatmap appearance and move the color bar to the bottom
    fig.update_layout(
        height=800,  # Adjusted height
        xaxis={"tickangle": 45},  # Rotate x-axis labels (years)
        yaxis={"tickangle": 0},  # Rotate y-axis labels (state)
        coloraxis_colorbar={
    "title": "Avg Weight (g)",
    "orientation": "h",
    "x": 0.5,
    "y": -0.2,
    "ticks": "outside",
    "ticklen": 5,
    "tickcolor": "black",
    "len": 0.75,
    "thickness": 20
},
    )

    # Return the figure
    return fig
