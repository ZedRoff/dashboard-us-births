import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv('../data/us_births_2016_2021.csv')

# Créer un box plot avec les états comme catégorie
fig = px.box(
    df,
    x="State",  # Ajouter les États comme catégories sur l'axe X
    y="Average Age of Mother (years)",  # Âge moyen des mères
    title="Box Plot of Average Age of Mothers by State",
    labels={"State": "State", "Average Age of Mother (years)": "Average Age of Mothers (years)"},
    color_discrete_sequence=["#0A3161"],  # Couleur personnalisée
)

# Appliquer un style cohérent
fig.update_layout(
    title_font=dict(size=18, color="black"),  # Taille et couleur du titre
    title_x=0.5,  # Centrer le titre
    xaxis=dict(
        title="State",  # Titre de l'axe X
        showline=True,  # Ajouter une ligne pour l'axe X
        linecolor="black",  # Couleur de la ligne
        linewidth=2,  # Épaisseur de la ligne
        ticks="outside",
        tickwidth=2,
        tickcolor='black',
    ),
    yaxis=dict(
        title="Average Age of Mothers (years)",  # Titre de l'axe Y
        showline=True,  # Ajouter une ligne pour l'axe Y
        linecolor="black",  # Couleur de la ligne
        linewidth=2,  # Épaisseur de la ligne
        showgrid=True,  # Activer les lignes de la grille
        gridcolor="lightgrey",  # Couleur des lignes de la grille
        gridwidth=1,  # Épaisseur des lignes de la grille
        griddash="dash",  # Style des lignes de la grille
        ticks="outside",
        tickwidth=2,
        tickcolor='black',
    ),
    plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
)

# Afficher le graphique
fig.show()
