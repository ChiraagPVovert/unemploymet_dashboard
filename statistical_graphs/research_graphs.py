import datetime
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import seaborn as sns
import plotly.graph_objects as go
from statistical_graphs import research_data as rd

original_series_description = """
The original series in time series analysis represents the observed data points over time. It encompasses the actual values of the variable of interest without any adjustments or decomposition. In the context of labor market data, the original series would include the recorded weekly values of the estimated unemployment rate, the number of employed individuals, and the labor participation rate. Analyzing the original series provides insights into the raw, unaltered temporal trends and fluctuations in the data.
"""

trend_description = """
The trend component in time series decomposition represents the long-term direction or overall pattern in the data. It aims to capture the underlying growth or decline in the variable of interest, excluding short-term fluctuations and seasonality. In the context of the labor market, the trend would highlight the fundamental, sustained changes in the estimated unemployment rate, employed individuals, or labor participation rate over an extended period. Understanding the trend is crucial for identifying the overall trajectory and underlying dynamics of the labor market.
"""

seasonality_description = """
Seasonality in time series analysis refers to recurring patterns or fluctuations in the data that follow a regular and predictable schedule, typically associated with specific time periods. For labor market data, seasonality might manifest as periodic changes in employment rates or labor force participation that repeat weekly, monthly, or seasonally. Identifying and understanding seasonality helps reveal consistent, time-dependent variations that may be attributed to external factors such as holidays, weather, or economic cycles.
"""

residuals_description = """
Residuals represent the unexplained, random variations in the data that remain after removing the trend and seasonality components. They capture irregularities, noise, or unexpected fluctuations in the original series. In labor market analysis, residuals could signify unexpected changes in employment or labor force participation that are not accounted for by the identified trend or seasonality. Analyzing residuals aids in detecting anomalies, uncovering unforeseen influences, and assessing the accuracy of the decomposition model.
"""

def read_files_overall():
    df_overall = pd.read_csv('unemployment_rate_total.csv')
    df_overall['Date'] = df_overall['Date'].str.strip()

    return df_overall


def read_files_rural():
    df_rural = pd.read_csv('unemployment_rate_rural.csv')
    df_rural['Date'] = df_rural['Date'].str.strip()

    return df_rural


def read_files_urban():
    df_urban = pd.read_csv('unemployment_rate_urban.csv')
    df_urban['Date'] = df_urban['Date'].str.strip()

    return df_urban

def lab_corr_graphs():

    df_overall = read_files_overall()
    fig_overall,interpretation = rd.lab_corr_unemp(df_overall,'Overall areas')

    df_rural = read_files_rural()
    fig_rural,interpretation = rd.lab_corr_unemp(df_rural,'Rural areas')

    df_urban = read_files_urban()
    fig_urban, interpretation = rd.lab_corr_unemp(df_urban, 'Urban areas')

    return fig_overall,fig_rural,fig_urban,interpretation

def std_deviation_graphs_overall():

    df_overall = read_files_overall()
    fig_overall_std, std_deviation_overall, interpretation_std = rd.weekly_deviation_labour(df_overall, 'overall')
    #print(std_deviation_overall)
    #fig
    df_rural = read_files_rural()
    fig_rural_std,std_deviation_rural, interpretation_std = rd.weekly_deviation_labour(df_rural,'in rural areas')
    #print(std_deviation_rural)
    # fig_1
    df_urban = read_files_urban()
    fig_urban_std,std_deviation_urban, interpretation_std = rd.weekly_deviation_labour(df_urban,'in urban areas')
    # print(std_deviation_urban)
    # fig_2

    return fig_overall_std,fig_rural_std,fig_urban_std, interpretation_std

def std_deviation_graphs_unemployment():

    df_overall = read_files_overall()
    fig_std_overall, std_deviation_overall, final_interpretation = rd.weekly_deviation_unemployment(df_overall, 'overall')
    #print(std_deviation_overall)
    #fig
    df_rural = read_files_rural()
    fig_std_rural,std_deviation_rural,final_interpretation = rd.weekly_deviation_unemployment(df_rural,'in rural areas')
    # print(std_deviation_rural)
    # fig_1
    df_urban = read_files_urban()
    fig_std_urban,std_deviation_urban,final_interpretation = rd.weekly_deviation_unemployment(df_urban,'in urban areas')
    # print(std_deviation_urban)
    # fig_2

    return fig_std_overall, fig_std_rural, fig_std_urban, final_interpretation

def std_deviation_graphs_employ():

    df_overall = read_files_overall()
    fig_std_employ_overall,std_deviation_overall,final_interpretation = rd.weekly_deviation_employ(df_overall,'overall')
    # print(std_deviation_overall)
    # fig
    df_rural = read_files_rural()
    fig_std_rural_overall,std_deviation_rural,final_interpretation = rd.weekly_deviation_employ(df_rural,'in rural areas')
    # print(std_deviation_rural)
    # fig_1
    df_urban = read_files_urban()
    fig_std_employ_urban,std_deviation_urban,final_interpretation = rd.weekly_deviation_employ(df_urban,'in urban areas')
    # print(std_deviation_urban)
    # fig_2
    return fig_std_employ_overall, fig_std_rural_overall, fig_std_employ_urban, final_interpretation

def time_series_analysis_graphs():

    df_overall = read_files_overall()
    tsa_overall = rd.time_series_analysis(df_overall)

    df_rural = read_files_rural()
    tsa_rural = rd.time_series_analysis(df_rural)

    df_urban = read_files_urban()
    tsa_urban = rd.time_series_analysis(df_urban)

    return tsa_overall,tsa_rural,tsa_urban,original_series_description,trend_description,seasonality_description,residuals_description

def lag_analysis_graph():

    df_overall = read_files_overall()
    fig_lag_overall = rd.lag_analysis(df_overall, ' Overall')
    #fig_lag_overall.show()

    df_rural = read_files_rural()
    fig_lag_rural = rd.lag_analysis(df_rural, ' in rural areas')

    df_urban = read_files_urban()
    fig_lag_urban = rd.lag_analysis(df_urban, ' in urban areas')

    return fig_lag_overall,fig_lag_rural,fig_lag_urban