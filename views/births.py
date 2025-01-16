from dash import html, dcc
import components.US_map as US_map
import components.tendanceGlob as tendanceGlob
def show():
    return html.Div([
        dcc.Graph(id="test", figure=US_map.create_plotly_map(2020)),
        dcc.Graph(id="test1", figure=tendanceGlob.generate())
    ])