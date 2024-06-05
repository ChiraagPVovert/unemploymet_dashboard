from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from google.oauth2 import service_account
import pandas_gbq as pd1
import csv

from statistical_graphs import labour_participation_rural_area_wise as lpr, labour_participation_total as lt, labour_participation_urban_area_wise as lpuaw, labour_participation_statewise_and_region_wise_year_2020 as lpsrwy

fig_year_estimated_labour_participation_overall = lt.year_estimated_labour_participation_overall()
fig_year_monthly_estimated_labour_participation_overall = lt.year_monthly_estimated_labour_participation_overall()
fig_estimated_labour_participation_in_overall_area_weekly_basis = lt.estimated_labour_participation_in_overall_area_weekly_basis()

fig_year_estimated_labour_participation_rate_rural = lpr.year_estimated_labour_participation_rate_rural()
fig_year_monthly_estimated_average_labour_participation_rate_rural = lpr.year_monthly_estimated_average_labour_participation_rate_rural()
fig_estimated_labour_participation_rate_in_rural_area_weekly_basis = lpr.estimated_labour_participation_rate_in_rural_area_weekly_basis()

fig_year_estimated_labour_participation_rate_urban = lpuaw.year_estimated_labour_participation_rate_urban()
fig_year_monthly_labour_participation_rate_urban = lpuaw.year_monthly_labour_participation_rate_urban()
fig_estimated_labour_participation_in_urban_area_weekly_basis = lpuaw.estimated_labour_participation_in_urban_area_weekly_basis()

fig_monthly_labour_participation = lpsrwy.monthly_labour_participation()
fig_statewise_average_labour_participation_rate = lpsrwy.statewise_average_labour_participation_rate()
fig_statewise_monthly_average_labour_participation_rate = lpsrwy.statewise_monthly_average_labour_participation_rate()
fig_regionwise_monthly_average_labour_participation_rate = lpsrwy.regionwise_monthly_average_labour_participation_rate()
fig_regionwise_average_labour_participation_rate_estimate = lpsrwy.regionwise_average_labour_participation_rate_estimate()
fig_map_statewise_monthly_average_labour_participation_rate_estimate = lpsrwy.map_statewise_monthly_average_labour_participation_rate_estimate()



layout = html.Div([
            html.Div([
                html.Div([
                    html.P(
                        "LABOUR PARTICIPATION RATE IN INDIA", style={"color": "#0084d6",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
                    ),
                ], className='home_bg ten columns')
            ], className='home_row row'),
            html.P(
                'STATISTICAL ESTIMATES OF LABOUR PARTICIPATION RATE IN INDIA', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_labour_participation_overall),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_labour_participation_overall),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_labour_participation_in_overall_area_weekly_basis)),
                            ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF LABOUR PARTICIPATION RATE IN RURAL AREAS IN INDIA', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_labour_participation_rate_rural),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_average_labour_participation_rate_rural),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_labour_participation_rate_in_rural_area_weekly_basis),),
                            ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF LABOUR PARTICIPATION RATE URBAN AREAS IN INDIA', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_labour_participation_rate_urban),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_labour_participation_rate_urban),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_labour_participation_in_urban_area_weekly_basis), ),
                             ],style={'margin-left': '70px'}),
                            ]),
            html.P(
                'STATISTICAL ESTIMATES OF LABOUR PARTICIPATION RATE IN INDIA - STATE WISE AND REGION WISE - 2020', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([

                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_monthly_labour_participation),),
                          dbc.Col(dcc.Graph(figure=fig_statewise_average_labour_participation_rate),),
                          ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_statewise_monthly_average_labour_participation_rate),),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_regionwise_monthly_average_labour_participation_rate),),
                          dbc.Col(dcc.Graph(figure=fig_regionwise_average_labour_participation_rate_estimate),),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_map_statewise_monthly_average_labour_participation_rate_estimate),),
                      ])
                    ]),

])