import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

def run():

    # Charger les données depuis le CSV
    df = pd.read_csv("world-data-2023.csv")

    # Nettoyage des données : convertir les taux de fécondité en numérique
    df['Fertility Rate'] = pd.to_numeric(df['Fertility Rate'], errors='coerce')

    # Supprimer les lignes avec des valeurs manquantes dans le taux de fécondité
    df = df.dropna(subset=['Fertility Rate'])

    # Initialiser l'application Dash
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Créer l'histogramme pour la distribution des taux de fécondité avec personnalisation
    fig = px.histogram(
    df,
    x='Fertility Rate',  # Taux de fécondité sur l'axe X
    nbins=20,            # Nombre de bins pour l'histogramme
    title="Distribution des Taux de Fécondité dans le Monde",
    labels={"Fertility Rate": "Taux de Fécondité"},
    template="plotly",  # Template classique clair
    )

    # Styliser l'histogramme
    fig.update_traces(marker=dict(color='royalblue', line=dict(color='black', width=1)))

    # Personnaliser le titre et les axes
    fig.update_layout(
    title={
        'text': "Histogramme des Taux de Fécondité par Pays",
        'x': 0.5,  # Centrer le titre
        'xanchor': 'center',
        'font': {'size': 24, 'family': 'Arial', 'color': 'black'}
    },
    xaxis=dict(
        title="Taux de Fécondité",
        title_font={'size': 18, 'color': 'black'},
        tickfont={'size': 14, 'color': 'black'},
        gridcolor='lightgray',  # Gris clair pour les lignes de la grille
    ),
    yaxis=dict(
        title="Number of Countries",
        title_font={'size': 18, 'color': 'black'},
        tickfont={'size': 14, 'color': 'black'},
        gridcolor='lightgray',  # Gris clair pour les lignes de la grille
    ),
    plot_bgcolor='white',  # Fond du graphique en blanc
    paper_bgcolor='white',  # Fond extérieur du graphique
    showlegend=False,  # Désactiver la légende (pas nécessaire ici)
    margin=dict(t=40, b=40, l=50, r=50)  # Marges autour du graphique
    )

    # Définir la mise en page de l'application
    app.layout = html.Div([
    html.H1("Distribution des Taux de Fécondité dans le Monde", style={'textAlign': 'center', 'color': 'black'}),

    # Graphique interactif
    html.Div([
        dcc.Graph(
            id='fertility-rate-histogram',
            figure=fig
        )
    ])
    ])
    return fig
