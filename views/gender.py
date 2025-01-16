from dash import html, dcc
import components.genderGlob as genderGlob 

def show():
    return html.Div([
        dcc.Graph(id="test", figure=genderGlob.generate())
    ])