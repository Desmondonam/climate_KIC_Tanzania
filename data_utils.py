# Import libraries
import pandas as pd
import numpy as np
import streamlit as st

# Load teh data
@st.cache_data
def load_data():
    """
    Generate or load the data for climate
    in real real world application you woul load the data from csv or an API instead of generating data

    """
    # Create dates for years of monthly temperatures averages
    dates = pd.date_range(start = "2010-01-01", end = "2024-12-31", freq = "M")

    # Generate the synthetic temperatures 
    temps = []
    for i in range(len(dates)):
        # Base temp wht seasonal pattern 
        seasonal = 15 + 10 * np.sin(2 * np.pi * i / 12)
        # add some upward trend
        trend = 0.03 * i
        # Add some random noise
        noise = np.random.normal(0, 1.5)
        temps.append(seasonal + trend + noise)

    # Create df
    df = pd.DataFrame({
        "dates" : dates,
        "temperature" : temps
    })

    # Extract the features
    df['year'] = df['dates'].dt.year
    df['month'] = df['dates'].dt.month
    df['day'] = df['dates'].dt.day

    return df

def prepare_features(df):
    """
    prepare the features for model training
    """
    X = df[['year', 'month']].values
    y = df['temperature'].values
    return X, y
