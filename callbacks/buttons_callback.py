from dash import Output, Input, callback_context, html
from views import demography, economy, education, environment, language

def register(app):
    @app.callback(
    Output("content", "children"),
    [Input("one", "n_clicks"), Input("two", "n_clicks"), Input("three", "n_clicks"), Input("four", "n_clicks"), Input("five", "n_clicks")],
    prevent_initial_call=True
)
    def update_content(one_clicks, two_clicks, three_clicks, four_clicks, five_clicks):
        ctx = callback_context
        if not ctx.triggered:
            return html.P("No button clicked")
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        content_map = {
        "one": demography.show,
        "two": economy.show,
        "three": education.show,
        "four": environment.show,
        "five": language.show
        }
        return content_map.get(button_id, lambda: html.P("Invalid button"))()
    