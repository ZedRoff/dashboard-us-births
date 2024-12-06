from dash import html

def create_sidebar():
    return html.Aside([
                html.I(className="fa-solid fa-people-group", id="one"),
                html.I(className="fa-solid fa-coins", id="two"),
                html.I(className="fa-solid fa-graduation-cap", id="three"),
                html.I(className="fa-solid fa-leaf", id="four"),
                html.I(className="fa-solid fa-language", id="five")
            ],className="Nav")