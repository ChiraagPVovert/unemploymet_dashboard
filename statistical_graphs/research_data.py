import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import seaborn as sns
import plotly.graph_objects as go


def lab_corr_unemp(df, area):
    # Remove leading and trailing spaces from the 'Date' column
    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    df.sort_values(by='Date', inplace=True)

    columns = ['Estimated Labour Participation Rate', 'Estimated Unemployment Rate']

    correlation = df['Estimated Labour Participation Rate'].corr(df['Estimated Unemployment Rate'])

    correlation_str = area + " - Pearson Correlation Coefficient : " + str(round(correlation, 3))

    # Create a scatter plot using Plotly
    fig = px.scatter(df, x=columns[0], y=columns[1],
                     title='Correlation between Labour Participation Rate and Unemployment Rate ' + area,
                     labels={'Estimated Labour Participation Rate': 'Labour Participation Rate',
                             'Estimated Unemployment Rate': 'Unemployment Rate'},
                     hover_data=['Date'])
    fig.update_layout(title=correlation_str, width=550, height=400)  # title_1 + '<br>' +

    fig.update_layout(  # yaxis_range=[0, 30],
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 15},
        xaxis=dict(  # title='<b>Date</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(  # title='<b>Daily confirmed Cases</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),

        legend={
            'orientation': 'h',
            'bgcolor': '#3D3C3A',
            'xanchor': 'center', 'x': 0.5, 'y': -0.3},
        font=dict(
            family="sans-serif",
            size=12,
            color='white'),

    )

    interpretation = "The observed relationship between the estimated labor participation rate and the estimated unemployment rate indicates a statistically significant negative correlation. This negative correlation implies that, on average, as the unemployment rate increases, there is a tendency for the labor participation rate to decrease, and conversely, as the unemployment rate decreases, there is a tendency for the labor participation rate to increase. The strength of this negative correlation is quantified using the Pearson correlation coefficient, which provides a measure of the linear relationship between these two variables."

    # Show the plot
    return fig, interpretation


# The observed relationship between the estimated labor participation rate and the estimated unemployment rate indicates a statistically significant negative correlation.
# This negative correlation implies that, on average, as the unemployment rate increases, there is a tendency for the labor participation rate to decrease, and conversely, as the unemployment rate decreases, there is a tendency for the labor participation rate to increase.
# The strength of this negative correlation is quantified using the Pearson correlation coefficient, which provides a measure of the linear relationship between these two variables.
# df_overall = read_files_overall()
# fig,interpretation = lab_corr_unemp(df_overall,'Overall areas')
# fig.show()
#print(interpretation)
# df_rural = read_files_rural()
# fig_1,correlation_str_rural,interpretation = lab_corr_unemp(df_rural,'Rural areas')
# fig_1.show()
# df_urban = read_files_urban()
# fig_1,correlation_str_urban,interpretation = lab_corr_unemp(df_urban,'Urban areas')
# fig_1.show()

def weekly_deviation_labour(df, area):
    # Remove leading and trailing spaces from the 'Date' column
    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    df.sort_values(by='Date', inplace=True)

    # Calculate the standard deviation of the weekly Labour Participation Rates
    unemployment_rate_std = df['Estimated Labour Participation Rate'].std()

    # Print the result
    # print(f"The standard deviation of the weekly Labour Participation Rates is: {unemployment_rate_std:.2f}")
    unemployment_rate_std = round(unemployment_rate_std, 3)

    interpretation = (
        f"The standard deviation of {unemployment_rate_std} in weekly Labour Participation Rates {area} <br>"
        f"indicates the average deviation from the mean."
    )

    interpretation_2 = (
        f"It serves as a measure of volatility, with a higher value suggesting greater variability. "
        f"A small proportion relative to the mean indicates lower variability, while a larger proportion may signify higher variability."
    )

    mean_unemployment_rate = df['Estimated Labour Participation Rate'].mean()
    std_unemployment_rate = df['Estimated Labour Participation Rate'].std()

    # Create a line plot for the weekly Labour Participation Rates
    fig = px.line(df, x='Date', y='Estimated Labour Participation Rate',
                  title='Weekly Labour Participation Rates with Variability '+area+'<br>'+interpretation.lower(),
                  labels={'Estimated Labour Participation Rate': 'Labour Participation Rate'})

    # Add scatter plot to highlight individual data points
    fig.add_trace(
        px.scatter(df, x='Date', y='Estimated Labour Participation Rate', color_discrete_sequence=['red']).data[0])

    # Add shaded areas representing one and two standard deviations from the mean
    fig.add_shape(type='rect', x0=df['Date'].min(), x1=df['Date'].max(),
                  y0=mean_unemployment_rate - std_unemployment_rate, y1=mean_unemployment_rate + std_unemployment_rate,
                  line=dict(color='rgba(0,0,0,0)'), fillcolor='rgba(0,100,80,0.2)', layer='below')

    fig.add_shape(type='rect', x0=df['Date'].min(), x1=df['Date'].max(),
                  y0=mean_unemployment_rate - 2 * std_unemployment_rate,
                  y1=mean_unemployment_rate + 2 * std_unemployment_rate,
                  line=dict(color='rgba(0,0,0,0)'), fillcolor='rgba(0,100,80,0.4)', layer='below')

    fig.update_layout(  # yaxis_range=[0, 30],
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 15},
        xaxis=dict(  # title='<b>Date</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(  # title='<b>Daily confirmed Cases</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),

        legend={
            'orientation': 'h',
            'bgcolor': '#3D3C3A',
            'xanchor': 'center', 'x': 0.5, 'y': -0.3},
        font=dict(
            family="sans-serif",
            size=12,
            color='white'),

    )

    # These are the 1 standard deviation formulas from the mean
    # formula = y0=mean_unemployment_rate - std_unemployment_rate
    # formula = y1=mean_unemployment_rate + std_unemployment_rate

    # These are the 2 standard deviations formulas from the mean
    # formula = y0=mean_unemployment_rate - 2 * std_unemployment_rate
    # formula = y1=mean_unemployment_rate + 2 * std_unemployment_rate

    # fig.show()

    return fig, interpretation, interpretation_2


