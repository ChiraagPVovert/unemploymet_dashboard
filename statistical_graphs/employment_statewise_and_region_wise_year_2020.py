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
    
    df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')

    df.columns = ['state','date','frequency','estimated unemployment rate','estimated employed','estimated labour participation_rate','region','longitude','latitude']

    df['date'] = pd.to_datetime(df['date'],dayfirst = True) #Convert the datatype to date
    #print(df)
    df['monthly'] = df['date'].dt.month #Extracting Month from date
    #print(df)
    df['month'] = df['monthly'].apply(lambda x: calendar.month_abbr[x])#convert the months into words
    #print(df)


    #Extracting year

    df['year'] = df['date'].dt.year
    #print(df)
    x = df['year'][:1]
    year = int(x)
    
    return df,year


# In[3]:


def monthly_estimated_employed():
    
    #print(year)
    
    df,year = fetch_dataframe()
    
    data = df.groupby(['month'])[['estimated employed']].mean() #Grouped by month
    data=pd.DataFrame(data).reset_index()
    
    #print(data)
    
    month = data.month
    employed = data['estimated employed']

    fig = px.bar(data, x='month', y='estimated employed', color_discrete_sequence=['sky blue'] * len(data),
                 width=800, height=600)

    fig.update_layout(title='Monthly Estimated Average Employed - Year ' + str(year),
                      xaxis={'categoryorder': 'array',
                             'categoryarray': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']})

    fig.update_layout(  # yaxis_range=[0, 30],
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 20},
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



def statewise_average_employed():
    
    df,year = fetch_dataframe()
    
    state =  df.groupby(['state'])[['estimated employed']].mean()
    state = pd.DataFrame(state).reset_index()
    state = state.sort_values(by=['estimated employed'], ascending=False)
    #print(state)
    
    fig = px.bar(state,x='state',y='estimated employed',color='state',title='Estimated Employed',
                 width=800, height=600,color_discrete_sequence=['sky blue'] * len(df))
    #fig.update_layout(xaxis={'categoryorder':'total descending'})
    #fig.show()
    fig.update_layout(title = 'Estimated Average Employed - Year '+str(year))

    fig.update_layout(#yaxis_range=[0, 30],
                      showlegend=False,
                      plot_bgcolor='#3D3C3A',
                      paper_bgcolor='#3D3C3A',
                      titlefont={
                          'color': 'white',
                          'size': 20},
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


def statewise_monthly_average_employed():
    
    df,year = fetch_dataframe()
    
    fig = px.bar(df,x='state',y='estimated employed',animation_frame='month',color='state',
                title='Estimated Employed, statewise every month in the year 2020',text="state",width=1500, height=600,
                color_discrete_sequence=['sky blue'] * len(df))
    
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(yaxis_range=[0,61000000])
    fig.update_traces(textfont_size=100, textangle=90, textposition="outside", cliponaxis=False)
    fig.update_layout(  # yaxis_range=[0, 30],
        showlegend=False,
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 20},
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


def regionwise_monthly_average_employed():
    
    df,year = fetch_dataframe()
    
    region =  df.groupby(['region'])[['estimated employed']].mean()
    region = pd.DataFrame(region).reset_index()
    region = region.sort_values(by=['estimated employed'], ascending=False)
    
    fig = px.bar(df,x='region',y='estimated employed',animation_frame='month',color='region',
                title='Estimated Employed, region wise every month in the year 2020',width=800, height=600,
                 color_discrete_sequence=['sky blue'] * len(df))

    fig.update_layout(  # yaxis_range=[0, 30],
        showlegend=False,
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 20},
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
    #fig.update_xaxes(showticklabels=False)
    #fig.update_layout(yaxis_range=[0,200])
    
    return fig


def regionwise_average_employed():
    
    df,year = fetch_dataframe()
    
    region =  df.groupby(['region'])[['estimated employed']].mean()
    region = pd.DataFrame(region).reset_index()
    region = region.sort_values(by=['estimated employed'], ascending=False)
    
    fig = px.bar(region,x='region',y='estimated employed',color='region',title='Average estimated employed regionwise in the year 2020',
                 width=800, height=600,color_discrete_sequence=['sky blue'] * len(df))
    fig.update_layout(  # yaxis_range=[0, 30],
        showlegend=False,
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 20},
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



def map_statewise_monthly_average_employed():
    
    df,year = fetch_dataframe()

    fig=px.scatter_geo(df,'longitude','latitude',color='state',
                      hover_name='state',size='estimated employed',
                      animation_frame='month',scope='asia',title='Estimated Employed in India at the year 2020',
                      opacity = 0.8,size_max=30,
                      #width=1000,
                      height=1000,
                      color_discrete_sequence=['sky blue'] * len(df))

    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] =5000
    fig.update_geos(lataxis_range=[7,37],lonaxis_range=[67,98],
                    oceancolor='lightblue',showocean=True,
                   )

    fig.update_layout(geo = dict(
                        showland = True,
                        showlakes = True,
                        showsubunits = True,
                        showcountries = True,
                        resolution = 50,
                        ))
    fig.update_layout(  # yaxis_range=[0, 30],
        showlegend=False,
        plot_bgcolor='#3D3C3A',
        paper_bgcolor='#3D3C3A',
        titlefont={
            'color': 'white',
            'size': 20},
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

    #fig.show()
    return fig





