import plotly.graph_objects as go
import pandas as pd
import utils.helpers as helpers

def create_graph():

    # Charger les données
    df = helpers.load_data()

    # Assumer que "Fertility Rate" est déjà au bon format
    df["Fertility Rate"] = pd.to_numeric(df["Fertility Rate"], errors='coerce')

    # Vérifier que les colonnes nécessaires existent
    required_columns = ["Fertility Rate", "Country"]
    df.dropna(subset=["Fertility Rate"], inplace=True)

    # Créer des catégories pour le taux de fécondité
    categories = pd.cut(df["Fertility Rate"], bins=[0, 2, 4, 6, 8], labels=["<2 (Fertility rate below 2)", "2-4 (Fertility rate between 2 and 4)", "4-6 (Fertility rate between 4 and 6)", "6-8 Fertility rate between 6 and 8)"])

    # Compter le nombre de pays dans chaque catégorie
    category_counts = categories.value_counts()

    # Créer le graphique circulaire
    fig = go.Figure(data=[go.Pie(
        labels=category_counts.index,
        values=category_counts.values,
        marker=dict(colors=["#E74C3C", "#229954", "#884EA0", "#D0D3D4"],line=dict(width=2, color='black')  # Contour noir
    )
    )])

    # Mise à jour du layout
    fig.update_layout(
        title="Distribution of Countries by Fertility Rate",
        template="plotly_white"
    )

    return fig
