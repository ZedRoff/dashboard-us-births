from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd

# Charger les données depuis un fichier CSV
csv_file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin de votre fichier CSV
df = pd.read_csv(csv_file_path)

# Définir les colonnes d'intérêt
column_of_interest = "Average Age of Mother (years)"
unit = "années"  # Définir l'unité associée à la colonne

# Calculer la moyenne et le maximum pour la colonne d'intérêt
average_value = df[column_of_interest].mean()
max_value = df[column_of_interest].max()

# Préparer les données pour l'affichage
data = [
    {
        "Variable": column_of_interest,
        "Moyenne": round(average_value, 2),  # Arrondir la moyenne à 2 décimales
        "Maximum": max_value,
        "Unité": unit,
    }
]

# Convertir en DataFrame
df_display = pd.DataFrame(data)

# Fonction pour créer une carte stylisée avec un cercle de progression
def create_styled_card(title, value, max_value, unit):
    percentage = int((value / max_value) * 100)  # Calcul du pourcentage

    # Styles pour le cercle et la progression
    circle_style = {
        "width": "120px",
        "height": "120px",
        "border-radius": "50%",
        "border": "10px solid #f0f0f0",
        "position": "relative",
        "margin": "auto",
    }

    progress_style = {
        "position": "absolute",
        "top": 0,
        "left": 0,
        "width": "100%",
        "height": "100%",
        "clip-path": "circle(50% at 50% 50%)",
        "background": f"conic-gradient(#28a745 {percentage}%, #f0f0f0 {percentage}%)",
    }

    # Styles pour la carte
    card_style = {
        "background": "#ffffff",
        "border": "1px solid #ddd",
        "border-radius": "15px",
        "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
        "padding": "20px",
        "text-align": "center",
        "margin": "10px",
    }

    # Retourne la carte stylisée
    return html.Div(
        style=card_style,
        children=[
            html.H4(title, className="card-title", style={"margin-bottom": "15px", "color": "#333"}),
            html.Div(
                [
                    html.Div(style=circle_style, children=[
                        html.Div(style=progress_style),
                        html.Div(
                            f"{percentage}%",
                            style={
                                "position": "absolute",
                                "top": "50%",
                                "left": "50%",
                                "transform": "translate(-50%, -50%)",
                                "font-size": "18px",
                                "font-weight": "bold",
                                "color": "#333",
                            },
                        ),
                    ]),
                    html.P(
                        f"{value} {unit}",
                        style={
                            "margin-top": "10px",
                            "font-size": "16px",
                            "color": "#666",
                        },
                    ),
                ]
            ),
        ],
    )

# Initialiser l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Construire l'interface utilisateur
app.layout = html.Div(
    [
        html.H1("Résumé Statistique avec Progress Circles", className="text-center mt-4", style={"color": "#007bff"}),
        html.Div(
            [
                create_styled_card(
                    row["Variable"], row["Moyenne"], row["Maximum"], row["Unité"]
                )
                for _, row in df_display.iterrows()
            ],
            style={
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "center",
                "padding": "20px",
            },
        ),
    ],
    style={"background-color": "#f8f9fa", "padding-bottom": "50px"},
)

# Lancer l'application
if __name__ == "__main__":
    app.run_server(debug=True)
