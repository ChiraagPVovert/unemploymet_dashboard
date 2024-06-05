#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar


# In[3]:


def fetch_dataframe():
    
    df_urban = pd.read_csv('unemployment_rate_urban.csv')
    '''df_urban.head()

    df_urban.info()

    df_urban.isnull().sum()'''

    df_urban['Date'] = pd.to_datetime(df_urban['Date'],dayfirst = True)

    df_urban['Month'] = df_urban['Date'].dt.month.apply(lambda x: calendar.month_abbr[x])

    #Extracting year

    df_urban['Year'] = df_urban['Date'].dt.year
    x = df_urban['Year'][:1]
    year = int(x)

    return df_urban,year


# In[4]:


def year_estimated_labour_participation_rate_urban():
    
    #print(year)
    
    df_urban,year = fetch_dataframe()
    
    data = df_urban.groupby(['Year'])[['Estimated Labour Participation Rate']].mean() #Grouped by month
    data = pd.DataFrame(data).reset_index()
    
    #print(data)
    
    Year = data.Year
    labour_participation = data['Estimated Labour Participation Rate']

    fig = px.bar(data, x='Year', y='Estimated Labour Participation Rate', color_discrete_sequence=['sky blue'] * len(data),
                 width=550, height=600)
    
    fig.update_layout(title = 'Yearly Estimated Average Labour Participation Rate in urban Areas - 2016 - 2021')

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
    
    return fig
    #fig.show()

def year_monthly_labour_participation_rate_urban():
    
    df_urban,year = fetch_dataframe()
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Convert 'Month' column to categorical with specified order
    df_urban['Month'] = pd.Categorical(df_urban['Month'], categories=month_order, ordered=True)
    
    average_labour_participation_rate = df_urban.groupby(['Year', 'Month'])['Estimated Labour Participation Rate'].mean().reset_index()
    
    fig = px.bar(average_labour_participation_rate,x='Month',y='Estimated Labour Participation Rate',animation_frame='Year',
                title='Estimated Labour Participation Rate in urban areas from 2016 - 2021',text="Month",width=550, height=600,
                 color_discrete_sequence =['sky blue']*len(average_labour_participation_rate))

    fig.update_xaxes(showticklabels=False)
    #fig.update_layout(yaxis_range=[0,30])
    fig.update_layout(#yaxis_range=[0, 30],
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
    
    fig.update_xaxes(showticklabels=False)
    #fig.update_layout(yaxis_range=[0,30])
    fig.update_traces(textfont_size=40, textangle=0, textposition="outside", cliponaxis=False)
    
    return fig


def estimated_labour_participation_in_urban_area_weekly_basis():
    
    df_urban,year = fetch_dataframe()
    
    fig=px.line(df_urban, x='Date', y='Estimated Labour Participation Rate', title='Estimated Labour Participation Rate in urban areas every week from 2016 to 2021',
                width=550, height=600, color_discrete_sequence=['sky blue'] * len(df_urban))

    fig.update_layout(#yaxis_range=[0, 30],
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
    
    return fig