#df_overall = read_files_overall()
#fig, std_deviation_overall, interpretation = weekly_deviation_labour(df_overall, 'overall')
#print(std_deviation_overall)
#fig
# df_rural = read_files_rural()
# fig_1,std_deviation_rural = weekly_deviation_labour(df_rural,'in rural areas')
# print(std_deviation_rural)
# fig_1
# fig_2,df_urban = read_files_urban()
# std_deviation_urban = weekly_deviation_labour(df_urban,'in rural areas')
# print(std_deviation_urban)
# fig_2

def weekly_deviation_unemployment(df, area):
    # Remove leading and trailing spaces from the 'Date' column
    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    df.sort_values(by='Date', inplace=True)

    # Calculate the standard deviation of the weekly Estimated Unemployment Rates
    unemployment_rate_std = df['Estimated Unemployment Rate'].std()

    # Print the result
    # print(f"The standard deviation of the weekly Estimated Unemployment Rates is: {unemployment_rate_std:.2f}")
    unemployment_rate_std = round(unemployment_rate_std, 3)

    interpretation = (
        f"The standard deviation of {unemployment_rate_std} in weekly Unemployment Rates {area}<br> "
        f"indicates the average deviation from the mean."
    )

    interpretation_2 = (
        f"It serves as a measure of volatility, with a higher value suggesting greater variability. "
        f"A small proportion relative to the mean indicates lower variability, while a larger proportion may signify higher variability."
    )

    mean_unemployment_rate = df['Estimated Unemployment Rate'].mean()
    std_unemployment_rate = df['Estimated Unemployment Rate'].std()

    # Create a line plot for the weekly Estimated Unemployment Rates
    fig = px.line(df, x='Date', y='Estimated Unemployment Rate',
                  title='Weekly Estimated Unemployment Rates with Variability '+area+'<br>'+interpretation.lower(),
                  labels={'Estimated Estimated Unemployment Rate': 'Estimated Unemployment Rate'})

    # Add scatter plot to highlight individual data points
    fig.add_trace(px.scatter(df, x='Date', y='Estimated Unemployment Rate', color_discrete_sequence=['red']).data[0])

    # Add shaded areas representing one and two standard deviations from the mean
    fig.add_shape(type='rect', x0=df['Date'].min(), x1=df['Date'].max(),
                  y0=mean_unemployment_rate - std_unemployment_rate, y1=mean_unemployment_rate + std_unemployment_rate,
                  line=dict(color='rgba(0,0,0,0)'), fillcolor='rgba(0,100,80,0.2)', layer='below')

    fig.add_shape(type='rect', x0=df['Date'].min(), x1=df['Date'].max(),
                  y0=mean_unemployment_rate - 2 * std_unemployment_rate,
                  y1=mean_unemployment_rate + 2 * std_unemployment_rate,
                  line=dict(color='rgba(0,0,0,0)'), fillcolor='rgba(0,100,80,0.4)', layer='below')

    fig.update_layout(  # yaxis_range=[0, 30],
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 15},
        xaxis=dict(  # title='<b>Date</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(  # title='<b>Daily confirmed Cases</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),

        legend={
            'orientation': 'h',
            'bgcolor': '#3D3C3A',
            'xanchor': 'center', 'x': 0.5, 'y': -0.3},
        font=dict(
            family="sans-serif",
            size=12,
            color='white'),

    )

    # These are the 1 standard deviation formulas from the mean
    # formula = y0=mean_unemployment_rate - std_unemployment_rate
    # formula = y1=mean_unemployment_rate + std_unemployment_rate

    # These are the 2 standard deviations formulas from the mean
    # formula = y0=mean_unemployment_rate - 2 * std_unemployment_rate
    # formula = y1=mean_unemployment_rate + 2 * std_unemployment_rate

    # fig.show()

    return fig, interpretation, interpretation_2


