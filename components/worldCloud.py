import io
import base64
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import utils.helpers as helpers

def create_graph():
    # Charger les données
    df = helpers.load_data()

    # Récupérer la colonne des langues officielles
    languages = df["Official language"].dropna()
    languages = languages.str.replace(" ", "_")

    # Créer le nuage de mots
    wordcloud = WordCloud(width=1000, height=400, background_color="purple", colormap="spring").generate(' '.join(languages))

    # Sauvegarder l'image du nuage de mots dans un buffer
    buffer = io.BytesIO()
    wordcloud.to_image().save(buffer, format="PNG")
    buffer.seek(0)

    # Encoder l'image en base64
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")

    # Retourner l'image en base64 sous forme d'une URL compatible avec Dash
    return f"data:image/png;base64,{img_base64}"
