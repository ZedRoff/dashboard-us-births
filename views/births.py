from dash import html, dcc
import components.US_map as US_map
def show():
    return html.Div([
        dcc.Graph(id="test", figure=US_map.create_plotly_map(2020))
    ])