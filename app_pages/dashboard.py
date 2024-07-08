import streamlit as st
import pandas as pd
import numpy as np
import requests

def dashboard_gols():
    try:
        json_brasileirao = requests.get('http://127.0.0.1:3001/listar_dados/668aa404e2197a8612177b99').json()
        df = pd.DataFrame(json_brasileirao)
        df['FTHG'] = df['FTHG'].astype(int)
        df['FTAG'] = df['FTAG'].astype(int)
        gols_times_casa = df.groupby('HomeTeam')['FTHG'].sum()
        gols_times_visitante = df.groupby('AwayTeam')['FTAG'].sum()
        total_gols = gols_times_casa + gols_times_visitante
        gols_times = pd.concat([gols_times_casa, gols_times_visitante, total_gols], axis=1)
        gols_times.columns = ['Gols Casa', 'Gols Visitante', 'Total Gols']
        gols_times.index.name = 'Times'
        colunas = st.multiselect(
            "Quais colunas deseja mostrar no dataframe?",
            [x for x in gols_times.columns],
            [gols_times.columns[0], gols_times.columns[1], gols_times.columns[2]])
        df_to_show = gols_times[colunas]
        st.bar_chart(df_to_show)
    except Exception as e:
        st.error(f"Deu erro: {e}")

def dashboard_est_time():
    json_brasileirao = requests.get('http://127.0.0.1:3001/listar_dados/668aa404e2197a8612177b99').json()
    df = pd.DataFrame(json_brasileirao)
    df['FTHG'] = df['FTHG'].astype(int)
    df['FTAG'] = df['FTAG'].astype(int)
    nome_times = df['HomeTeam'].unique()
    time_selecionado = st.selectbox('Selecione o time', nome_times)
    df_time_home = df[df['HomeTeam'] == time_selecionado]
    df_time_away = df[df['AwayTeam'] == time_selecionado]
    estatistica_desejada = st.selectbox('Selecione a estatística desejada', 
                                          ['Gols'])
    df_estatistica = pd.DataFrame()
    if estatistica_desejada == "Gols":
        df_estatistica.loc[0, 'Gols feitos em jogos dentro de casa'] = df_time_home['FTHG'].sum()
        df_estatistica.loc[0, 'Gols feitos em jogos fora de casa'] = df_time_away['FTAG'].sum()
        df_estatistica.loc[0, 'Gols feitos'] = df_time_home['FTHG'].sum() + df_time_away['FTAG'].sum()
        df_estatistica.loc[0, 'Gols sofridos em jogos dentro de casa'] = df_time_home['FTAG'].sum()
        df_estatistica.loc[0, 'Gols sofridos em jogos fora de casa'] = df_time_away['FTHG'].sum()
        df_estatistica.loc[0, 'Gols sofridos'] = df_time_home['FTAG'].sum() + df_time_away['FTHG'].sum()
    st.dataframe(df_estatistica.T.set_index(False))
def tab_pane():
    tab1, tab2 = st.tabs(["Gols Totais", "Estatistica por Time"])
    with tab1:
        dashboard_gols()
    with tab2:
        dashboard_est_time()

tab_pane()