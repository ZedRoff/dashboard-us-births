import plotly.express as px
import utils.helpers as helpers

def create_graph():

    # Load the data
    df = helpers.load_data()

    # Count the occurrences of each language
    language_counts = df["Official language"].value_counts()

    # Create a bar chart with a different color
    fig = px.bar(language_counts, 
                x=language_counts.index, 
                y=language_counts.values, 
                labels={"x": "Official Language", "y": "Number of Countries"},
                title="Number of Countries by Official Language", 
                color_discrete_sequence=["mediumseagreen"])  # Change color to mediumseagreen

    fig.update_layout(xaxis_title="Official Language", 
                    yaxis_title="Number of Countries", 
                    template="plotly_white")
    return fig
