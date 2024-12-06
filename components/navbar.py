from dash import html

def create_navbar():
    return html.Header([
            html.Div("France"),
            html.Div("Dashboard World Data 2023"),
            html.Button([
                html.I(className = "fa-solid fa-map-marker-alt")
            ], id="bouton")
        ])