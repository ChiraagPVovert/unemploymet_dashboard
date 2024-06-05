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
    
    df_overall = pd.read_csv('unemployment_rate_total.csv')

    df_overall.columns = ['Date','Frequency','Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate']

    df_overall['Date'] = pd.to_datetime(df_overall['Date'],dayfirst = True) #Convert the datatype to Date
    #print(df_overall)
    df_overall['monthly'] = df_overall['Date'].dt.month #Extracting Month from Date
    #print(df_overall)
    df_overall['Month'] = df_overall['monthly'].apply(lambda x: calendar.month_abbr[x])#convert the months into words
    #print(df_overall)


    #Extracting year

    df_overall['Year'] = df_overall['Date'].dt.year
    #print(df_overall)
    x = df_overall['Year'][:1]
    year = int(x)
    
    return df_overall,year


# In[4]:


def year_estimated_labour_participation_overall():
    
    #print(year)
    
    df_overall,year = fetch_dataframe()
    
    data = df_overall.groupby(['Year'])[['Estimated Labour Participation Rate']].mean() #Grouped by month
    data = pd.DataFrame(data).reset_index()
    
    #print(data)
    
    Year = data.Year
    estimated_labour = data['Estimated Labour Participation Rate']

    fig = px.bar(data, x='Year', y='Estimated Labour Participation Rate', color_discrete_sequence=['sky blue'] * len(data))
    
    fig.update_layout(title = 'Yearly Estimated Employed in India - 2016 - 2021',width=550, height=600)

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

def year_monthly_estimated_labour_participation_overall():
    
    df_overall,year = fetch_dataframe()
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Convert 'Month' column to categorical with specified order
    df_overall['Month'] = pd.Categorical(df_overall['Month'], categories=month_order, ordered=True)
    
    estimated_labour = df_overall.groupby(['Year', 'Month'])['Estimated Labour Participation Rate'].mean().reset_index()
    
    fig = px.bar(estimated_labour,x='Month',y='Estimated Labour Participation Rate',animation_frame='Year',
                title='Estimated Estimated Labour Participation Rate in overall areas from 2016 - 2021',text="Month",width=550, height=600,
                 color_discrete_sequence =['sky blue']*len(estimated_labour))
    
    fig.update_xaxes(showticklabels=False)
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
    #fig.update_layout(yaxis_range=[0,30])
    fig.update_traces(textfont_size=40, textangle=0, textposition="outside", cliponaxis=False)
    
    return fig

def estimated_labour_participation_in_overall_area_weekly_basis():
    
    df_overall,year = fetch_dataframe()
    
    fig=px.line(df_overall, x='Date', y='Estimated Labour Participation Rate', title='Estimated Labour Participation Rate every week from 2016 to 2021',
                width = 550, height = 600, color_discrete_sequence = ['sky blue'] * len(df_overall))

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




