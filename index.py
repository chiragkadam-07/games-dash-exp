# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px

# Connect to main app.py file\

from app import app
from app import server

# Connect to your app pages
from apps import vgames, global_sales


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Video Games|', href='/apps/vgames'),
        dcc.Link('Other Products', href='/apps/global_sales'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/vgames':
        return vgames.layout
    if pathname == '/apps/global_sales':
        return global_sales.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
