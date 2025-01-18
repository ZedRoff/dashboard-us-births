import pandas as pd
import plotly.express as px


def generate(selected_state: str) -> px.Figure :
    """
    Creates a heatmap displaying the average birth weight by year for the specified state.
    
    Args:
        selected_state (str): The state to filter the data by.
    
    Returns:
        plotly.graph_objects.Figure: The generated heatmap with a bottom color bar.
    """
    # Load the data from CSV
    birth_data = pd.read_csv("data/us_births_2016_2021.csv")

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
        coloraxis_colorbar=dict(
            title="Avg Weight (g)",  # Title for the legend
            orientation="h",  # Horizontal orientation
            x=0.5,  # Center the color bar horizontally
            y=-0.2,  # Position it below the graph
            ticks="outside",  # Place ticks outside the color bar
            ticklen=5,  # Length of the ticks
            tickcolor="black",  # Color of the ticks
            len=0.75,  # Length of the color bar as a fraction of the graph width
            thickness=20,  # Thickness of the color bar
        ),
    )

    # Return the figure
    return fig
