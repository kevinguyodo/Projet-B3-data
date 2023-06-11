from script.clean_db import CleanDBConnection
from script.initial_db import InitialDBConnection
from script.final_db import FinalDBConnection
import os
import streamlit as st
import altair as alt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

def main():
    clean_db_conn = CleanDBConnection()
    clean_db_conn.get_data_from_csv()

    initial_db_conn = InitialDBConnection()
    initial_db_conn.get_data_from_csv()

    if os.path.exists("data/final_drug.csv"):
        final_db_conn = FinalDBConnection()
        final_db_conn.get_data_from_csv()
        streamlit_interative_plot()


def streamlit_interative_plot():
    final_drug = pd.read_csv("data/final_drug.csv", low_memory=False)
    build_interactive_plot(final_drug)


def build_interactive_plot(final_drug):
    get_condition_unique = final_drug['Condition'].unique()
    # Sélection du dropdown
    my_condition = st.selectbox('Select condition', get_condition_unique)
    # Définir le titre de l'application Streamlit
    st.title(f'Satisfaction level of drug (condition: {my_condition})')
    # create sub dataframe with only 'Satisfaction' column and the drug associated with the Condition asked with Drug satisfaction mean
    test = final_drug.loc[final_drug['Condition']==my_condition, ["Satisfaction", 'Drug']].groupby('Drug').mean().reset_index()
    df = pd.DataFrame(test)
    # Build plot
    fig = px.bar(df, x='Satisfaction', y='Drug', orientation='h')
    st.write(fig)

main()