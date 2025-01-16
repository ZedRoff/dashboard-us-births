from dash import html, dcc
import components
def local():
    return html.Main([
       html.Iframe(src="../assets/temp_map.html", id="map"),
       dcc.Graph(figure=components.gender.generate(), id="gender_graph")

    ], id="container_local")