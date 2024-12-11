from dash import Output, Input, html

def register(app):
    @app.callback(
    Output("location-store", "data"),
    Input("change-location", "n_clicks"),
    prevent_initial_call=True
    )
    def change_location(n_clicks):
        return "Germany"
    @app.callback(
    Output("testa", "children"),
    Input("location-store", "data")
    )
    def display_location(location):
        return html.P(location)

    