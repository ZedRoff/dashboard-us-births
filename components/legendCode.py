
import pandas as pd
import plotly.graph_objects as go

def generate():
    # Charger les données
    file_path = 'data/us_births_2016_2021.csv'
    df = pd.read_csv(file_path)


    # Créer une table descriptive
    # Remplacer les longues descriptions par une mise en forme plus concise
    education_levels = df['Education Level of Mother'].unique()
    education_levels[7] = 'Doctorate (PhD, EdD) or\nProfessional Degree (MD, DDS, etc.)'

    # Créer une table interactive
    table = go.Figure(
        data=[go.Table(
            header=dict(
                values=["Code", "Niveau d'éducation"],
                fill_color='#0A3161',
                align='center',
                font=dict(size=14, color='white')
            ),
            cells=dict(
                values=[df['Education Level Code'].unique(), education_levels],
                fill_color=[["#B31942"] * len(education_levels), ["#B31942"] * len(education_levels)],
                align='center',
                font=dict(size=12, color="white")
            )
        )]
    )

    # Afficher les visualisations
    return table
