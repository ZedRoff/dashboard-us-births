import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Charger les données
file_path = 'us_births_2016_2021.csv'
df = pd.read_csv(file_path)

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Créer une liste d'états pour le menu déroulant
states = df['State'].unique()

# Créer la mise en page de l'application
app.layout = html.Div([
    html.H1('Nombre de Naissances par Année pour un État'),
    
    # Menu déroulant pour sélectionner un état
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in states],
        value=states[0],  # valeur initiale sélectionnée
        style={'width': '50%'}
    ),
    
    # Graphique pour afficher l'histogramme
    dcc.Graph(id='births-histogram')
])

# Callback pour mettre à jour l'histogramme en fonction de l'état sélectionné
@app.callback(
    Output('births-histogram', 'figure'),
    Input('state-dropdown', 'value')
)
def update_histogram(selected_state):
    # Filtrer les données pour l'état sélectionné
    df_state = df[df['State'] == selected_state]
    
    # Agréger le nombre de naissances par année pour l'état sélectionné
    births_by_year = df_state.groupby('Year')['Number of Births'].sum()
    
    # Créer un histogramme avec Plotly
    fig = px.bar(
        births_by_year,
        x=births_by_year.index,
        y=births_by_year.values,
        labels={'x': 'Année', 'y': 'Nombre de naissances'},
        title=f'Nombre de naissances par année - {selected_state}',
        color=births_by_year.index.astype(str),  # Couleur par année
        color_discrete_sequence=px.colors.qualitative.Set2  # Choisir une palette de couleurs
    )
    
    return fig

# Exécuter l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
