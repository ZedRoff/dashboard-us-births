from dash import html
def glob():
  
    return html.Main([
        html.Iframe(src="../assets/temp_map.html", id="map")
    ])