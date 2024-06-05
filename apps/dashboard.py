from dash import html
from dash import dcc
import csv
import datetime
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import seaborn as sns
import plotly.graph_objects as go
from statistical_graphs import dashboard_graphs as dg

highest_rate_graphs = dg.max_emp_unemp_lab_graph()
lowest_rate_graphs = dg.min_emp_unemp_lab_graph()
highest_rate_changes_graphs = dg.highest_rate_change_graph()
lowest_rate_changes_graphs = dg.lowest_rate_change_graph()

layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "DASHBOARD", style={"color": "#0084d6",
                                              "font-size": "30px",
                                              'margin-left': '30px',
                                              'margin-top': '15px',
                                              'text-align':'center',}
            ),
        ], className='home_bg ten columns')
    ], className='home_row row'),
    html.P(
                ' HIGHEST ESTIMATIONS ACCORDING TO AREAS', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[0]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[1]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[2]),),
                      ],style={'margin-left': '70px',}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[3]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[4]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[5]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[6]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[7]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_graphs[8]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                ' LOWEST ESTIMATIONS ACCORDING TO AREAS', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[0]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[1]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[2]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[3]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[4]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[5]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[6]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[7]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_graphs[8]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                ' HIGHEST RATE CHANGE ESTIMATIONS ACCORDING TO AREAS', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[0]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[1]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[2]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[3]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[4]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[5]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[6]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[7]),),
                          dbc.Col(dcc.Graph(figure=highest_rate_changes_graphs[8]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                ' LOWEST RATE CHANGE ESTIMATIONS ACCORDING TO AREAS', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[0]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[1]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[2]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[3]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[4]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[5]), ),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[6]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs[7]),),
                          dbc.Col(dcc.Graph(figure=lowest_rate_changes_graphs [8]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
])