#df_overall = read_files_overall()
#fig, std_deviation_overall, final_interpretation = weekly_deviation_unemployment(df_overall, 'overall')
#print(std_deviation_overall)
#fig
# df_rural = read_files_rural()
# fig_1,std_deviation_rural,final_interpretation = weekly_deviation_unemployment(df_rural,'in rural areas')
# print(std_deviation_rural)
# fig_1
# fig_2,df_urban = read_files_urban()
# std_deviation_urban,final_interpretation = weekly_deviation_unemployment(df_urban,'in rural areas')
# print(std_deviation_urban)
# fig_2

def weekly_deviation_employ(df, area):
    # Remove leading and trailing spaces from the 'Date' column
    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    df.sort_values(by='Date', inplace=True)

    # Calculate the standard deviation of the weekly Estimated Employed
    unemployment_rate_std = df['Estimated Employed'].std()

    # Print the result
    # print(f"The standard deviation of the weekly Estimated Employed is: {unemployment_rate_std:.2f}")
    unemployment_rate_std = round(unemployment_rate_std, 3)

    interpretation = (
        f"The standard deviation of {unemployment_rate_std} in weekly Employed {area} <br> "
        f"indicates the average deviation from the mean."
    )

    interpretation_2 = (
        f"It serves as a measure of volatility, with a higher value suggesting greater variability. "
        f"A small proportion relative to the mean indicates lower variability, while a larger proportion may signify higher variability."
    )

    mean_unemployment_rate = df['Estimated Employed'].mean()
    std_unemployment_rate = df['Estimated Employed'].std()

    # Create a line plot for the weekly Estimated Employed
    fig = px.line(df, x='Date', y='Estimated Employed',
                  title='Weekly Estimated Employed with Variability '+area+'<br>'+interpretation.lower(),
                  labels={'Estimated Estimated Employed': 'Estimated Employed'})

    # Add scatter plot to highlight individual data points
    fig.add_trace(px.scatter(df, x='Date', y='Estimated Employed', color_discrete_sequence=['red']).data[0])

    # Add shaded areas representing one and two standard deviations from the mean
    fig.add_shape(type='rect', x0=df['Date'].min(), x1=df['Date'].max(),
                  y0=mean_unemployment_rate - std_unemployment_rate, y1=mean_unemployment_rate + std_unemployment_rate,
                  line=dict(color='rgba(0,0,0,0)'), fillcolor='rgba(0,100,80,0.2)', layer='below')

    fig.add_shape(type='rect', x0=df['Date'].min(), x1=df['Date'].max(),
                  y0=mean_unemployment_rate - 2 * std_unemployment_rate,
                  y1=mean_unemployment_rate + 2 * std_unemployment_rate,
                  line=dict(color='rgba(0,0,0,0)'), fillcolor='rgba(0,100,80,0.4)', layer='below')

    fig.update_layout(  # yaxis_range=[0, 30],
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 15},
        xaxis=dict(  # title='<b>Date</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(  # title='<b>Daily confirmed Cases</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),

        legend={
            'orientation': 'h',
            'bgcolor': '#3D3C3A',
            'xanchor': 'center', 'x': 0.5, 'y': -0.3},
        font=dict(
            family="sans-serif",
            size=12,
            color='white'),

    )

    # These are the 1 standard deviation formulas from the mean
    # formula = y0=mean_unemployment_rate - std_unemployment_rate
    # formula = y1=mean_unemployment_rate + std_unemployment_rate

    # These are the 2 standard deviations formulas from the mean
    # formula = y0=mean_unemployment_rate - 2 * std_unemployment_rate
    # formula = y1=mean_unemployment_rate + 2 * std_unemployment_rate

    # fig.show()

    return fig, interpretation, interpretation_2

# df_overall = read_files_overall()
# fig_std_employ_overall,std_deviation_overall,final_interpretation = weekly_deviation_employ(df_overall,'overall')
# print(std_deviation_overall)
# fig
# df_rural = read_files_rural()
# fig_std_rural_overall,std_deviation_rural,final_interpretation = weekly_deviation_employment(df_rural,'in rural areas')
# print(std_deviation_rural)
# fig_1
# fig_2,df_urban = read_files_urban()
# fig_std_employ_urban,std_deviation_urban,final_interpretation = weekly_deviation_employment(df_urban,'in urban areas')
# print(std_deviation_urban)
# fig_2

