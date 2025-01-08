from dash import html
import pandas as pd

df = pd.read_csv('data/us_births_2016_2021.csv')

max_weight_row = df.loc[df['Average Birth Weight (g)'].idxmax()]  # Ligne avec le poids max
max_weight = df['Average Birth Weight (g)'].max()
state = max_weight_row['State']

total_births_by_year = df.groupby('Year')['Number of Births'].sum()
# Trouver l'année avec le plus grand total de naissances
max_births_year = total_births_by_year.idxmax()  # Année
max_births_value = total_births_by_year.max()    # Nombre total de naissances

# Trouver l'âge moyen des mères le plus élevé et l'état associé
max_age_row = df.loc[df['Average Age of Mother (years)'].idxmax()]  # Ligne avec l'âge maximum
max_age = max_age_row['Average Age of Mother (years)']
state_with_max_age = max_age_row['State']

# Trouver l'âge moyen des mères le plus bas et l'état associé
min_age_row = df.loc[df['Average Age of Mother (years)'].idxmin()]  # Ligne avec l'âge minimum
min_age = min_age_row['Average Age of Mother (years)']
state_with_min_age = min_age_row['State']



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
                       #html.H2("Births"),
                    
                           html.Div([
                       
                      html.H3("Year with Most Births", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P(f"{max_births_year}", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("Value", className="stat_global_title"),
                      html.Div([
                            html.I(className=f"fa-solid fa-birthday"),
                          html.P(f"{max_births_value} births", className="stat_data")                       
                      ], className="data_splitter")
                           ], className="section"),
                           
                  ], className="stat_global"),

                   html.Div([
                      
                       #html.H2("Average Birth Weight"),
                    
                           html.Div([
                       
                      html.H3("Highest Recorded Average Birth Weight", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P(f"{max_weight} kg", className="stat_data")
                         
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("State", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P(f"{state}", className="stat_data")
                        
                      ], className="data_splitter")
                           ], className="section"),
                           
                  ], className="stat_global"),
                   html.Div([
                      
                       html.H2("Maternal Age Overview"),
                    html.Div([

                   
                           html.Div([
                       
                      html.H3("Highest Average Age of Mother", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P(f"{max_age}", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("State", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P(f"{state_with_max_age}", className="stat_data")
                        
                      ], className="data_splitter")
                           ], className="section"),
                           html.Div(id="bar"),
                              
                               html.Div([
                       
                      html.H3("Lowest Average Age of Mother", className="stat_global_title"),
                      html.Div([
                          html.I(className="fa-solid fa-birthday"),
                          html.P(f"{min_age}", className="stat_data")
                        
                      ], className="data_splitter"),
                      html.Hr(),
                      html.H3("State", className="stat_global_title"),
                      html.Div([
                          html.I(className=f"fa-solid fa-birthday"),
                          html.P(f"{state_with_min_age}", className="stat_data")
                        
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