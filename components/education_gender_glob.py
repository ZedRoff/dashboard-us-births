"""
Generates a bar chart visualizing the average number of births by mother's education level.
The chart uses US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.graph_objects as go


def generate():
    """
    Creates a bar chart showing the average number of births for each level of education
    based on the US births data from 2016 to 2021.
    
    Returns:
        plotly.graph_objects.Figure: The generated bar chart.
    """

    # Load the data
    file_path = "data/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)
    b_d = birth_data
    # Group the data by education level and sum the number of births
    grouped_data = b_d.groupby("Education Level Code")["Number of Births"].sum().reset_index()

    # Convert education level codes to strings
    edu_codes_str = grouped_data["Education Level Code"].astype(str)

    # Create an interactive bar chart
    bar_chart = go.Figure()
    bar_chart.add_trace(
        go.Bar(
            x=edu_codes_str,
            y=grouped_data["Number of Births"],
            text=grouped_data["Number of Births"],
            marker={"color": "#0A3161", "line": {"color": "black", "width": 3}},
            name="Average number of births",
        )
    )

    # Configure the appearance of the chart
    bar_chart.update_layout(
        title="Average number of births by mother's level of education",
        xaxis_title="Education level code",
        yaxis_title="Average number of births",
        plot_bgcolor="#FFFFFF",
        font={"size": 14},
        xaxis={
            "showline": True,
            "linecolor": "black",
            "linewidth": 2,
        },
        yaxis={
            "showline": True,
            "linecolor": "black",
            "linewidth": 2,
            "showgrid": True,  # Enable horizontal grid lines
            "gridcolor": "lightgrey",  # Grid line color
            "gridwidth": 1,  # Grid line thickness
            "ticks": "outside",  # Display ticks outside the axis
            "griddash": "dash",  # Grid lines as dashed
            "tickwidth": 2,  # Tick thickness
            "tickcolor": "black",  # Tick color
        },
    )

    # Return the generated bar chart
    return bar_chart
