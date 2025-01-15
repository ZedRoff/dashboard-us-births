import pandas as pd
import plotly.express as px

# Charger les données
file_path = '../data/us_births_2016_2021.csv'
df = pd.read_csv(file_path)

# Créer une nouvelle colonne pondérée (poids multiplié par le nombre de naissances)
df['Weighted Birth Weight'] = df['Average Birth Weight (g)'] * df['Number of Births']

# Créer un histogramme avec les données pondérées
fig = px.histogram(
    df,
    x='Average Birth Weight (g)',  # On conserve l'axe x avec les poids moyens
    y='Weighted Birth Weight',    # L'axe y devient les poids pondérés
    color='Gender',
    title='Distribution of Average Birth Weight by Gender (Weighted)',
    labels={
        'Average Birth Weight (g)': 'Average Birth Weight (g)',
        'Weighted Birth Weight': 'Weighted Total Birth Weight (g)',
    },
    nbins=30,
    color_discrete_sequence=['#B31942', '#0A3161'],
    text_auto=True,
)

# Personnaliser la mise en page
fig.update_layout(
    xaxis_title='Average Birth Weight (g)',
    yaxis_title='Weighted Total Birth Weight (g)',
    title_font_size=20,
    plot_bgcolor='#FFFFFF',
    font=dict(size=14),
    showlegend=False,
    xaxis=dict(
        showline=True,
        linecolor='black',
        linewidth=2,
    ),
    yaxis=dict(
        showline=True,
        linecolor='black',
        linewidth=2,
        showgrid=True,
        gridcolor='lightgrey',
        gridwidth=1,
        ticks="outside",
        griddash='dash',
        tickwidth=2,
        tickcolor='black'
    ),
)

# Ajouter une bordure aux barres
fig.update_traces(
    marker_line_color='black',
    marker_line_width=1.5,
)

# Afficher le graphique
fig.show()
