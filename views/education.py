from dash import html, dcc
import components.educationGenderGlob as educationGenderGlob


def show():
    return html.Div([
        dcc.Graph(id="test", figure=educationGenderGlob.generate())
    ])