import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_time_series(df):
    """
    Plot the temperatures over time
    """
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.plot(df['dates'], df['temperature'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperatures in C")
    ax.set_title("Monthly Average Temperatures")
    ax.grid(True)
    return fig

def plot_seasonal_patterns(df):
    """
    Plot the monthly temperature distributions
    """
    fig, ax = plt.subplots(figsize = (10, 6))
    sns.boxplot(x = 'month', y = 'temperature', data = df, ax = ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperatures in C")
    ax.set_title("Monthly Temperature Distributions")
    return fig


def plot_yearly_trends(df):
    """
    plot the yearly average temperatures
    """
    year_avg = df.groupby('year')['temperature'].mean().reset_index()
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.plot(year_avg['year'], year_avg['temperature'], marker = 'o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperatures in C")
    ax.set_title("Yearly Average Temperatures")
    ax.grid(True)
    return fig

def plot_actual_vs_predicted(y_test, y_pred):
    """
    Plot the actual vs predicted values
    """
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.scatter(y_test, y_pred, alpha = 0.7)
    ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
    ax.set_xlabel("Actual Temperature")
    ax.set_ylabel("Predicted Temperature")
    ax.set_title("Actual VS Predicted Temperatures")
    return fig

def plot_prediction_context(hist_temps, pred_year, pred_month, prediction):
    """
    Plot the prediction in historical context
    """
    years_hist, temp_hist = zip(*hist_temps)

    fig, ax = plt.subplots(figsize = (10, 6))
    # Plot the historical data for that month
    ax.scatter(years_hist, temp_hist, label = f"Historical (Month {pred_month})", color = 'blue')
    ax.plot(years_hist, temp_hist, 'b--', alpha = 0.6)

    # Pllot the prediction
    ax.scatter([pred_year], [prediction], color = 'red', s = 100, label = 'Prediction')
    # Add a trend line
    z = np.polyfit(years_hist, temp_hist, 1)
    p = np.poly1d(z)
    ax.plot(range(2010, pred_year+1), p(range(2010, pred_year + 1)), 'g-', label = 'Trend')
    ax.set_xlabel("Year")
    ax.set_ylabel(f"Temperatures for month {pred_month} in C")
    ax.set_title("Histprical Context")
    ax.legend()
    ax.grid(True)
    return fig  
