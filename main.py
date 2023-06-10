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



    get_chart_98185()

def drop_down(final_drug):
    get_condition_unique = final_drug['Condition'].unique()

    # Définir le titre de l'application Streamlit
    st.title('Menu déroulant des maladies')


    # Sélection du dropdown
    my_condition = st.selectbox('Sélectionnez une maladie', get_condition_unique)

    st.write(my_condition)

    test = final_drug.loc[final_drug['Condition']==my_condition, ["Satisfaction", 'Drug']]

    st.write("Satisfaction moyenne : " + str(test.loc[test['Drug'] == 'Crotamiton', 'Satisfaction'].mean()))

    # test.groupby('Satisfaction').unique()

    print(test.agg(['mean']))

    # satisfaction_mean = test.groupby('Satisfaction')['Drug'].mean()
    # print(satisfaction_mean)
    df = pd.DataFrame(test)
    fig = px.bar(df, x='Satisfaction', y='Drug', orientation='h')
    st.write(fig)


def get_chart_98185():
    # Créer un exemple de DataFrame avec des données numériques
    data = {
        'Groupe 1': np.random.normal(0, 1, 100),
        'Groupe 2': np.random.normal(2, 1, 100),
        'Groupe 3': np.random.normal(5, 1, 100),
    }

    df = pd.DataFrame(data)

    # Définir le titre de l'application Streamlit
    st.title('Ridgeline Plot avec des nombres')

    # Afficher le DataFrame
    st.subheader('Données')
    st.write(df)

    # Melt le DataFrame pour le rendre compatible avec Seaborn
    melted_df = df.melt(var_name='Groupe', value_name='Valeur')

    # Créer le ridgeline plot avec Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))

    # Dessiner le ridgeline plot
    sns.kdeplot(data=melted_df, x='Valeur', hue='Groupe', fill=True, palette='husl', linewidth=1.5, ax=ax)

    # Configurer les axes et les étiquettes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)
    plt.xlabel('Valeur', labelpad=15, fontsize=12, color='#333333')
    plt.ylabel('Densité', labelpad=15, fontsize=12, color='#333333')

    # Afficher le ridgeline plot dans Streamlit
    st.subheader('Ridgeline Plot')
    st.pyplot(fig)

# main()


jupyternotebook()