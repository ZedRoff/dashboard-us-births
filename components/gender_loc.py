"""
Generates a pie chart showing the distribution of births by gender for each year 
for a selected state using US births data (2016-2021).
"""

import pandas as pd
import plotly.express as px


def generate(selected_state):
    """
    Creates a pie chart displaying the distribution of births by gender for each year 
    in the specified state.
    
    Args:
        selected_state (str): The state to filter the data by.
    
    Returns:
        plotly.graph_objects.Figure: The generated pie chart.
    """
    # Load the data
    birth_data = pd.read_csv("data/us_births_2016_2021.csv")

    # Filter the data for the selected state
    df_state = birth_data[birth_data["State"] == selected_state]

    # Calculate the total number of births by gender for each year
    gender_year_counts = (
        df_state.groupby(["Year", "Gender"])["Number of Births"]
        .sum()
        .reset_index()
    )

    # Create a pie chart for each year
    fig = px.pie(
        gender_year_counts,
        hole=0.5,
        names="Gender",  # Gender of the baby
        values="Number of Births",  # Number of births by gender
        title=f"In {selected_state}",
        labels={"Number of Births": "Number of Births", "Gender": "Gender"},
        facet_col="Year",  # Create a subplot for each year
        facet_col_wrap=3,  # Display 3 years per row
        color="Gender",  # Use the 'Gender' column to define the colors
        color_discrete_map={
            "M": "#0A3161",  # Blue for males
            "F": "#B31942",  # Pink for females
        },
    )

    # Customize pie chart sections
    fig.update_traces(
        textinfo="percent+label",  # Display percentage and label in sections
        textfont={"family": "Arial", "size": 14, "color": "white", "weight": "bold"},
        marker={"line": {"color": "black", "width": 2}},
    )

    # Adjust appearance for better readability
    fig.update_layout(
        height=800,  # Height for better readability
        width=1200,  # Width to ensure everything is visible
        title_font_size=20,
        showlegend=False,
    )

    # Return the figure
    return fig
