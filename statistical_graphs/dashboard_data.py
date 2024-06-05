import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import seaborn as sns
import plotly.graph_objects as go


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


def max_emp_unemp_lab(df):
    # df = read_files_overall()

    columns = ['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']

    max_week = []
    top_10_weeks_str = []
    top_10_weeks_data = []

    for i in columns:
        max_finder = df.loc[df[str(i)].idxmax()]
        max_finder_week_date = pd.to_datetime(max_finder['Date'], format='%d-%m-%Y').date()
        max_finder_count = max_finder[str(i)]

        max_employed_week = f"Highest " + i.lower() + " week " + str(max_finder_week_date) + " with " + str(max_finder_count)

        sorted_df = df.sort_values(by=i, ascending=False)

        # Get the top 10 weeks
        top_10_weeks = sorted_df.head(10)

        top_10_weeks = pd.DataFrame(top_10_weeks[['Date', str(i)]])
        top_10_weeks_overall = top_10_weeks.reset_index(drop=True)

        top_10_weeks_overall_str = "Top 10 weeks " + i.lower() + " : "

        max_week.append(max_employed_week)
        top_10_weeks_str.append(top_10_weeks_overall_str)
        top_10_weeks_data.append(top_10_weeks_overall)
        # print(data)
    # print(top_20_weeks_overall)

    # return max_employed_week,top_20_weeks_overall_str,top_20_weeks_overall

    return max_week, top_10_weeks_str, top_10_weeks_data


def min_emp_unemp_lab(df):
    df = read_files_overall()

    columns = ['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']

    min_week = []
    low_10_weeks_str = []
    low_10_weeks_data = []

    for i in columns:
        min_finder = df.loc[df[str(i)].idxmin()]
        min_finder_week_date = pd.to_datetime(min_finder['Date'], format='%d-%m-%Y').date()
        min_finder_count = min_finder[str(i)]

        min_employed_week = f"The week with the lowes number of " + i.lower() + " is on a week starting from" + str(
            min_finder_week_date) + " with " + str(min_finder_count) + " %."

        sorted_df = df.sort_values(by=i)

        # Get the low 10 weeks
        low_10_weeks = sorted_df.head(10)

        low_10_weeks = pd.DataFrame(low_10_weeks[['Date', str(i)]])
        low_10_weeks_overall = low_10_weeks.reset_index(drop=True)

        low_10_weeks_overall_str = "10 weeks with the lowest " + i.lower() + " : "

        min_week.append(min_employed_week)
        low_10_weeks_str.append(low_10_weeks_overall_str)
        low_10_weeks_data.append(low_10_weeks_overall)
        # print(data)
    # print(low_10_weeks_overall)

    # return min_employed_week,low_10_weeks_overall_str,low_10_weeks_overall

    return min_week, low_10_weeks_str, low_10_weeks_data


def highest_rate_change(df):
    # print(df.head())
    # Remove leading and trailing spaces from the 'Date' column

    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    # df.sort_values(by='Date', inplace=True)
    columns_1 = ['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']
    columns_2 = ['Unemployment Rate Change', 'Employed Rate Change', 'Labour Participation Rate Change']
    week_with_highest_rate_change_str = []
    week_with_highest_rate_change = []
    top_10_week_with_highest_rate_change_str = []
    top_10_week_with_highest_rate_change = []

    for i in range(len(columns_1)):
        # Calculate the weekly percentage change in the unemployment rate
        df[columns_2[i]] = df[columns_1[i]].pct_change() * 100

        # print(df.head())

        df.dropna(subset=[columns_2[i]], inplace=True)

        # Find the week with the highest unemployment rate change
        max_change_week = df.loc[df[columns_2[i]].idxmax()]

        # Find the top 10 weeks with the highest increase in unemployment rate change
        top_increase_weeks = df.nlargest(10, columns_2[i])
        top_increase_weeks = top_increase_weeks.reset_index(drop=True)

        week_with_highest_rate_change_str.append("Week with the highest " + columns_2[i] + " :")
        week_with_highest_rate_change.append(max_change_week[['Date', columns_2[i]]])
        top_10_week_with_highest_rate_change_str.append(
            "Top 10 weeks with the highest increase in " + columns_2[i].lower() + " : ")
        top_10_week_with_highest_rate_change.append(top_increase_weeks[['Date', columns_2[i]]])

    return top_10_week_with_highest_rate_change_str, top_10_week_with_highest_rate_change

# df_overall = read_files_overall()
# top_10_week_with_highest_rate_change_str_overall,top_10_week_with_highest_rate_change_overall = highest_rate_change(df_overall)
# df_rural = read_files_rural()
# top_10_week_with_highest_rate_change_str_rural,top_10_week_with_highest_rate_change_rural = highest_rate_change(df_rural)
# df_urban = read_files_urban()
# top_10_week_with_highest_rate_change_str_urban,top_10_week_with_highest_rate_change_urban = highest_rate_change(df_urban)
# print(top_10_week_with_highest_rate_change_str_overall,top_10_week_with_highest_rate_change_overall)

def lowest_rate_change(df):
    # print(df.head())
    # Remove leading and trailing spaces from the 'Date' column

    df['Date'] = df['Date'].str.strip()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by the 'Date' column
    # df.sort_values(by='Date', inplace=True)
    columns_1 = ['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']
    columns_2 = ['Unemployment Rate Change', 'Employed Rate Change', 'Labour Participation Rate Change']
    week_with_lowest_rate_change_str = []
    week_with_lowest_rate_change = []
    top_10_week_with_lowest_rate_change_str = []
    top_10_week_with_lowest_rate_change = []

    for i in range(len(columns_1)):
        # Calculate the weekly percentage change in the unemployment rate
        df[columns_2[i]] = df[columns_1[i]].pct_change() * 100

        # print(df.head())

        df.dropna(subset=[columns_2[i]], inplace=True)

        # Find the week with the lowest unemployment rate change
        max_change_week = df.loc[df[columns_2[i]].idxmin()]

        # Find the top 10 weeks with the lowest increase in unemployment rate change
        top_decrease_weeks = df.nsmallest(10, columns_2[i])

        week_with_lowest_rate_change_str.append("Week with the highest decrease " + columns_2[i] + " :")
        week_with_lowest_rate_change.append(max_change_week[['Date', columns_2[i]]])
        top_10_week_with_lowest_rate_change_str.append(
            "Top 10 weeks with the highest decrease in " + columns_2[i].lower() + " : ")
        top_10_week_with_lowest_rate_change.append(top_decrease_weeks[['Date', columns_2[i]]])

    return top_10_week_with_lowest_rate_change_str, top_10_week_with_lowest_rate_change

# df_overall = read_files_overall()
# top_10_week_with_lowest_rate_change_str_overall,top_10_week_with_lowest_rate_change_overall = lowest_rate_change(df_overall)
# df_rural = read_files_rural()
# top_10_week_with_lowest_rate_change_str_rural,top_10_week_with_lowest_rate_change_rural = lowest_rate_change(df_rural)
# df_urban = read_files_urban()
# top_10_week_with_lowest_rate_change_str_urban,top_10_week_with_lowest_rate_change_urban = lowest_rate_change(df_urban)
# print(top_10_week_with_lowest_rate_change_str_overall,top_10_week_with_lowest_rate_change_overall)
