"""
Generates a bar chart showing the breakdown of mothers' average age ranges and 
the number of births for each age group, based on US births data from 2016 to 2021 
for a selected state.
"""

import pandas as pd
import plotly.express as px

# Load the CSV file containing the US births data
df = pd.read_csv("data/us_births_2016_2021.csv")


def generate(selected_state):
    """
    Creates a bar chart for a selected state showing the number of births 
    for each age range of mothers.
    
    Args:
        selected_state (str): The state for which the data should be displayed.
    
    Returns:
        plotly.graph_objects.Figure: The generated bar chart.
    """

    # Filter the data for the selected state
    df_state = df[df["State"] == selected_state]

    # Define age intervals for the average age of mothers
    age_intervals = pd.cut(
        df_state["Average Age of Mother (years)"], bins=range(22, 38, 2)
    )

    # Calculate the number of births in each age group
    age_counts = df_state.groupby(age_intervals, observed=False)[
        "Number of Births"
    ].sum()

    # Create a bar chart with Plotly
    fig = px.bar(
        x=age_counts.index.astype(str),  # Age groups (x-axis)
        y=age_counts.values,  # Number of births (y-axis)
        labels={"x": "Age range of mothers", "y": "Number of births"},
        title=f"Breakdown of mothers' average age: {selected_state}",
        text=age_counts.values,  # Display number on bars
        color_discrete_sequence=["#0A3161"],  # Custom bar color
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title="Age range of mothers (in years)",
        yaxis_title="Number of Births",
        title_font_size=20,
        plot_bgcolor="#FFFFFF",
        font={"size": 14},
        xaxis={
            "showline": True,
            "linecolor": "black",
            "linewidth": 2
        },
        yaxis={
            "showline": True,
            "linecolor": "black",
            "linewidth": 2,
            "showgrid": True,
            "gridcolor": "lightgrey",
            "gridwidth": 1,
            "ticks": "outside",
            "griddash": "dash",
            "tickwidth": 2,
            "tickcolor": "black"
        },
    )

    # Add borders to bars for better visibility
    fig.update_traces(marker_line_color="black", marker_line_width=1.5)

    # Return the generated figure
    return fig
