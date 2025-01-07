import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/us_births_2016_2021.csv')

def generate():
    # Calculer le nombre total de naissances par sexe pour chaque année
    gender_year_counts = df.groupby(['Year', 'Gender'])['Number of Births'].sum().reset_index()
    # Créer un graphique à secteurs pour chaque année
    fig = px.pie(
        gender_year_counts,
        hole = 0.5,
        names="Gender",  # Sexe du bébé
        values="Number of Births",  # Nombre de naissances par sexe
        title="Distribution of births by sex for each year",
        labels={"Number of Births", "Gender"},
        facet_col="Year",  # Créer un sous-graphique pour chaque année
        facet_col_wrap=3,  # Afficher 3 années par ligne
        color="Gender",  # Utiliser la colonne 'Gender' pour définir les couleurs
        color_discrete_map={
            "M": "#3AABF6",  # Bleu pour les garçons
            "F": "#F63AAE",  # Rose pour les filles
        }
    )

    fig.update_traces(
    textinfo="percent+label",  # Affiche le pourcentage et le label dans les sections
       textfont=dict(family="Arial", size=14, color="white", weight="bold") 
    )

    # Ajuster l'apparence pour améliorer la lisibilité
    fig.update_layout(
        height=800,  # Hauteur pour une meilleure lisibilité
        width=1200,  # Largeur pour s'assurer que tout est visible
        title="Distribution of births by sex for each year",
         legend=dict(
            orientation="v",  # Orientation verticale
            y=-0.3,  # Placer la légende sous le graphique
            x=0.1,
        )
    )
    fig.show()
generate()
