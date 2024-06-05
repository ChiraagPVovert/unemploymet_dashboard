from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from google.oauth2 import service_account
import pandas_gbq as pd1
import csv

from statistical_graphs import employment_rural_area_wise as eraw, employment_total as et, employment_urban_area_wise as euaw, employment_statewise_and_region_wise_year_2020 as esrwy

fig_year_estimated_employment_rate_overall = et.year_estimated_employed_overall()
fig_year_monthly_estimated_employment_rate_overall = et.year_monthly_estimated_employed_overall()
fig_estimated_employment_rate_in_overall_area_weekly_basis = et.estimated_employed_in_overall_area_weekly_basis()

fig_year_estimated_employment_rate_rural = eraw.year_estimated_employed_rural()
fig_year_monthly_estimated_employment_rate_rural = eraw.year_monthly_estimated_employed_rural()
fig_estimated_employment_rate_in_rural_area_weekly_basis = eraw.estimated_employed_in_rural_area_weekly_basis()

fig_year_estimated_employment_rate_urban = euaw.year_estimated_employed_rate_urban()
fig_year_monthly_estimated_employment_rate_urban = euaw.year_monthly_estimated_employed_urban()
fig_estimated_employment_rate_in_urban_area_weekly_basis = euaw.estimated_employed_in_urban_area_weekly_basis()

fig_monthly_estimated_employment_rate = esrwy.monthly_estimated_employed()
fig_statewise_average_employment_rate = esrwy.statewise_average_employed()
fig_statewise_monthly_average_employment_rate = esrwy.statewise_monthly_average_employed()
fig_regionwise_monthly_average_employment_rate = esrwy.regionwise_monthly_average_employed()
fig_regionwise_average_employment_rate = esrwy.regionwise_average_employed()
fig_map_statewise_monthly_average_employment_rate = esrwy.map_statewise_monthly_average_employed()



layout = html.Div([
            html.Div([
                html.Div([
                    html.P(
                        "EMPLOYMENT IN INDIA", style={"color": "#0084d6",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
                    ),
                ], className='home_bg ten columns')
            ], className='home_row row'),
            html.P(
                'STATISTICAL ESTIMATES OF EMPLOYMENT RATE IN INDIA', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_employment_rate_overall),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_employment_rate_overall),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_employment_rate_in_overall_area_weekly_basis)),
                            ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF EMPLOYMENT RATE IN RURAL AREAS IN INDIA', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_employment_rate_rural),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_employment_rate_rural),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_employment_rate_in_rural_area_weekly_basis),),
                            ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF EMPLOYMENT RATE URBAN AREAS IN INDIA', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_employment_rate_urban),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_employment_rate_urban),),
                        dbc.Col(dcc.Graph(figure=fig_estimated_employment_rate_in_urban_area_weekly_basis), ),
                             ],style={'margin-left': '70px'}),
                            ]),
            html.P(
                'STATISTICAL ESTIMATES OF EMPLOYMENT RATE IN INDIA - STATE WISE AND REGION WISE - 2020', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([

                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_monthly_estimated_employment_rate),),
                          dbc.Col(dcc.Graph(figure=fig_statewise_average_employment_rate),),
                          ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_statewise_monthly_average_employment_rate),),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_regionwise_monthly_average_employment_rate),),
                          dbc.Col(dcc.Graph(figure=fig_regionwise_average_employment_rate),),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_map_statewise_monthly_average_employment_rate),),
                      ])
                    ]),

])