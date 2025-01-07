from dash import html, dcc
import components
import components.gender
def local():
    return html.Main([
       html.Iframe(src="../assets/temp_map.html", id="map"),
       dcc.Graph(figure=components.gender.generate(), id="")

    ], id="container_local")