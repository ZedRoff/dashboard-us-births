from dash import html, dcc
import components.ageGlob as ageGlob
import components.motherAgeGlob as motherAgeGlob

def show():
    return html.Div([
        dcc.Graph(id="test", figure=ageGlob.generate()),
        dcc.Graph(id="test3", figure=motherAgeGlob.generate())
    ])