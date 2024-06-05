from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "HOME", style={"color": "#0084d6",
                               "font-size": "30px",
                               'margin-left': '30px',
                               'margin-top': '15px',
                               'text-align':'center',}
            ),
        ], className='home_bg ten columns')
    ], className='home_row row'),
    dbc.Container([
        dbc.Card([
            dbc.CardBody([
                html.H1("Welcome to the Employment Dashboard", className="card-title"),
                html.P(
                    "An interactive dashboard providing comprehensive insights into "
                    "unemployment rates, labour participation rates, and employment estimates "
                    "across different areas and time periods.",
                    className="card-text",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "The statistical application is divided into several sections, each providing a unique perspective on the data:"
                ),
                html.Ul([
                    html.Li("DASHBOARD : Explore highest and lowest estimations according to areas, and rate change estimations."),
                    html.Li("REASEARCH : Delve into correlation, standard deviation, and time series analysis. Lag analysis is also available."),
                    html.Li("RESEARCH OUTCOME : View the results of our extensive research into employment trends."),
                    html.Li("DATA : Access the raw data used in our analyses, presented in a user-friendly table format."),
                    html.Li("EMPLOYMENT, UNEMPLOYMENT, LABOUR PARTICIPATION : Discover specific graphs related to each of these key indicators."),
                ]),
                #dbc.Button("Learn more", color="primary"),
            ])
        ], className="mt-4"),
    ])
])
