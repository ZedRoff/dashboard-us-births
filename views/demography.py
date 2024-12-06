
from dash import dcc
import components.demography as demography
import components.fertility as fertility
def show():
    return [
            dcc.Graph(id="demography", figure=demography.create_graph()),
            dcc.Graph(id="fertility", figure=fertility.create_graph())
        ]