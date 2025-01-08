from dash import html
def glob():
  
    return html.Main([
       html.Div([
            html.Div([
               sidebar_element("Statistiques globales"),
               sidebar_element("Test 2"),
               sidebar_element("Test 3")
            ], id="elements_sidebar")

       ], id="sidebar"), 
       html.Div([
           html.Div([
               
                  html.Div([
                      
                       html.H2("Births"),
                    
                           html.Div([
                       
                      html.H3("Most births year", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P("2021", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("Value", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P("95000 births", className="stat_data")
                        
                      ], className="data_splitter")
                           ], className="section"),
                           
                  ], className="stat_global"),
                   html.Div([
                      
                       html.H2("Weights"),
                    
                           html.Div([
                       
                      html.H3("Most weighted child", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P("5kg", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("State", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P("California", className="stat_data")
                        
                      ], className="data_splitter")
                           ], className="section"),
                           
                  ], className="stat_global"),
                   html.Div([
                      
                       html.H2("Mothers"),
                    html.Div([

                   
                           html.Div([
                       
                      html.H3("Most young", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P("15 years old", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("State", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P("Texas", className="stat_data")
                        
                      ], className="data_splitter")
                           ], className="section"),
                           html.Div(id="bar"),
                              
                               html.Div([
                       
                      html.H3("Most young", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P("15 years old", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("State", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P("Texas", className="stat_data")
                        
                      ], className="data_splitter")
                           ], className="section")
                            ], id="special_stat_global")
                  ], className="stat_global")
                
              ], id="stats_global")


       ], id="main_global")
    ], id="container_global")


def sidebar_element(title):
    return  html.Div([

                    html.P(title, className="element_sidebar_title"),
                    html.I(className="fa-chevron-right fa-solid")
                ], className="element_sidebar")