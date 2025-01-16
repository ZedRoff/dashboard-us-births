from dash import html, dcc
import components.US_map as US_map
def local():
    return html.Main([
      dcc.Graph(id="test", figure=US_map.create_plotly_map(2020))

    ], id="container_local")