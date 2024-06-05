from dash import html
from dash import dcc

correlation_interpretation = """The observed relationship between the estimated labor participation rate and the estimated unemployment rate indicates a statistically significant negative correlation. This negative correlation implies that, on average, as the unemployment rate increases, there is a tendency for the labor participation rate to decrease, and conversely, as the unemployment rate decreases, there is a tendency for the labor participation rate to increase. The strength of this negative correlation is quantified using the Pearson correlation coefficient, which provides a measure of the linear relationship between these two variables."""

std_deviation_interpretation = """It serves as a measure of volatility, with a higher value suggesting greater variability. A small proportion relative to the mean indicates lower variability, while a larger proportion may signify higher variability."""

insights_std_labour = """
1. Labour Participation Rates: The standard deviation of 2.562 in overall weekly labour participation rates, 2.53 in rural areas, and 2.855 in urban areas, indicates variability around the average rate. This suggests that the labour participation rate fluctuates from week to week, with urban areas showing slightly more variability than rural areas.
"""

insights_std_unemp = """
2. Unemployment Rates: The standard deviation of 3.639 in overall weekly unemployment rates, 3.615 in rural areas, and 4.017 in urban areas, shows that there is a higher degree of fluctuation in unemployment rates compared to labour participation rates. Again, urban areas exhibit more variability, indicating that urban unemployment rates are more volatile.
"""
insights_std_emp = """
3. Employment Estimates: The standard deviation of 23,297,565.977 in overall weekly employment, 15,905,542.737 in rural areas, and 8,355,138.827 in urban areas, demonstrates a significant amount of variation in employment numbers. This suggests that the number of people employed can change dramatically from week to week.
"""

insights_std_sum = """
In summary, these statistics highlight the dynamic nature of the labor market, with significant week-to-week variations in labour participation, unemployment rates, and employment numbers.This variability is something your clients should be aware of when making decisions or forecasts based on labor market trends.
"""

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

lag_analysis_description = (
        "Lag analysis involves examining how changes in one variable (Variable A) are related to changes in another variable (Variable B) at different time points. "
        "In simpler terms, it helps us identify patterns where a change in Variable A today is followed by a change in Variable B after some time has passed. "
        "\nFor instance, consider unemployment rates (Variable A) and economic growth (Variable B). Lag analysis would help us determine if an increase in unemployment today tends to be followed by a decrease in Labour participation in the next few months, or vice versa. "
        "\nBy studying these relationships over time, we can pinpoint potential leading or lagging indicators. A leading indicator suggests that changes in Variable A precede changes in Variable B, providing an early signal. "
        "\nConversely, a lagging indicator indicates that changes in Variable A follow changes in Variable B. "
        "\nHigh correlations at specific lags may indicate meaningful relationships between the variables at those time points."
    )

layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "RESEARCH OUTCOMES", style={"color": "#fefefe",
                               "font-size": "30px",
                               'text-align':'center',}
            ),
        ], className='home_bg ten columns')
    ], className='home_row row'),
    html.Div([
        html.H2("CORRELATION INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(correlation_interpretation, style={"text-align": "justify","color": "white"}),
        html.H2("STANDARD DEVIATION INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(std_deviation_interpretation, style={"text-align": "justify","color": "white"}),
        html.P(insights_std_labour, style={"text-align": "justify","color": "white"}),
        html.P(insights_std_unemp, style={"text-align": "justify","color": "white"}),
        html.P(insights_std_emp, style={"text-align": "justify","color": "white"}),
        html.P(insights_std_sum, style={"text-align": "justify","color": "white"}),
        html.H2("ORIGINAL SERIES INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(original_series_description, style={"text-align": "justify","color": "white"}),
        html.H2("TREND INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(trend_description, style={"text-align": "justify","color": "white"}),
        html.H2("SEASONALITY INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(seasonality_description, style={"text-align": "justify","color": "white"}),
        html.H2("RESIDUALS INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(residuals_description, style={"text-align": "justify","color": "white"}),
        html.H2("LAG ANALYSIS INTERPRATION", style={"color": "#0084d6","text-align": "center"}),
        html.P(lag_analysis_description, style={"text-align": "justify","color": "white"}),
    ], style={"padding": "1em"})
], style={"font-family": "Arial, sans-serif","margin": "auto", "width": "85%", "padding": "10px"}
)