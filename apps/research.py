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
from statistical_graphs import research_graphs as rg

styles = {
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'font-family': 'Arial, sans-serif',
    'font-size': '16px',
    'line-height': '1.5',
    'margin': '20px',
    'padding': '10px',
    'border': '1px solid #eee',
    'border-radius': '5px',
    'background': '#fafafa',
}

fig_overall, fig_rural, fig_urban, interpretation = rg.lab_corr_graphs()
fig_overall_std,fig_rural_std,fig_urban_std, interpretation_std = rg.std_deviation_graphs_overall()
fig_std_unemp_overall, fig_std_unemp_rural,fig_std_unemp_urban,interpretation_std  = rg.std_deviation_graphs_unemployment()
fig_std_employ_overall, fig_std_rural_overall, fig_std_employ_urban, final_interpretation = rg.std_deviation_graphs_employ()
tsa_overall,tsa_rural,tsa_urban,original_series_description,trend_description,seasonality_description,residuals_description = rg.time_series_analysis_graphs()
fig_lag_overall,fig_lag_rural,fig_lag_urban = rg.lag_analysis_graph()

layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "RESEARCH", style={"color": "#0084d6",
                                              "font-size": "30px",
                                              'margin-left': '30px',
                                              'margin-top': '15px',
                                              'text-align':'center',}
            ),
        ], className='home_bg ten columns')
    ], className='home_row row'),
    html.P(
                ' CORELATION BETWEEN ESTIMATED LABOUR PARTICIPATION RATE AND ESTIMATED UNEMPLOYMENT RATE', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_overall),),
                          dbc.Col(dcc.Graph(figure=fig_rural),),
                          dbc.Col(dcc.Graph(figure=fig_urban), ),
                      ],style={'margin-left': '70px'}),
                    ]),

            html.P(
                ' STANDARD DEVIATIONS ', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_overall_std),),
                          dbc.Col(dcc.Graph(figure=fig_rural_std),),
                          dbc.Col(dcc.Graph(figure=fig_urban_std), ),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_std_unemp_overall),),
                          dbc.Col(dcc.Graph(figure=fig_std_unemp_rural),),
                          dbc.Col(dcc.Graph(figure=fig_std_unemp_urban), ),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_std_employ_overall),),
                          dbc.Col(dcc.Graph(figure=fig_std_rural_overall),),
                          dbc.Col(dcc.Graph(figure=fig_std_employ_urban), ),
                      ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                ' TIME SERIES ANALYSIS ', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            dbc.Row([
                dcc.Markdown(
                    children=' ANALYSIS ON OVERALL DATA',
                    style=styles
                ),
            ]),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_overall[0]),),
                          dbc.Col(dcc.Graph(figure=tsa_overall[1]),),
                          dbc.Col(dcc.Graph(figure=tsa_overall[2]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_overall[3]), ),
                          dbc.Col(dcc.Graph(figure=tsa_overall[4]),),
                          dbc.Col(dcc.Graph(figure=tsa_overall[5]),),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_overall[6]), ),
                          dbc.Col(dcc.Graph(figure=tsa_overall[7]), ),
                          dbc.Col(dcc.Graph(figure=tsa_overall[8]),),
                      ],style={'margin-left': '70px'}),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_overall[9]),),
                          dbc.Col(dcc.Graph(figure=tsa_overall[10]),),
                          dbc.Col(dcc.Graph(figure=tsa_overall[11]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
            dbc.Row([
                dcc.Markdown(
                    children=' ANALYSIS ON RURAL AREAS',
                    style=styles
                ),
            ]),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_rural[0]),),
                          dbc.Col(dcc.Graph(figure=tsa_rural[1]),),
                          dbc.Col(dcc.Graph(figure=tsa_rural[2]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_rural[3]), ),
                          dbc.Col(dcc.Graph(figure=tsa_rural[4]),),
                          dbc.Col(dcc.Graph(figure=tsa_rural[5]),),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_rural[6]), ),
                          dbc.Col(dcc.Graph(figure=tsa_rural[7]), ),
                          dbc.Col(dcc.Graph(figure=tsa_rural[8]),),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_rural[9]),),
                          dbc.Col(dcc.Graph(figure=tsa_rural[10]),),
                          dbc.Col(dcc.Graph(figure=tsa_rural[11]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
            dbc.Row([
                dcc.Markdown(
                    children=' ANALYSIS ON URBAN AREAS',
                    style=styles
                ),
            ]),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_urban[0]),),
                          dbc.Col(dcc.Graph(figure=tsa_urban[1]),),
                          dbc.Col(dcc.Graph(figure=tsa_urban[2]), ),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_urban[3]), ),
                          dbc.Col(dcc.Graph(figure=tsa_urban[4]),),
                          dbc.Col(dcc.Graph(figure=tsa_urban[5]),),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_urban[6]), ),
                          dbc.Col(dcc.Graph(figure=tsa_urban[7]), ),
                          dbc.Col(dcc.Graph(figure=tsa_urban[8]),),
                      ],style={'margin-left': '70px'}),
                    ]),
                    html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=tsa_urban[9]),),
                          dbc.Col(dcc.Graph(figure=tsa_urban[10]),),
                          dbc.Col(dcc.Graph(figure=tsa_urban[11]), ),
                      ],style={'margin-left': '70px'}),
                    ]),

            dbc.Row([
                dcc.Markdown(
                    children=' LAG ANALYSIS OVERALL, RURAL AREAS AND URBAN AREAS',
                    style=styles
                ),
            ]),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_lag_overall),),
                        ],style={'margin-left': '150px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_lag_rural), ),
                      ],style={'margin-left': '150px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_lag_urban), ),
                      ],style={'margin-left': '150px'}),
                    ]),
            ]),
])