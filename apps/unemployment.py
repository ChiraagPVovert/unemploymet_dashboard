from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from google.oauth2 import service_account
import pandas_gbq as pd1
import csv

from statistical_graphs import unemployment_rural_area_wise as uraw, unemployment_total as ut, unemployment_urban_area_wise as uuaw, unemployment_statewise_and_region_wise_year_2020 as usrwy

fig_year_estimated_unemployment_rate_overall = ut.year_estimated_unemployment_rate_overall()
fig_year_monthly_estimated_unemployment_rate_overall = ut.year_monthly_estimated_unemployment_rate_overall()
fig_estimated_unemployment_rate_in_overall_area_weekly_basis = ut.estimated_unemployment_rate_in_overall_area_weekly_basis()

fig_year_estimated_unemployment_rate_rural = uraw.year_estimated_unemployment_rate_rural()
fig_year_monthly_estimated_unemployment_rate_rural = uraw.year_monthly_estimated_unemployment_rate_rural()
fig_estimated_unemployment_rate_in_rural_area_weekly_basis = uraw.estimated_unemployment_rate_in_rural_area_weekly_basis()

fig_year_estimated_unemployment_rate_urban = uuaw.year_estimated_unemployment_rate_urban()
fig_year_monthly_estimated_unemployment_rate_urban = uuaw.year_monthly_estimated_unemployment_rate_urban()
fig_estimated_unemployment_rate_in_urban_area_weekly_basis = uuaw.estimated_unemployment_rate_in_urban_area_weekly_basis()

fig_monthly_estimated_unemployment_rate = usrwy.monthly_estimated_unemployment_rate()
fig_statewise_average_unemployment_rate = usrwy.statewise_average_unemployment_rate()
fig_statewise_monthly_average_unemployment_rate = usrwy.statewise_monthly_average_unemployment_rate()
fig_regionwise_monthly_average_unemployment_rate = usrwy.regionwise_monthly_average_unemployment_rate()
fig_regionwise_average_unemployment_rate = usrwy.regionwise_average_unemployment_rate()
fig_map_statewise_monthly_average_unemployment_rate = usrwy.map_statewise_monthly_average_unemployment_rate()



layout = html.Div([
            html.Div([
                html.Div([
                    html.P(
                        "UNEMPLOYMENT IN INDIA", style={"color": "#0084d6",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
                    ),
                ], className='home_bg ten columns')
            ], className='home_row row'),
            html.P(
                'STATISTICAL ESTIMATES OF UNEMPLOYMENT RATE IN INDIA', style={"color": "white",
                                                      "font-size": "30px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_unemployment_rate_overall),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_unemployment_rate_overall),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_unemployment_rate_in_overall_area_weekly_basis)),
                      ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF UNEMPLOYMENT RATE IN RURAL AREAS IN INDIA', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_unemployment_rate_rural),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_unemployment_rate_rural),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_unemployment_rate_in_rural_area_weekly_basis),),
                        ],style={'margin-left': '70px'}),

                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF UNEMPLOYMENT RATE URBAN AREAS IN INDIA', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_year_estimated_unemployment_rate_urban),),
                          dbc.Col(dcc.Graph(figure=fig_year_monthly_estimated_unemployment_rate_urban),),
                          dbc.Col(dcc.Graph(figure=fig_estimated_unemployment_rate_in_urban_area_weekly_basis),),
                        ],style={'margin-left': '70px'}),
                    ]),
            html.P(
                'STATISTICAL ESTIMATES OF UNEMPLOYMENT RATE IN INDIA - STATE WISE AND REGION WISE - 2020', style={"color": "white",
                                                      "font-size": "25px",
                                                      'margin-left': '30px',
                                                      'margin-top': '15px',
                                                      'text-align':'center',}
            ),
            html.Div([

                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_monthly_estimated_unemployment_rate),),
                          dbc.Col(dcc.Graph(figure=fig_statewise_average_unemployment_rate),),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_statewise_monthly_average_unemployment_rate),),
                      ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_regionwise_monthly_average_unemployment_rate),),
                          dbc.Col(dcc.Graph(figure=fig_regionwise_average_unemployment_rate),),
                          ],style={'margin-left': '70px'}),
                      dbc.Row([
                          dbc.Col(dcc.Graph(figure=fig_map_statewise_monthly_average_unemployment_rate),),
                      ])
                    ]),

])