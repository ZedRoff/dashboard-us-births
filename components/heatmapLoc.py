import pandas as pd
import plotly.express as px

def generate(selected_state):
    # Charger les données depuis le fichier CSV
    df = pd.read_csv('data/us_births_2016_2021.csv')

    # Filtrer les données pour un état spécifique
    df_state = df[df['State'] == selected_state]

    # Créer une heatmap pour afficher les poids moyens à la naissance par année
    heatmap_data = df_state.pivot_table(
        values="Average Birth Weight (g)", 
        index="State",  # Ici uniquement un état, mais conserve la structure
        columns="Year",  # Année
        aggfunc="mean"  # Moyenne des poids
    )

    # Créer la heatmap
    fig = px.imshow(
        heatmap_data,
        color_continuous_scale="Jet",  # Choix d'une palette de couleurs
        labels=dict(x="Year", y="State", color="Average weight (grams)"),
        title=f"Heatmap of Average Birth Weight by Year ({selected_state})",
    )

    # Ajuster l'apparence de la heatmap
    fig.update_layout(
        height=800,  # Hauteur ajustée
        width=1000,  # Largeur ajustée
        xaxis=dict(tickangle=45),  # Rotation des étiquettes de l'axe x (années)
        yaxis=dict(tickangle=0),  # Rotation des étiquettes de l'axe y (état)
    )

    # Afficher le graphique
    return fig
