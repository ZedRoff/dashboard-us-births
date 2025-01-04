import pandas as pd
import plotly.express as px

# Charger les données depuis le fichier CSV
file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(file_path)

column_name = "Average Age of Mother (years)"

# Créer un histogramme
fig = px.histogram(
    df,
    x=column_name,
    nbins=15,  # Plus de détails avec davantage de bins
    title="Répartition des Âges des Mères",
    labels={column_name: "Âge moyen des mères (en années)"},  # Renomme l'axe X
    template="plotly_dark",  # Style sombre pour un effet dynamique
    color_discrete_sequence=["#FFA07A"],  # Couleur personnalisée
)

# Ajouter des ajustements esthétiques
fig.update_layout(
    title_font=dict(size=28, family="Comic Sans MS", color="#FFD700"),  # Police fun et couleur dorée
    xaxis=dict(
        title="Âge moyen des mères (années)",
        title_font=dict(size=18, family="Courier New", color="#32CD32"),  # Police classique en vert
        tickfont=dict(size=14, color="#87CEFA"),  # Couleur des ticks
        gridcolor="#444444",
    ),
    yaxis=dict(
        title="Nombre de cas",
        title_font=dict(size=18, family="Courier New", color="#32CD32"),
        tickfont=dict(size=14, color="#87CEFA"),
        gridcolor="#444444",
    ),
    paper_bgcolor="#1A1A1A",  # Fond sombre pour l'ensemble
    plot_bgcolor="#2F4F4F",  # Fond du graphique
    margin=dict(l=50, r=50, t=80, b=50),  # Marges bien définies
)

# Ajouter des effets interactifs
fig.update_traces(
    marker=dict(line=dict(color="#FFFFFF", width=2)),  # Bordure blanche autour des barres
    opacity=0.9,  # Légère transparence pour un effet "glossy"
)

# Afficher l'histogramme
fig.show()

