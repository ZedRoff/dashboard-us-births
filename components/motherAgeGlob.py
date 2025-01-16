import pandas as pd
import plotly.express as px

def generate():
    # Charger les données
    df = pd.read_csv('data/us_births_2016_2021.csv')

    # Nom de la colonne pour le box plot
    column_name = "Average Age of Mother (years)"

    # Créer un box plot
    fig = px.box(
        df,
        y=column_name,
        title="Box Plot of Average Age of Mothers",
        labels={column_name: "Average Age of Mothers (years)"},  # Renommer l'axe Y
        color_discrete_sequence=["#0A3161"],  # Couleur personnalisée
    )

    # Récupérer les statistiques pour chaque boîte
    stats = df[column_name].describe()

    # Ajouter des annotations avec les valeurs statistiques
    fig.add_annotation(
        x=0.2, 
        y=stats["50%"],  # Médiane
        text=f"Median: {stats['50%']:.1f}",  # Texte de l'annotation
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowcolor="black",
        font=dict(size=12, color="black"),
        bgcolor="lightgrey",
        bordercolor="black",
    )

    # Appliquer un style visuel cohérent
    fig.update_layout(
        title_font=dict(size=22, color="black"),  # Taille et couleur du titre
        title_x=0.5,  # Centrer le titre
        xaxis=dict(
            title="Average Age of Mothers (years)",  # Titre de l'axe X
            showline=True,  # Ajouter une ligne pour l'axe X
            linecolor="black",  # Couleur de la ligne
            linewidth=2,  # Épaisseur de la ligne
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
    return fig
