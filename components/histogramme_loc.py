"""
Generates a bar chart showing the number of births per year for a selected state 
using US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.express as px

# Load data
def generate(selected_state):
    """
    Creates a bar chart displaying the number of births per year for the specified state.
    
    Args:
        selected_state (str): The state to filter the data by.
    
    Returns:
        plotly.graph_objects.Figure: The generated bar chart.
    """
    file_path = "data/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)

    # Filter the data for the selected state
    df_state = birth_data[birth_data["State"] == selected_state]

    # Aggregate the number of births by year for the selected state
    births_by_year = df_state.groupby("Year")["Number of Births"].sum().reset_index()

    # Create a bar chart with Plotly
    fig = px.bar(
        births_by_year,
        x="Year",  # Use the 'Year' column for the X-axis
        y="Number of Births",  # Use the 'Number of Births' column for the Y-axis
        labels={"Year": "Year", "Number of Births": "Number of births"},
        title=f"Number of births per year in {selected_state}",
        text="Number of Births",  # Add value annotations
        color_discrete_sequence=["#0A3161"],  # Set the bar color
    )

    # Customize layout using dictionary literals
    fig.update_layout(
        xaxis={
            "title": "Year",
            "showline": True,
            "linecolor": "black",  # X-axis line color
            "linewidth": 2,  # X-axis line thickness
        },
        yaxis={
            "title": "Number of births",
            "showgrid": True,  # Enable grid lines
            "gridcolor": "lightgrey",  # Grid line color
            "gridwidth": 1,  # Grid line thickness
            "griddash": "dash",  # Dashed grid lines
            "showline": True,
            "ticks": "outside",
            "tickwidth": 2,
            "tickcolor": "black",
            "linecolor": "black",  # Y-axis line color
            "linewidth": 2,  # Y-axis line thickness
        },
        title_font_size=18,  # Title font size
        title_x=0.5,  # Center the title
        showlegend=False,  # Hide legend
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        bargap=0.5,  # Adjust the space between bars
    )

    # Customize bar styling
    fig.update_traces(
        marker_line_color="black",  # Add black borders around bars
        marker_line_width=1.5,  # Set border thickness
        textposition="outside",  # Position annotations outside bars
    )

    # Return the figure
    return fig
