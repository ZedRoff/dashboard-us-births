import pandas as pd
import plotly.express as px

# Charger le fichier CSV
df = pd.read_csv('data/us_births_2016_2021.csv')

def generate(selected_state):
    # Filtrer les données pour l'état sélectionné
    df_state = df[df['State'] == selected_state]

    # Définir les intervalles pour l'âge moyen des mères
    age_intervals = pd.cut(df_state['Average Age of Mother (years)'], bins=range(22, 38, 2))
    
    # Calculer le nombre de mères dans chaque tranche d'âge
    age_counts = df_state.groupby(age_intervals, observed=False)['Number of Births'].sum()

    # Créer un histogramme avec Plotly
    fig = px.bar(
        x=age_counts.index.astype(str),  # Tranches d'âge
        y=age_counts.values,  # Nombre de mères dans chaque tranche
        labels={'x': "Age range of mothers", 'y': "Number of births"},
        title=f"Breakdown of mothers' average age : in {selected_state}",
        text=age_counts.values,  # Ajouter le nombre sur les barres
        color_discrete_sequence=['#0A3161']  # Couleur personnalisée pour les barres
    )

    # Personnaliser la mise en page
    fig.update_layout(
        xaxis_title="Age range of mothers (in years)",
        yaxis_title="Number of Births",
        title_font_size=20,
        plot_bgcolor='#FFFFFF',
        font=dict(size=14),
        xaxis=dict(
            showline=True,
            linecolor='black',
            linewidth=2,
        ),
        yaxis=dict(
            showline=True,
            linecolor='black',
            linewidth=2,
            showgrid=True,
            gridcolor='lightgrey',
            gridwidth=1,
            ticks="outside",
            griddash='dash',
            tickwidth=2,
            tickcolor='black'
        )
    )

    # Ajouter des bordures aux barres
    fig.update_traces(
        marker_line_color='black',
        marker_line_width=1.5
    )

    # Afficher le graphique
    return fig


