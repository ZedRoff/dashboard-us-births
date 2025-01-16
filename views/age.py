from dash import html, dcc
import components.ageGlob as ageGlob
import components.motherAge as motherAge

def show():
    return html.Div([
        dcc.Graph(id="test", figure=ageGlob.generate()),
        dcc.Graph(id="test3", figure=motherAge.generate())
    ])