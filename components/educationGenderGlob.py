import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Charger les données
file_path = '../data/us_births_2016_2021.csv'
df = pd.read_csv(file_path)

# Grouper les données par niveau d'éducation et calculer la somme des naissances
a = df.groupby('Education Level Code')['Number of Births'].sum().reset_index()

# Convertir les codes d'éducation en chaîne de caractères
edu_codes_str = a['Education Level Code'].astype(str)

# Créer un graphique à barres interactif
bar_chart = go.Figure()
bar_chart.add_trace(go.Bar(
    x=edu_codes_str,
    y=a['Number of Births'],
    text=a['Number of Births'], 
    marker=dict(color='#0A3161', line=dict(color='black', width=3)),
    name="Nombre moyen de naissances", 
))

# Configurer l'apparence du graphique 
bar_chart.update_layout(
    title="Average number of births by mother's level of education",
    xaxis_title="Education level code",
    yaxis_title="Average number of births",
    plot_bgcolor='#FFFFFF',
    font=dict(size=14),
    xaxis=dict(
        showline=True,
        linecolor='black',  
        linewidth=2,    
    ),
    yaxis=dict(
        showline=True,
        linecolor='black', 
        linewidth=2,    
        showgrid=True,      # Active les lignes horizontales
        gridcolor='lightgrey',  # Couleur des lignes de la grille
        gridwidth=1,        # Épaisseur des lignes de la grille
        ticks="outside",    # Affiche les graduations à l'extérieur
        griddash='dash',    # Définit les lignes de la grille en pointillés
        tickwidth=2,        # Épaisseur des graduations
        tickcolor='black'   # Couleur des graduations    
    )
)


# Afficher les visualisations
bar_chart.show()