import plotly.express as px


def time_series_analysis(df):
    # ... your existing preprocessing code ...
    # Remove leading and trailing spaces from the 'Date' column
    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    df.sort_values(by='Date', inplace=True)

    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)

    # Time series decomposition
    decomposition_unemployment = sm.tsa.seasonal_decompose(df['Estimated Unemployment Rate'])
    decomposition_employed = sm.tsa.seasonal_decompose(df['Estimated Employed'])
    decomposition_participation = sm.tsa.seasonal_decompose(df['Estimated Labour Participation Rate'])

    # Create a list to store all the figures
    figs = []

    # Original series
    figs.append(px.line(df, y='Estimated Unemployment Rate', title='Original Series - Unemployment Rate'))
    figs.append(px.line(df, y='Estimated Employed', title='Original Series - Employed'))
    figs.append(
        px.line(df, y='Estimated Labour Participation Rate', title='Original Series - Labour Participation Rate'))

    # Trend
    figs.append(px.line(decomposition_unemployment.trend.dropna(), title='Trend - Unemployment Rate'))
    figs.append(px.line(decomposition_employed.trend.dropna(), title='Trend - Employed'))
    figs.append(px.line(decomposition_participation.trend.dropna(), title='Trend - Labour Participation Rate'))

    # Seasonality
    figs.append(px.line(decomposition_unemployment.seasonal, title='Seasonality - Unemployment Rate'))
    figs.append(px.line(decomposition_employed.seasonal, title='Seasonality - Employed'))
    figs.append(px.line(decomposition_participation.seasonal, title='Seasonality - Labour Participation Rate'))

    # Residuals
    figs.append(px.line(decomposition_unemployment.resid.dropna(), title='Residuals - Unemployment Rate'))
    figs.append(px.line(decomposition_employed.resid.dropna(), title='Residuals - Employed'))
    figs.append(px.line(decomposition_participation.resid.dropna(), title='Residuals - Labour Participation Rate'))

    for fig in figs:
        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 15},
            xaxis=dict(  # title='<b>Date</b>',
                color='white',
                showline=False,
                showgrid=False,
                showticklabels=True,
                linecolor='white',
                linewidth=2,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='white'
                )
            ),
            yaxis=dict(  # title='<b>Daily confirmed Cases</b>',
                color='white',
                showline=False,
                showgrid=False,
                showticklabels=True,
                linecolor='white',
                linewidth=2,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='white'
                )
            ),

            legend={
                'orientation': 'h',
                'bgcolor': '#3D3C3A',
                'xanchor': 'center', 'x': 0.5, 'y': -0.3},
            font=dict(
                family="sans-serif",
                size=12,
                color='white'),

        )

    return figs


#df_overall = read_files_overall()
#tsa_overall = time_series_analysis(df_overall)
#tsa_overall[0].show()

def lag_analysis(df, area):
    # Remove leading and trailing spaces from the 'Date' column
    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    df.sort_values(by='Date', inplace=True)

    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)

    # Specify the variables for lag analysis
    lag_variables = ['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']

    # Create lagged columns for each variable
    for variable in lag_variables:
        for lag in range(1, 4):  # Adjust the lag range as needed
            df[f'{variable} (lag {lag})'] = df[variable].shift(lag)

    # Calculate correlation matrix for lagged variables
    corr_matrix = df[list(df.filter(regex='lag'))].corr()

    # Plot correlation heatmap for lagged variables using Plotly Express
    fig = px.imshow(corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.index,
                    labels=dict(color='Correlation'),
                    color_continuous_scale='Viridis',
                    color_continuous_midpoint=0,
                    width=1300,  # Adjust the width as needed
                    height=900,  # Adjust the height as needed
                    text_auto=True,
                    aspect='auto')

    fig.update_layout(
        title='Correlation Heatmap for Lagged Variables' + area,
        # xaxis=dict(tickfont=dict(size=14)),  # Adjust font size for x-axis ticks
        # yaxis=dict(tickfont=dict(size=14)),  # Adjust font size for y-axis ticks
        coloraxis_colorbar=dict(tickfont=dict(size=14)),  # Adjust font size for colorbar ticks
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 25},
        xaxis=dict(  # title='<b>Date</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        yaxis=dict(  # title='<b>Daily confirmed Cases</b>',
            color='white',
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='white'
            )
        ),
        legend={
            'orientation': 'h',
            'bgcolor': '#3D3C3A',
            'xanchor': 'center', 'x': 0.5, 'y': -0.3},
        font=dict(
            family="sans-serif",
            size=12,
            color='white'),
    )

    # Add values to each box in the heatmap
    fig.update_traces(showscale=True)

    return fig


#df_overall = read_files_overall()
#fig_lag_overall = lag_analysis(df_overall, ' Overall')
#fig_lag_overall.show()