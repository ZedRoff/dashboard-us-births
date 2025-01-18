"""
Generates an interactive table displaying education levels of mothers and their corresponding codes 
using the US births data from 2016 to 2021.
"""

import pandas as pd
import plotly.graph_objects as go


def generate() -> go.Figure :
    """
    Creates an interactive table showing the education 
    levels of mothers and their corresponding codes.
    
    Returns:
        plotly.graph_objects.Figure: The generated interactive table.
    """
    # Charger les données
    file_path = "data/cleaned/us_births_2016_2021.csv"
    birth_data = pd.read_csv(file_path)

    # Créer une table descriptive
    # Remplacer les longues descriptions par une mise en forme plus concise
    education_levels = birth_data["Education Level of Mother"].unique()
    education_levels[7] = "Doctorate (PhD, EdD) or\nProfessional Degree (MD, DDS, etc.)"

    # Créer une table interactive
    table = go.Figure(
        data=[
            go.Table(
                header={
                    "values": ["Code", "Education Level"],
                    "fill_color": "#0A3161",
                    "align": "center",
                    "font": {"size": 14, "color": "white"},
                    "line_color": "black",  # Bordures noires pour les cellules
                    "line_width": 2,  # Épaisseur des bordures
                },
                cells={
                    "values": [
                        birth_data["Education Level Code"].unique(),
                        education_levels
                    ],
                    "fill_color": [
                        ["#B31942"] * len(education_levels),
                        ["#B31942"] * len(education_levels),
                    ],
                    "align": "center",
                    "font": {"size": 12, "color": "white"},
                    "line_color": "black",  # Bordures noires pour les cellules
                    "line_width": 2,  # Épaisseur des bordures
                },
            )
        ]
    )

    # Afficher les visualisations
    return table
