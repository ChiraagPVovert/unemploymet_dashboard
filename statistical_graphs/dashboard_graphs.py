import datetime
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import seaborn as sns
import plotly.graph_objects as go
from statistical_graphs import dashboard_data as dd


def max_emp_unemp_lab_graph():
    graphs = []

    a = 0

    df_overall = dd.read_files_overall()
    max_week_overall, top_20_weeks_str_overall, top_20_weeks_data_overall = dd.max_emp_unemp_lab(df_overall)

    df_rural = dd.read_files_rural()
    max_week_rural, top_20_weeks_str_rural, top_20_weeks_data_rural = dd.max_emp_unemp_lab(df_rural)
    # print(max_week_rural)

    df_urban = dd.read_files_urban()
    max_week_urban, top_20_weeks_str_urban, top_20_weeks_data_urban = dd.max_emp_unemp_lab(df_urban)

    for i in range(3):
        title_1 = max_week_overall[a]
        title_2 = top_20_weeks_str_overall[a]
        data = pd.DataFrame(top_20_weeks_data_overall[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.line(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data), markers=True)

        fig.update_layout(title=title_2+'overall', width=550, height=400) #title_1 + '<br>' +

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
        graphs.append(fig)

        title_1 = max_week_rural[a]
        title_2 = top_20_weeks_str_rural[a]
        data = pd.DataFrame(top_20_weeks_data_rural[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.line(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data), markers=True)

        fig.update_layout(title=title_2+'rural areas', width=550, height=400)#title_1 + '<br>' +

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
        graphs.append(fig)

        title_1 = max_week_urban[a]
        title_2 = top_20_weeks_str_urban[a]
        data = pd.DataFrame(top_20_weeks_data_urban[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.line(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data), markers=True)

        fig.update_layout(title=title_2+'urban areas', width=550, height=400) #title_1 + '<br>' +

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
        graphs.append(fig)
        a += 1

    return graphs


#graphs = max_emp_unemp_lab_graph()
#for i in graphs:
#    i.show()

def min_emp_unemp_lab_graph():
    graphs = []

    a = 0

    df_overall = dd.read_files_overall()
    min_week_overall, top_20_weeks_str_overall, top_20_weeks_data_overall = dd.min_emp_unemp_lab(df_overall)

    df_rural = dd.read_files_rural()
    min_week_rural, top_20_weeks_str_rural, top_20_weeks_data_rural = dd.min_emp_unemp_lab(df_rural)
    # print(min_week_rural)

    df_urban = dd.read_files_urban()
    min_week_urban, top_20_weeks_str_urban, top_20_weeks_data_urban = dd.min_emp_unemp_lab(df_urban)

    for i in range(3):
        title_1 = min_week_overall[a]
        title_2 = top_20_weeks_str_overall[a]
        data = pd.DataFrame(top_20_weeks_data_overall[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.line(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data), markers=True)

        fig.update_layout(title=title_2+'overall', width=550, height=400) #title_1 + '<br>' +

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
        graphs.append(fig)

        title_1 = min_week_rural[a]
        title_2 = top_20_weeks_str_rural[a]
        data = pd.DataFrame(top_20_weeks_data_rural[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.line(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data), markers=True)

        fig.update_layout(title=title_2+'rural areas', width=550, height=400)#title_1 + '<br>' +

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
        graphs.append(fig)

        title_1 = min_week_urban[a]
        title_2 = top_20_weeks_str_urban[a]
        data = pd.DataFrame(top_20_weeks_data_urban[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.line(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data), markers=True)

        fig.update_layout(title=title_2+'urban areas', width=550, height=400) #title_1 + '<br>' +

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
        graphs.append(fig)
        a += 1

    return graphs


#graphs = min_emp_unemp_lab_graph()
#for i in graphs:
#    i.show()

def highest_rate_change_graph():
    graphs = []

    a = 0

    df_overall = dd.read_files_overall()
    top_10_week_with_highest_rate_change_str_overall, top_10_week_with_highest_rate_change_overall = dd.highest_rate_change(
        df_overall)

    df_rural = dd.read_files_rural()
    top_10_week_with_highest_rate_change_str_rural, top_10_week_with_highest_rate_change_rural = dd.highest_rate_change(
        df_rural)

    df_urban = dd.read_files_urban()
    top_10_week_with_highest_rate_change_str_urban, top_10_week_with_highest_rate_change_urban = dd.highest_rate_change(
        df_urban)

    for i in range(3):
        title_2 = top_10_week_with_highest_rate_change_str_overall[a]
        data = pd.DataFrame(top_10_week_with_highest_rate_change_overall[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.scatter(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data))

        fig.update_layout(title=title_2 + 'overall', width=550, height=400)  # title_1 + '<br>' +

        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 12},
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
        graphs.append(fig)

        title_2 = top_10_week_with_highest_rate_change_str_rural[a]
        data = pd.DataFrame(top_10_week_with_highest_rate_change_rural[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.scatter(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data))

        fig.update_layout(title=title_2 + 'rural areas', width=550, height=400)  # title_1 + '<br>' +

        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 12},
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
        graphs.append(fig)

        title_2 = top_10_week_with_highest_rate_change_str_urban[a]
        data = pd.DataFrame(top_10_week_with_highest_rate_change_urban[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.scatter(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data))

        fig.update_layout(title=title_2 + 'urban areas', width=550, height=400)  # title_1 + '<br>' +

        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 12},
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
        graphs.append(fig)
        a += 1

    return graphs


#graphs = min_emp_unemp_lab_graph()
#for i in graphs:
#    i.show()

def lowest_rate_change_graph():
    graphs = []

    a = 0

    df_overall = dd.read_files_overall()
    top_10_week_with_lowest_rate_change_str_overall, top_10_week_with_lowest_rate_change_overall = dd.lowest_rate_change(
        df_overall)

    df_rural = dd.read_files_rural()
    top_10_week_with_lowest_rate_change_str_rural, top_10_week_with_lowest_rate_change_rural = dd.lowest_rate_change(
        df_rural)

    df_urban = dd.read_files_urban()
    top_10_week_with_lowest_rate_change_str_urban, top_10_week_with_lowest_rate_change_urban = dd.lowest_rate_change(
        df_urban)

    for i in range(3):
        title_2 = top_10_week_with_lowest_rate_change_str_overall[a]
        data = pd.DataFrame(top_10_week_with_lowest_rate_change_overall[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.scatter(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data))

        fig.update_layout(title=title_2 + 'overall', width=550, height=400)  # title_1 + '<br>' +

        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 12},
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
        graphs.append(fig)

        title_2 = top_10_week_with_lowest_rate_change_str_rural[a]
        data = pd.DataFrame(top_10_week_with_lowest_rate_change_rural[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.scatter(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data))

        fig.update_layout(title=title_2 + 'rural areas', width=550, height=400)  # title_1 + '<br>' +

        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 12},
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
        graphs.append(fig)

        title_2 = top_10_week_with_lowest_rate_change_str_urban[a]
        data = pd.DataFrame(top_10_week_with_lowest_rate_change_urban[a])

        # print(title_1,title_2)
        # print(type(data))

        columns = list(data.columns)

        fig = px.scatter(data, x=columns[0], y=columns[1], color_discrete_sequence=['light blue'] * len(data))

        fig.update_layout(title=title_2 + 'urban areas', width=550, height=400)  # title_1 + '<br>' +

        fig.update_layout(  # yaxis_range=[0, 30],
            plot_bgcolor='#3D3C3A',
            paper_bgcolor='#3D3C3A',
            titlefont={
                'color': 'white',
                'size': 12},
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
        graphs.append(fig)
        a += 1

    return graphs


#graphs = min_emp_unemp_lab_graph()
#for i in graphs:
#    i.show()