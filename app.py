import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ClientsideFunction

import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server
app.config.suppress_callback_exceptions = True

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()



def generate_table_row(id, style, col1, col2, col3):
    """ Generate table rows.

    :param id: The ID of table row.
    :param style: Css style of this row.
    :param col1 (dict): Defining id and children for the first column.
    :param col2 (dict): Defining id and children for the second column.
    :param col3 (dict): Defining id and children for the third column.
    """

    return html.Div(
        id=id,
        className="row table-row",
        style=style,
        children=[
            html.Div(
                id=col1["id"],
                style={"display": "table", "height": "100%"},
                className="two columns row-department",
                children=col1["children"],
            ),
            html.Div(
                id=col2["id"],
                style={"textAlign": "center", "height": "100%"},
                className="five columns",
                children=col2["children"],
            ),
            html.Div(
                id=col3["id"],
                style={"textAlign": "center", "height": "100%"},
                className="five columns",
                children=col3["children"],
            ),
        ],
    )

app.layout = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("logo.png"))],
        ),
        
        html.Div(
            id="main-column",
            className="tweleve columns",
            children=[
                
                html.Div(
                    id="patient_volume_card",
                    children=[
                        html.B("Jobs Analysis"),
                        html.Hr(),
                        dcc.Graph(id="patient_volume_hm"),
                    ],
                ),
                
                html.Div(
                    id="wait_time_card",
                    children=[
                        html.B("Graphs"),
                        html.Hr(),
                        html.Div(id="wait_time_table", children=[]),
                    ],
                ),
            ],
        ),
    ],
)

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
