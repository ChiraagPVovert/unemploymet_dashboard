from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd

df_rural = pd.read_csv('unemployment_rate_rural.csv')
df_urban = pd.read_csv('unemployment_rate_urban.csv')
df_2020 = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
df_total = pd.read_csv('unemployment_rate_total.csv')

layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "DATA", style={"color": "#0084d6",
                               "font-size": "30px",
                               'margin-left': '30px',
                               'margin-top': '15px',
                               'text-align':'center',}
            ),
        ], className='home_bg ten columns')
    ], className='home_row row'),
   html.Div([
        dbc.Row(
            justify="center",  # Center the content horizontally within the row
            children=[
                dbc.Col([
                    html.H2('RURAL DATA', style={"color": "#0084d6", "text-align": "center"}),
                    dbc.Table.from_dataframe(df_rural.head(10), striped=True, bordered=True, hover=True)
                ], width=5),

                dbc.Col([
                    html.H2('URBAN DATA', style={"color": "#0084d6", "text-align": "center"}),
                    dbc.Table.from_dataframe(df_urban.head(10), striped=True, bordered=True, hover=True)
                ], width=5),
            ]
        ),

        dbc.Row(
            justify="center",  # Center the content horizontally within the row
            children=[
                dbc.Col([
                    html.H2('OVERALL DATA', style={"color": "#0084d6", "text-align": "center"}),
                    dbc.Table.from_dataframe(df_total.head(10), striped=True, bordered=True, hover=True)
                ], width=5),

                dbc.Col([
                    html.H2('YEAR 2020 DATA', style={"color": "#0084d6", "text-align": "center"}),
                    dbc.Table.from_dataframe(df_2020.head(10), striped=True, bordered=True, hover=True)
                ], width=5),
            ]
        ),
    ]),
])
