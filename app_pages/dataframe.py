import streamlit as st
import warnings
import pandas as pd

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import requests

st.set_page_config(page_title="Dataframe", page_icon="📈")
try:
    datasets_disponiveis = requests.get('http://127.0.0.1:3001/listar_datasets').json()
    torneios = [f'{torneio['country']} - {torneio['tournament']} - {torneio['time']}' for torneio in datasets_disponiveis]
    selecao_torneio = st.selectbox("Selecione o torneio desejado", torneios)
    torneio_selecionado = next(torneio['id'] for torneio in datasets_disponiveis if f"{torneio['country']} - {torneio['tournament']} - {torneio['time']}" == selecao_torneio)
    json_torneio = requests.get(f'http://127.0.0.1:3001/listar_dados/{torneio_selecionado}').json()
    df = pd.DataFrame(json_torneio)
    colunas = st.multiselect(
        "Quais colunas deseja mostrar no dataframe?",
        [x for x in df.columns],
        [df.columns[1], df.columns[3], df.columns[4]])
    df_to_show = df[colunas]
    st.dataframe(df_to_show, height=500)
except Exception as e:
    st.error(f"Deu erro: {e}")