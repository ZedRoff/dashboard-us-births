import pandas as pd
import plotly.express as px

def generate(selected_state):
    # Charger le fichier CSV
    df = pd.read_csv('../data/us_births_2016_2021.csv')

    # Filtrer les données pour un état spécifique
    df_state = df[df['State'] == selected_state]

    # Calculer le nombre total de naissances par sexe pour chaque année
    gender_year_counts = df_state.groupby(['Year', 'Gender'])['Number of Births'].sum().reset_index()

    # Créer un graphique à secteurs pour chaque année
    fig = px.pie(
        gender_year_counts,
        hole=0.5,
        names="Gender",  # Sexe du bébé
        values="Number of Births",  # Nombre de naissances par sexe
        title=f"Breakdown of births by gender for each year ({selected_state})",
        labels={"Number of Births": "Number of Births", "Gender": "Gender"},
        facet_col="Year",  # Créer un sous-graphique pour chaque année
        facet_col_wrap=3,  # Afficher 3 années par ligne
        color="Gender",  # Utiliser la colonne 'Gender' pour définir les couleurs
        color_discrete_map={
            "M": "#0A3161",  # Bleu pour les garçons
            "F": "#B31942",  # Rose pour les filles
        }
    )

    # Ajouter des informations et ajuster le style des secteurs
    fig.update_traces(
        textinfo="percent+label",  # Affiche le pourcentage et le label dans les sections
        textfont=dict(family="Arial", size=14, color="white", weight="bold") 
    )

    # Ajuster l'apparence pour une meilleure lisibilité
    fig.update_layout(
        height=800,  # Hauteur pour une meilleure lisibilité
        width=1200,  # Largeur pour s'assurer que tout est visible
        title_font_size=20,
        showlegend=False
    )

    # Afficher le graphique
    return fig
