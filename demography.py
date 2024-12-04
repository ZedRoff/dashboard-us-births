import pandas as pd
import plotly.graph_objects as go
def run():
    # Charger le fichier CSV (remplace "world-data-2023.csv" par le chemin exact)
    df = pd.read_csv("world-data-2023.csv")

    # Nom du pays à analyser
    pays_sélectionné = 'France'  # Remplacez par le nom du pays souhaité

    # Filtrer les données pour le pays sélectionné
    df_pays = df[df['Country'] == pays_sélectionné]

    # Vérifier si le pays existe
    if df_pays.empty:
        print(f"Le pays {pays_sélectionné} n'est pas trouvé dans le dataset.")
    else:
    # Extraire les données d'intérêt
        birth_rate = df_pays['Birth Rate'].values[0]
        fertility_rate = df_pays['Fertility Rate'].values[0]
        life_expectancy = df_pays['Life expectancy'].values[0]

    # Créer le graphique combiné
        fig = go.Figure()

    # Ajouter les barres pour Birth Rate et Fertility Rate
        fig.add_trace(go.Bar(
        x=['Birth Rate', 'Fertility Rate'],
        y=[birth_rate, fertility_rate],
        name='Rate',
        marker_color='blue'
        ))

    # Ajouter une ligne pour Life Expectancy
        fig.add_trace(go.Scatter(
        x=['Birth Rate', 'Fertility Rate'],
        y=[life_expectancy, life_expectancy],  # Associer une ligne horizontale
        mode='markers',
        name="Life expectancy",
        line=dict(color='red', width=3),
        marker=dict(size=10)
        ))

        # Mise en forme du graphique
        fig.update_layout(
        title=f"Indicateurs démographiques pour {pays_sélectionné}",
        xaxis_title="Indicateurs",
        yaxis_title="Valeurs",
        legend_title="Légende",
        template="plotly_white"
        )

    # Afficher le graphique
        return fig