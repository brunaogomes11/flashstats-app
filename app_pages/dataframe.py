import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Dataframe", page_icon="📈")
try:
    datasets_disponiveis = requests.get('http://127.0.0.1:3001/listar_datasets').json()
    torneios = [f'{torneio['country']} - {torneio['tournament']} - {torneio['time']}' for torneio in datasets_disponiveis]
    torneio_selecionado = st.selectbox("Selecione o torneio desejado", torneios)
    json_brasileirao = requests.get(f'http://127.0.0.1:3001/listar_dados/668aa404e2197a8612177b99').json()
    df = pd.DataFrame(json_brasileirao)
    colunas = st.multiselect(
        "Quais colunas deseja mostrar no dataframe?",
        [x for x in df.columns],
        [df.columns[1], df.columns[3], df.columns[4]])
    df_to_show = df[colunas]
    st.dataframe(df_to_show, height=500)
except Exception as e:
    st.error(f"Deu erro: {e}")