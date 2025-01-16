import pandas as pd
import plotly.express as px

def generate():
    # Charger les données
    file_path = 'data/us_births_2016_2021.csv'   
    df = pd.read_csv(file_path)

    # Calculer la moyenne de l'âge des mères par niveau d'éducation
    mean = df.groupby('Education Level of Mother')['Average Age of Mother (years)'].mean().sort_values()

    # Créer un graphique en barres horizontales avec Plotly Express
    fig = px.bar(
        mean,
        x=mean.values,
        y=mean.index,
        orientation='h',
        title='Average Age of Mothers Grouped by Education Level',
        labels={'x': 'Average Age of Mother (years)', 'y': 'Education Level of Mother'},
        text=mean,
    )
    fig.update_traces(marker_color='#0A3161', marker=dict(line=dict(color='black', width=2)))  # Bordure noire autour des barres


    # Personnaliser la mise en page
    fig.update_layout(
        xaxis=dict(
        title='Average Age of Mother (years)',
        showline=True,
        linecolor='black',  # Ligne de l'axe des X
        linewidth=2,        # Épaisseur de la ligne de l'axe des X
        showgrid=True,      # Activer les lignes de la grille
        gridcolor='lightgrey',  # Couleur des lignes de la grille
        gridwidth=1,        # Épaisseur des lignes de la grille
        ticks="outside",
        tickwidth=2,
        tickcolor='black',
        griddash='dash',    # Lignes de la grille en pointillés
    ),
    yaxis=dict(
        title='Education Level of Mother',
        showline=True,
        linecolor='black', # Ligne de l'axe des Y
        linewidth=2,        # Épaisseur de la ligne de l'axe des Y
    ),
    title_font_size=18,
    title_x=0.5,  # Centrer le titre
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',  # Fond transparent
    bargap=0.5,  # Ajuster l'espacement entre les barres
    )


    # Afficher le graphique
    return fig

