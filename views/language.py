from dash import html
import components.worldCloud as worldCloud

def show():
    return [
        html.Img(
            id="worldCloud",
            src=worldCloud.create_graph(),
        ),
    ]
