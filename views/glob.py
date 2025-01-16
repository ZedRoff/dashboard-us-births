from dash import html
import pandas as pd
import views.globalStats as globalStats
df = pd.read_csv('data/us_births_2016_2021.csv')


def glob():
  
    return html.Main([
       html.Div([
            html.Div([
               sidebar_element("Statistiques globales"),
               sidebar_element("Education"),
               sidebar_element("Test 3")
            ], id="elements_sidebar")

       ], id="sidebar"), 
       html.Div([
           globalStats.show()
       ], id="main_global")
    ], id="container_global")



def sidebar_element(title):
    return  html.Div([

                    html.P(title, className="element_sidebar_title"),
                    html.I(className="fa-chevron-right fa-solid")
                ], className="element_sidebar", id=title)