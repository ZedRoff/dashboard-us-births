import pandas as pd
import plotly.express as px

# Charger les données
file_path = '../data/us_births_2016_2021.csv'
df = pd.read_csv(file_path)

# Calculer la moyenne de l'âge des mères par niveau d'éducation
mean = df.groupby('Education Level of Mother')['Average Age of Mother (years)'].mean().sort_values()

# Créer un graphique en barres horizontales avec Plotly Express
fig = px.bar(
    mean,
    x=mean.values,
    y=mean.index,
    orientation='h',
    title='Average Age of Mothers Grouped by Education Level',
    color={
        '8th grade or less': '#3ddc97', 
        '9th through 12th grade with no diploma': '#e6c79c',
        'High school graduate or GED completed': '#D33A47', 
        'Some college credit, but not a degree': '#ffb49a',
        'Associate degree (AA, AS)': '#85C2FC',
        'Bachelor\'s degree (BA, AB, BS)': '#ff4f79',
        'Master\'s degree (MA, MS, MEng, MEd, MSW, MBA)': '#087e8b',
        'Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)': '#ff5a5f',
        'Unknown or Not Stated': '#a11692',
    },
    labels={'x': 'Average Age of Mother (years)', 'y': 'Education Level of Mother'},
    text=mean,
)

# Personnaliser la mise en page
fig.update_layout(
    xaxis_title='Average Age of Mother (years)',
    yaxis_title='Education Level of Mother',
    title_font_size=18,
    title_x=0.5,  # Centrer le titre
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',  # Fond transparent
    bargap=0.2,  # Ajuster l'espacement entre les barres
)




# Afficher le graphique
fig.show()
