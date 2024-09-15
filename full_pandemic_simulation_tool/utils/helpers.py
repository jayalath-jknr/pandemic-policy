
# utils/helpers.py

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data(file_path):
    return pd.read_csv(file_path)

def save_results(results, file_path):
    results.to_csv(file_path, index=False)

def plot_results(results):
    st.line_chart(results[['Infected', 'Recovered']])
