import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

# Charger les données depuis le CSV
# Remplacez 'votre_fichier.csv' par le chemin réel vers votre fichier CSV
df = pd.read_csv("world-data-2023.csv")

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Définir la mise en page de l'application
app.layout = html.Div([
    html.H1("Population Totale et Densité par Pays", style={'textAlign': 'center'}),
    
    # Dropdown pour choisir un sous-ensemble de pays
    html.Div([
        html.Label("Choisissez des pays :"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in df['Country']],
            value=df['Country'][:5],  # Sélectionne les 5 premiers pays par défaut
            multi=True
        )
    ], style={'width': '70%', 'margin': 'auto'}),
    
    # Graphique interactif
    html.Div([
        dcc.Graph(id='population-density-chart')
    ])
])

# Callback pour mettre à jour le graphique
@app.callback(
    Output('population-density-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_chart(selected_countries):
    # Filtrer les données pour les pays sélectionnés
    filtered_df = df[df['Country'].isin(selected_countries)]
    
    # Créer le graphique
    fig = go.Figure()

    # Ajouter les barres pour la population totale
    fig.add_trace(go.Bar(
        x=filtered_df['Country'],
        y=filtered_df['Population'],
        name='Population Totale',
        marker_color='blue',
        yaxis='y1'
    ))

    # Ajouter les points pour la densité
    fig.add_trace(go.Scatter(
        x=filtered_df['Country'],
        y=filtered_df['Density (P/Km2)'],
        mode='markers+lines',
        name='Densité (P/Km²)',
        marker=dict(color='red', size=10),
        yaxis='y2'
    ))

    # Ajouter les axes secondaires
    fig.update_layout(
        title="Comparaison de la Population Totale et de la Densité par Pays",
        xaxis=dict(title="Pays"),
        yaxis=dict(
            title="Population Totale",
            titlefont=dict(color="blue"),
            tickfont=dict(color="blue")
        ),
        yaxis2=dict(
            title="Densité (P/Km²)",
            titlefont=dict(color="red"),
            tickfont=dict(color="red"),
            overlaying='y',
            side='right'
        ),
        legend=dict(x=0.1, y=1.1),
        barmode='group',
        template='plotly'
    )

    return fig

# Lancer le serveur
if __name__ == '__main__':
    app.run_server(debug=True)
