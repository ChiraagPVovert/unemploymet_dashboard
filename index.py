from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
#from google.oauth2 import service_account
#import pandas_gbq as pd1
import csv

# Connect to main app.py file
from app import app
from app import server

# Connect to your pages
from apps import home, dashboard, unemployment, employment, labour, data, research_outcome, research


app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content', children=[]),

    html.Div(
        [
            html.Div([
                html.Div([
                    #html.Img(src="https://www.overtideasandsolutions.in/img/overt-logo.png", style={"width": "50rem"}),
                   html.Img(src="/assets/overt_ideas_logo.png", style={"width": "350px"}),
                ], className='image_title')
            ], className="sidebar-header", style={'backgroundColor': '#3D3C3A'}),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-house"),
                        html.Span("HOME", style={'margin-left': '15px'})], className='icon_title')],
                        href="/",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        #html.I(className="fa-solid fa-gauge"),
                        html.I(className="fa-solid fa-magnifying-glass"),
                        html.Span("RESEARCH", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/research",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-circle-info"),
                        html.Span("RESEARCH OUTCOMES", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/about",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        #html.I(className="fa-solid fa-gauge"),
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("DASHBOARD", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/dashboard",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-user-minus"),
                        html.Span("UNEMPLOYMENT", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/unemployment",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-user-check"),
                        html.Span("EMPLOYMENT", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/employment",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-person-circle-check"),
                        html.Span("LABOUR PARTICIPATION", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/labour",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-database"),
                        html.Span("DATA", style={'margin-left': '15px'})], className='icon_title')],
                        href="/apps/data",
                        active="exact",
                        className="pe-3"
                    ),
                ],
                vertical=True,
                pills=True,
            ),
        ],
         style={'font-family': 'Poppins, sans-serif !important'},
        id="bg_id",
        className="sidebar",
    )

])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/apps/research':
        return research.layout
    elif pathname == '/apps/dashboard':
        return dashboard.layout
    elif pathname == '/apps/unemployment':
        return unemployment.layout
    elif pathname == '/apps/employment':
        return employment.layout
    elif pathname == '/apps/labour':
        return labour.layout
    elif pathname == '/apps/data':
        return data.layout
    elif pathname == '/apps/about':
        return research_outcome.layout


if __name__ == '__main__':
    app.run_server(debug=True,port = 8503)
