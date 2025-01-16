import pandas as pd
import plotly.express as px

def generate(selected_state):
    # Charger les données
    file_path = 'data/us_births_2016_2021.csv'
    df = pd.read_csv(file_path)

    # Créer une nouvelle colonne pondérée (poids multiplié par le nombre de naissances)
    df['Weighted Birth Weight'] = df['Average Birth Weight (g)'] * df['Number of Births']

    # Filtrer les données pour un état spécifique
   
    df_state = df[df['State'] == selected_state]

    # Créer un histogramme pondéré avec Plotly
    fig = px.histogram(
        df_state,
        x='Average Birth Weight (g)',
        y='Weighted Birth Weight',  # Utiliser les poids pondérés pour l'axe Y
        color='Gender',
        title=f'Weighted Distribution of Average Birth Weight by Gender in {selected_state}',
        labels={
            'Average Birth Weight (g)': 'Average weight of birth (g)',
            'Weighted Birth Weight': 'Weighted Total Birth Weight (g)'
        },
        nbins=30,
        color_discrete_sequence=['#B31942', '#0A3161'],
        text_auto=True
    )

    # Personnaliser la mise en page
    fig.update_layout(
        xaxis_title='Average weight of birth (g)',
        yaxis_title='Weighted Total Birth Weight (g)',
        title_font_size=20,
        plot_bgcolor='#FFFFFF',
        font=dict(size=14),
        showlegend=False,
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


    # Ajouter une bordure aux barres
    fig.update_traces(
        marker_line_color='black',
        marker_line_width=1.5
    )

    # Afficher le graphique
    return fig
