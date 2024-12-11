import plotly.graph_objects as go
import utils.helpers as helpers

def create_graph():
    # Charger le fichier CSV (remplace "world-data-2023.csv" par le chemin exact)
    df = helpers.load_data()

    # Vérifier si les colonnes nécessaires existent
    required_columns = ['Country', 'Fertility Rate', 'Life expectancy', 'Population']
    if not all(col in df.columns for col in required_columns):
        print("Le fichier CSV ne contient pas toutes les colonnes nécessaires.")
        return

    # Créer le graphique à bulles
    fig = go.Figure()

    df['Population'] = df['Population']
    fig.add_trace(go.Scatter(
        x=df['Fertility Rate'],
        y=df['Life expectancy'],
        mode='markers',
        marker=dict(
            size=df['Population'] / 1e6,  # Ajuster la taille pour une meilleure lisibilité 
            sizemode='area',
           colorscale='Viridis',
            showscale=True
        ),
        text=df['Country'],  # Ajouter le nom des pays comme info-bulle
        name="Pays"
    ))

    # Mise en forme du graphique
    fig.update_layout(
        title="Relation entre le taux de fécondité, l'espérance de vie et la population",
        xaxis_title="Taux de fécondité",
        yaxis_title="Espérance de vie",
        legend_title="Légende",
        template="plotly_white",
        showlegend=False
    )

    return fig
