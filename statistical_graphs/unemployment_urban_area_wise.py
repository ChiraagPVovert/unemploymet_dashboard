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


# In[5]:


def year_estimated_unemployment_rate_urban():
    
    #print(year)
    
    df_urban,year = fetch_dataframe()
    
    data = df_urban.groupby(['Year'])[['Estimated Unemployment Rate']].mean() #Grouped by month
    data = pd.DataFrame(data).reset_index()
    
    #print(data)
    
    Year = data.Year
    unemployment_rate = data['Estimated Unemployment Rate']

    fig = px.bar(data, x='Year', y='Estimated Unemployment Rate', color_discrete_sequence=['sky blue'] * len(data),
                 width=550, height=600)

    fig.update_layout(title='Yearly Estimated Average Unemployment Rate in Urban Areas - 2016 - 2021')

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
    #fig.show()
    
#year_estimated_unemployment_rate_urban = year_estimated_unemployment_rate_urban()
#year_estimated_unemployment_rate_urban.show()


# In[6]:


def year_monthly_estimated_unemployment_rate_urban():
    
    df_urban,year = fetch_dataframe()
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Convert 'Month' column to categorical with specified order
    df_urban['Month'] = pd.Categorical(df_urban['Month'], categories=month_order, ordered=True)
    
    average_unemployment_rate = df_urban.groupby(['Year', 'Month'])['Estimated Unemployment Rate'].mean().reset_index()
    
    fig = px.bar(average_unemployment_rate,x='Month',y='Estimated Unemployment Rate',animation_frame='Year',
                title='Estimated Unemployment rate in urban areas from 2016 - 2021',text="Month",width=550, height=600,
                 color_discrete_sequence =['sky blue']*len(average_unemployment_rate))
    
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(yaxis_range=[0, 30],
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
    fig.update_traces(textfont_size=40, textangle=0, textposition="outside", cliponaxis=False)
    
    return fig
        
#year_monthly_estimated_unemployment_rate_urban = year_monthly_estimated_unemployment_rate_urban()
#year_monthly_estimated_unemployment_rate_urban


# In[7]:


def estimated_unemployment_rate_in_urban_area_weekly_basis():
    
    df_urban,year = fetch_dataframe()
    
    fig=px.line(df_urban, x='Date', y='Estimated Unemployment Rate', title='Estimated Unemployment Rate in urban areas every week from 2016 to 2021',
                width=550, height=600, color_discrete_sequence=['sky blue'] * len(df_urban))

    fig.update_layout(yaxis_range=[0, 30],
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