from dash import html
from dash import dcc
import components.languageHisto as languageHisto
import components.worldCloud as worldCloud
import components.languageMap as languageMap


def show():
    return [
        html.Img(
            id="worldCloud",
            src=worldCloud.create_graph(),
        ),
        dcc.Graph(id="languageHisto", figure=languageHisto.create_graph()),
        dcc.Graph(id="languageMap", figure=languageMap.create_graph()),

    ]
