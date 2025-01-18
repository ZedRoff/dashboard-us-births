"""
Generates a bar chart visualizing the average number of births by mother's education level,
filtered by the selected state using US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.graph_objects as go


def generate(state_filter: str) -> go.Figure:
    """
    Creates a bar chart showing the average number of births for each education level in
    the specified state based on the US births data from 2016 to 2021.

    Args:
        state_filter (str): The state for which the data will be filtered.

    Returns:
        plotly.graph_objects.Figure: The generated bar chart.
    """
    # Load the data
    file_path = "data/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)

    # Filter the data for the selected state
    df_state = birth_data[birth_data["State"] == state_filter]

    # Group the data by education level and sum the number of births for the selected state
    grouped_data = df_state.groupby("Education Level Code")["Number of Births"].sum().reset_index()

    # Convert education level codes to strings
    edu_codes_str = grouped_data["Education Level Code"].astype(str)

    # Create an interactive bar chart
    bar_chart = go.Figure()
    bar_chart.add_trace(
        go.Bar(
            x=edu_codes_str,
            y=grouped_data["Number of Births"],
            text=grouped_data["Number of Births"],
            textposition="outside",  # Position text outside the bars
            marker={"color": "#0A3161", "line": {"color": "black", "width": 3}},
            name=f"In {state_filter}",
        )
    )

    # Configure the appearance of the chart
    bar_chart.update_layout(
        title=f"Average number of births by mother's level of education in {state_filter}",
        xaxis_title="Education level code",
        yaxis_title="Average number of births",
        plot_bgcolor="#FFFFFF",  # Background color of the plot
        font={"size": 14},  # Font size for labels and title
        xaxis={
            "showline": True,
            "linecolor": "black",  # Color of the x-axis line
            "linewidth": 2,  # Thickness of the x-axis line
        },
        yaxis={
            "showline": True,
            "linecolor": "black",  # Color of the y-axis line
            "linewidth": 2,  # Thickness of the y-axis line
            "showgrid": True,  # Enable grid lines
            "gridcolor": "lightgrey",  # Color of the grid lines
            "gridwidth": 1,  # Thickness of the grid lines
            "ticks": "outside",  # Display ticks outside the axis
            "griddash": "dash",  # Dashed grid lines
            "tickwidth": 2,  # Thickness of the ticks
            "tickcolor": "black",  # Color of the ticks
        },
    )

    # Return the generated bar chart
    return bar_chart
