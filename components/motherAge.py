import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv('../data/us_births_2016_2021.csv')

# Nom de la colonne pour l'histogramme
column_name = "Average Age of Mother (years)"

# Créer un histogramme
fig = px.histogram(
    df,
    x=column_name,
    nbins=15,  # Ajustement du nombre de bins
    title="Age Distribution of Mothers",
    labels={column_name: "Average Age of Mothers (years)"},  # Renomme l'axe X
    color_discrete_sequence=["#0A3161"],  # Couleur personnalisée
)

# Appliquer le style des autres graphiques
fig.update_layout(
    title_font=dict(size=18, color="black"),  # Taille et couleur du titre
    title_x=0.5,  # Centrer le titre
    xaxis=dict(
        title="Average Age of Mothers (years)",  # Titre de l'axe X
        showline=True,  # Ajouter une ligne pour l'axe X
        linecolor="black",  # Couleur de la ligne
        linewidth=2,  # Épaisseur de la ligne
        tickfont=dict(size=14, color="black"),  # Style des ticks
    ),
    yaxis=dict(
        title="Number of Cases",  # Titre de l'axe Y
        showline=True,  # Ajouter une ligne pour l'axe Y
        linecolor="black",  # Couleur de la ligne
        linewidth=2,  # Épaisseur de la ligne
        showgrid=True,  # Activer les lignes de la grille
        gridcolor="lightgrey",  # Couleur des lignes de la grille
        gridwidth=1,  # Épaisseur des lignes de la grille
        griddash="dash",  # Style des lignes de la grille
        tickfont=dict(size=14, color="black"),  # Style des ticks
    ),
    plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
    bargap=0.2,  # Espacement entre les barres
    margin=dict(l=50, r=50, t=50, b=50),  # Marges
)

# Ajouter des bordures et de la transparence aux barres
fig.update_traces(
    marker=dict(line=dict(color="white", width=2)),  # Bordure blanche autour des barres
    opacity=0.9,  # Transparence des barres
)

# Afficher le graphique
fig.show()
