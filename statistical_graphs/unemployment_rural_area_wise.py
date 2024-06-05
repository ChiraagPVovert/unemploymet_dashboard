#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar


# In[2]:


def fetch_dataframe():
    
    df_rural = pd.read_csv('unemployment_rate_rural.csv')    
    
    '''df_rural.head()

    df_rural.info()

    df_rural.isnull().sum()'''
    

    df_rural['Date'] = pd.to_datetime(df_rural['Date'],dayfirst = True)

    df_rural['Month'] = df_rural['Date'].dt.month.apply(lambda x: calendar.month_abbr[x])

    #Extracting year

    df_rural['Year'] = df_rural['Date'].dt.year
    x = df_rural['Year'][:1]
    year = int(x)

    return df_rural,year


# In[3]:


def year_estimated_unemployment_rate_rural():
    
    df_rural,year = fetch_dataframe()
    
    #print(year)
    
    data = df_rural.groupby(['Year'])[['Estimated Unemployment Rate']].mean() #Grouped by month
    data = pd.DataFrame(data).reset_index()
    
    #print(data)
    
    Year = data.Year
    unemployment_rate = data['Estimated Unemployment Rate']

    #fig = go.Figure()

    #fig.add_trace(go.Bar(x = Year,y = unemployment_rate,name = 'Unemployment Rate'))

    fig = px.bar(data, x='Year', y='Estimated Unemployment Rate', color_discrete_sequence=['sky blue'] * len(data),
                 width=550, height=600)
    
    fig.update_layout(title = 'Yearly Estimated Average Unemployment Rate in Rural Areas - 2016 - 2021')

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



def year_monthly_estimated_unemployment_rate_rural():
    
    df_rural,year = fetch_dataframe()
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Convert 'Month' column to categorical with specified order
    df_rural['Month'] = pd.Categorical(df_rural['Month'], categories=month_order, ordered=True)
    
    average_unemployment_rate = df_rural.groupby(['Year', 'Month'])['Estimated Unemployment Rate'].mean().reset_index()
    
    fig = px.bar(average_unemployment_rate,x='Month',y='Estimated Unemployment Rate',animation_frame='Year',
                title='Estimated Unemployment rate in rural areas from 2016 - 2021',text="Month",width=550, height=600,
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

def estimated_unemployment_rate_in_rural_area_weekly_basis():
    
    df_rural,year = fetch_dataframe()
    
    fig=px.line(df_rural, x='Date', y='Estimated Unemployment Rate', title='Estimated Unemployment Rate in rural areas every week from 2016 to 2021',
                width=550, height=600,color_discrete_sequence =['sky blue']*len(df_rural))

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



