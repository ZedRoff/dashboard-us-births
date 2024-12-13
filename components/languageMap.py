import plotly.express as px
import utils.helpers as helpers
import random


def create_graph():

    # Charger les données
    df = helpers.load_data()

    # Nettoyer les données en supprimant les lignes manquantes
    df = df.dropna(subset=["Country", "Official language"])

    # Générer des couleurs aléatoires
    def generate_random_color():
        return f"#{random.randint(0, 0xFFFFFF):06x}"

    # Créer un dictionnaire de couleurs pour chaque langue en utilisant des couleurs aléatoires
    languages = df["Official language"].unique()
    language_colors = {lang: generate_random_color() for lang in languages}

    # Créer un graphique basé sur les coordonnées géographiques (latitude, longitude)
    fig = px.scatter_geo(df, 
                        lat="Latitude",  # Utiliser la latitude
                        lon="Longitude",  # Utiliser la longitude
                        color="Official language",  # Utiliser la langue officielle pour colorier les pays
                        hover_name="Country",  # Afficher le nom du pays au survol
                        title="Official Languages of the World",
                        color_discrete_map=language_colors,  # Appliquer le dictionnaire de couleurs
                        projection="natural earth")  # Type de projection de la carte

    # Mise à jour du layout pour une meilleure lisibilité
    fig.update_layout(template="plotly_white")

    return fig
