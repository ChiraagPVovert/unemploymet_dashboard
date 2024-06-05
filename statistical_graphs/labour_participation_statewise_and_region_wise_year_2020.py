#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar


# In[7]:


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


# In[8]:


def monthly_labour_participation():
    
    #print(year)
    
    df,year = fetch_dataframe()
    
    data = df.groupby(['month'])[['estimated labour participation_rate']].mean() #Grouped by month
    data=pd.DataFrame(data).reset_index()
    
    #print(data)
    
    month = data.month
    labour_participation = data['estimated labour participation_rate']

    fig = px.bar(data, x='month', y='estimated labour participation_rate', color_discrete_sequence=['sky blue'] * len(data),
                 width=800, height=600)
    
    fig.update_layout(title = 'Monthly Estimated Labour Participation Rate - Year '+str(year),
                         xaxis = {'categoryorder':'array','categoryarray':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct']})

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


def statewise_average_labour_participation_rate():
    
    df,year = fetch_dataframe()
    
    state =  df.groupby(['state'])[['estimated labour participation_rate']].mean()
    state = pd.DataFrame(state).reset_index()
    state = state.sort_values(by=['estimated labour participation_rate'], ascending=False)
    #print(state)
    
    fig = px.bar(state,x='state',y='estimated labour participation_rate',color='state',title='Estimated Labour Participation Rate',
                 width=800, height=600,color_discrete_sequence=['sky blue'] * len(df))
    #fig.update_layout(xaxis={'categoryorder':'total descending'})
    #fig.show()
    fig.update_layout(title = 'Estimated Average Labour Participation Rate - Year '+str(year))

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



def statewise_monthly_average_labour_participation_rate():
    
    df,year = fetch_dataframe()
    
    fig = px.bar(df,x='state',y='estimated labour participation_rate',animation_frame='month',color='state',
                title='Estimated Labour Participation Rate, statewise every month in the year 2020',text="state",width=1500, height=600,
                 color_discrete_sequence=['sky blue'] * len(df))
    
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(yaxis_range=[0,70])
    fig.update_traces(textfont_size=40, textangle=90, textposition="outside", cliponaxis=False)
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



def regionwise_monthly_average_labour_participation_rate():
    
    df,year = fetch_dataframe()
    
    region =  df.groupby(['region'])[['estimated labour participation_rate']].mean()
    region = pd.DataFrame(region).reset_index()
    region = region.sort_values(by=['estimated labour participation_rate'], ascending=False)
    
    fig = px.bar(df,x='region',y='estimated labour participation_rate',animation_frame='month',color='region',
                title='Estimated Labour Participation Rate, region wise every month in the year 2020',width=800, height=600,
                 color_discrete_sequence=['sky blue'] * len(df))#,text="region")#,width=1000, height=800)
    
    #fig.update_xaxes(showticklabels=False)
    fig.update_layout(yaxis_range=[0,400])
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



def regionwise_average_labour_participation_rate_estimate():
    
    df,year = fetch_dataframe()
    
    region =  df.groupby(['region'])[['estimated labour participation_rate']].mean()
    region = pd.DataFrame(region).reset_index()
    region = region.sort_values(by=['estimated labour participation_rate'], ascending=False)
    
    fig = px.bar(region,x='region',y='estimated labour participation_rate',color='region',title='Average estimated labour participation rate regionwise in the year 2020',
                width = 800, height = 600, color_discrete_sequence = ['sky blue'] * len(df))

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



# In[22]:


def map_statewise_monthly_average_labour_participation_rate_estimate():
    
    df,year = fetch_dataframe()

    fig=px.scatter_geo(df,'longitude','latitude',color='state',
                      hover_name='state',size='estimated labour participation_rate',
                      animation_frame='month',scope='asia',title='Estimated labour participation rate in India at the year 2020',
                      opacity = 0.8,size_max=30,
                      #width=1000,
                      height=800,
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





