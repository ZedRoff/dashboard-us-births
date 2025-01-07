from dash import html
def homepage():
    return html.Main([
            html.Div([
                html.H2("US Births from 2016 to 2021", id="subtitle_main"),
                html.P("A minimalist dashboard developed for a ESIEE course that showcase US births data", id="description_main"),
                 html.Div([

        html.Div([
            html.I(className="fa-solid fa-flag icon_stat"),
            html.H3("States", className="stat_title"),
            html.P("51", className="stat_data")

        ], className="stat_card"),

        html.Div([
            html.I(className="fa-solid fa-chart-bar icon_stat"),
            html.H3("Graphs", className="stat_title"),
            html.P("15", className="stat_data")

        ], className="stat_card"),

    ], id="stats_main")
            ], id="block_left"),
            html.Img(src="./assets/image.png", id="image_main")
    ], id="block_main"), html.Div(html.Div([
            html.H3(
                "Data source", id="source_title"
            ),
            html.P("The data in this dataset was obtained using CDC's WONDER retrieval tool on the CDC Natality page"),
            html.Div([
                html.A("Kaggle", className="source_button"),
                html.A("CSV", className="source_button")
            ], id="source_buttons")
], id="source"), id="source_section"
)
        