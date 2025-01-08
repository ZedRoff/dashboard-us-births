from dash import html
def glob():
  
    return html.Main([
       html.Div([
           

       ], id="sidebar"), 
       html.Div([
           html.Div([
               html.H2("Stats globales"),
              html.Div([
                  
                  html.Div([
                      html.H3("POURCENTAGE NATALITE", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-home"),
                          html.P("38%", className="stat_data")

                      ], className="data_splitter")
                  ], className="stat_global")

              ], id="stats_global")

           ], id="section")

       ], id="main_global")
    ], id="container_global")