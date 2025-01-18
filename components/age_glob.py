"""
Generates a bar chart visualizing the breakdown of mothers' average age ranges and 
the number of births in each age group using US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.express as px

# Load the CSV file containing the US births data
df = pd.read_csv("data/us_births_2016_2021.csv")


def generate() -> px.Figure:
    """
    Creates a bar chart showing the number of births for each age range of mothers.
    
    Returns:
        plotly.graph_objects.Figure: The generated bar chart.
    """

    # Check for missing values in the dataset
    if df["Average Age of Mother (years)"].isnull().any() or df["Number of Births"].isnull().any():
        raise ValueError("The dataset contains missing values in important columns.")

    # Define age intervals for the average age of mothers
    age_intervals = pd.cut(df["Average Age of Mother (years)"], bins=range(22, 38, 2))

    # Calculate the number of births in each age group
    age_counts = df.groupby(age_intervals, observed=False)["Number of Births"].sum()

    # Create a bar chart with Plotly
    fig = px.bar(
        x=age_counts.index.astype(str),  # Age groups (x-axis)
        y=age_counts.values,  # Number of births (y-axis)
        labels={"x": "Age range of mothers", "y": "Number of births"},
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
