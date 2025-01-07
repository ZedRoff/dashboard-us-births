import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(file_path)

# Calculer la moyenne de l'âge des mères par niveau d'éducation
df5 = df.groupby('Education Level of Mother')['Average Age of Mother (years)'].agg('mean').sort_values()

# Créer un graphique en barres horizontales
df5.plot.barh(
    xlabel='Average Age',  # Étiquette pour l'axe des abscisses
    ylabel='Education Level',  # Étiquette pour l'axe des ordonnées
    color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
           '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'],  # Couleurs des barres
    title='Average Age of Mothers Grouped by Education Level'  # Titre du graphique
)

# Afficher le graphique
plt.show()