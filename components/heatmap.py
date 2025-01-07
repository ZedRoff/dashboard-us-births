import pandas as pd
import plotly.express as px
import utils.helpers as h
# Charger les données depuis le fichier CSV

df = pd.read_csv(h.load_data())
def generate():
    # Créer une heatmap pour afficher les poids moyens à la naissance par état et par année
    heatmap_data = df.pivot_table(
        values="Average Birth Weight (g)", 
        index="State",  # État
        columns="Year",  # Année
        aggfunc="mean"  # Moyenne des poids
    )

    # Créer la heatmap
    fig = px.imshow(
        heatmap_data,
        color_continuous_scale="Jet",  # Choix d'une palette de couleurs
        labels=dict(x="Année", y="État", color="Poids Moyen (grammes)"),
        title="Heatmap du Poids Moyen à la Naissance par État et par Année",
        template="plotly_dark"
    )

    # Ajuster l'apparence de la heatmap pour que tout soit visible
    fig.update_layout(
        height=1000,  # Ajuster la hauteur de la figure
        width=1500,  # Ajuster la largeur de la figure pour plus d'espace
        paper_bgcolor="#1A1A1A",  # Fond sombre
        plot_bgcolor="#2F4F4F",  # Fond de la carte
        xaxis=dict(tickangle=45),  # Rotation des étiquettes de l'axe x (années)
        yaxis=dict(tickangle=0),  # Rotation des étiquettes de l'axe y (états)
    )

    # Afficher le graphique
    return fig
