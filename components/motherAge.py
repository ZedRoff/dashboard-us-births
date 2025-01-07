import pandas as pd
import plotly.express as px
df = pd.read_csv('../data/us_births_2016_2021.csv')


def generate():
    column_name = "Average Age of Mother (years)"

    # Créer un histogramme
    fig = px.histogram(
        df,
        x=column_name,
        nbins=15,  # Plus de détails avec davantage de bins
        title="Age distribution of mothers",
        labels={column_name: "Average age of mothers (in years)"},  # Renomme l'axe X
        color_discrete_sequence=["#4A7B9D"],  # Couleur personnalisée
    )

    # Ajouter des ajustements esthétiques
    fig.update_layout(
        title_font=dict(size=28, family="Comic Sans MS", color="black"),  # Police fun et couleur dorée
        xaxis=dict(
            title="Âge moyen des mères (années)",
            title_font=dict(size=18, family="Courier New", color="black"),  # Police classique en vert
            tickfont=dict(size=14, color="black"),  # Couleur des ticks
            gridcolor="white",
        ),
        yaxis=dict(
            title="Nombre de cas",
            title_font=dict(size=18, family="Courier New", color="black"),
            tickfont=dict(size=14, color="black"),
            gridcolor="white",
        ),
        margin=dict(l=50, r=50, t=80, b=50),  # Marges bien définies
    )

    # Ajouter des effets interactifs
    fig.update_traces(
        marker=dict(line=dict(color="#FFFFFF", width=2)),  # Bordure blanche autour des barres
        opacity=0.9,  # Légère transparence pour un effet "glossy"
    )

    fig.show()
generate()
