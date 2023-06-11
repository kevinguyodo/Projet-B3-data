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




def jupyternotebook():
    final_drug = pd.read_csv("data/final_drug.csv", low_memory=False)
    drop_down(final_drug)


def drop_down(final_drug):
    get_condition_unique = final_drug['Condition'].unique()

    # Sélection du dropdown
    my_condition = st.selectbox('Select condition', get_condition_unique)

    # Définir le titre de l'application Streamlit
    st.title(f'Satisfaction level of drug (condition: {my_condition})')

    # Selection
    test = final_drug.loc[final_drug['Condition']==my_condition, ["Satisfaction", 'Drug']].groupby('Drug').mean().reset_index()

    df = pd.DataFrame(test)
    fig = px.bar(df, x='Satisfaction', y='Drug', orientation='h')
    st.write(fig)
# main()


jupyternotebook()