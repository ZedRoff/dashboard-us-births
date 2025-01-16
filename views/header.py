from dash import html
def header(page):
    dic = {"home": "Accueil", "local": "Donnéees Locales", "global": "Données Globales"}
    return html.Header([
        html.A([
            html.I(className="fa-solid fa-map-marker-alt"),
            html.H1("US Births", id="title_main"),
            
     ], className="element_header", href="#"),
     html.Div([
        html.A("Home", className=("nav_item nav_item_active" if page == "home" else "nav_item"), id="home"),
        html.A("Local Data", className=("nav_item nav_item_active" if page == "local" else "nav_item"), id="local"),
        html.A("Global Data", className=("nav_item nav_item_active" if page == "global" else "nav_item"), id="global"),
 html.I(className="fa-solid fa-moon", id="theme_switch")
     ], id="navbar")
], className="header_main")
