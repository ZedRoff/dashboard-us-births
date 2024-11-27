import dash
import numpy as np
import pandas as pd
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px

# Initialisation de l'application
app = dash.Dash(__name__)
app.title = "Dashboard Students Performance Factors"

# Charger le fichier StudentFactors.csv
df = pd.read_csv('StudentPerformanceFactors.csv')

# Calculer la ligne de tendance (Ordinary Least Squares - OLS)  
coeffs = np.polyfit(df['Hours_Studied'], df['Exam_Score'], 1)  # Régression linéaire
trendline = np.poly1d(coeffs)  # Fonction de la droite

# Trendline (ligne de tendance)
trace_trendline = go.Scatter(
    x=df['Hours_Studied'],
    y=trendline(df['Hours_Studied']),
    mode='lines',
    name=f"Tendance: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}",
    line=dict(color="red")
)

#Scatter plot
trace = go.Scatter(x= df['Hours_Studied'],
                   y= df['Exam_Score'],
                   mode = 'markers')

data = [trace]
layout = go.Layout( title="Comparaison entre le temps d'études et les performances",
                    xaxis=dict(title="Heures étudiées"),
                    yaxis=dict(title="Score à l'examen"))
fig = go.Figure(data=[trace, trace_trendline], layout=layout)
#fig.show()

# Filtrer les colonnes numériques
numeric_df = df.select_dtypes(include=['number'])

# Calcul des statistiques
statistics = pd.DataFrame({
    'Variable': numeric_df.columns,
    'Moyenne': numeric_df.mean(),
    'Médiane': numeric_df.median(),
    'Écart type': numeric_df.std()
}).reset_index(drop=True)

# Initialisation de l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='stats-table',
        columns=[{"name": col, "id": col} for col in statistics.columns],
        data=statistics.to_dict('records'),
        style_table={'margin': 'auto', 'width': '80%'},
        style_header={'backgroundColor': 'lightblue', 'fontWeight': 'bold'},
        style_cell={'textAlign': 'center', 'padding': '5px'}
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
 
# Regroupement des données en fonction de chaque variable pour le boxplot
x_data = ['Gender', 'School_Type', 'Parental_Education_Level']
y_data = [
    df[df['Gender'] == 'M']['Exam_Score'].values.tolist(),
    df[df['School_Type'] == 'Public']['Exam_Score'].values.tolist(),
    df[df['Parental_Education_Level'] == 'High School']['Exam_Score'].values.tolist()
]

# Définition des couleurs pour chaque catégorie
colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)']

# Création du graphique
fig = go.Figure()

# Ajout des traces de boxplot pour chaque catégorie
for xd, yd, cls in zip(x_data, y_data, colors):
    fig.add_trace(go.Box(
        y=yd,
        name=xd,
        boxpoints='all',  # Affichage de tous les points
        jitter=0.5,  # Permet de décaler les points pour plus de lisibilité
        whiskerwidth=0.2,  # Largeur des moustaches
        fillcolor=cls,  # Couleur du boxplot
        marker_size=5,  # Taille des points
        line_width=1  # Largeur des lignes
    ))

# Mise à jour du layout
fig.update_layout(
    title=dict(text='Distribution des scores par catégories'),
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor='rgb(255, 255, 255)',  # Couleur de la grille
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',  # Couleur de la ligne 0
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',  # Couleur de fond
    plot_bgcolor='rgb(243, 243, 243)',  # Couleur du fond du graphique
    showlegend=False  # Désactivation de la légende
)

# Afficher le graphique
#fig.show()
