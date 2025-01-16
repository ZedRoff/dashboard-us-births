from dash import html, dcc
import components.educationGenderGlob as educationGenderGlob
import components.educationGlob as educationGlob
import components.legendCode as legendCode

def show():
    return html.Div([
        dcc.Graph(id="test", figure=educationGenderGlob.generate()),
        dcc.Graph(id="test3", figure=legendCode.generate()),
        dcc.Graph(id="test2", figure=educationGlob.generate())
    ])