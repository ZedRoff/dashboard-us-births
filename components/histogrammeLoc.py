import pandas as pd
import plotly.express as px

# Charger les données
file_path = 'data/us_births_2016_2021.csv'
df = pd.read_csv(file_path)

# Créer une fonction pour afficher l'histogramme avec un style harmonisé
def generate(selected_state):
    # Filtrer les données pour l'état sélectionné
    df_state = df[df['State'] == selected_state]
    
    # Agréger le nombre de naissances par année pour l'état sélectionné
    births_by_year = df_state.groupby('Year')['Number of Births'].sum().reset_index()

    # Créer un histogramme avec Plotly
    fig = px.bar(
        births_by_year,
        x='Year',  # Utiliser la colonne 'Year' pour l'axe des X
        y='Number of Births',  # Utiliser la colonne 'Number of Births' pour l'axe des Y
        labels={'Year': 'Year', 'Number of Births': 'Number of births'},
        title=f'Number of births per year in {selected_state}',
        text='Number of Births',  # Ajouter les annotations des valeurs
        color_discrete_sequence=["#0A3161"]  # Spécification de la couleur des barres
    )
    
    # Personnaliser la mise en page
    fig.update_layout(
        xaxis=dict(
            title='Year',
            showline=True,
            linecolor='black',  # Ligne de l'axe des X
            linewidth=2,        # Épaisseur de la ligne de l'axe des X
           
        ),
        yaxis=dict(
            title='Number of births',
            showgrid=True,      # Activer les lignes de la grille
            gridcolor='lightgrey',  # Couleur des lignes de la grille
            gridwidth=1,        # Épaisseur des lignes de la grille
            griddash='dash',    # Lignes de la grille en pointillés
            showline=True,
            ticks="outside",
            tickwidth=2,
            tickcolor='black',
            linecolor='black',  # Ligne de l'axe des Y
            linewidth=2,        # Épaisseur de la ligne de l'axe des Y
        ),
        title_font_size=18,  # Taille de la police du titre
        title_x=0.5,  # Centrer le titre
        showlegend=False,  # Masquer la légende
        plot_bgcolor='rgba(0,0,0,0)',  # Fond transparent
        bargap=0.5,  # Ajuster l'espacement entre les barres
    )

    # Ajouter une personnalisation des barres
    fig.update_traces(
        marker_line_color='black',  # Bordures noires autour des barres
        marker_line_width=1.5,     # Épaisseur des bordures
        textposition='outside'     # Position des annotations à l'extérieur des barres
    )
    
    # Afficher le graphique
    return fig
