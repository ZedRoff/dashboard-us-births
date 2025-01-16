from dash import html, dcc
import components.weightGlob as weightGlob
def show():
    return html.Div([
        dcc.Graph(id="test", figure=weightGlob.generate())
    ])