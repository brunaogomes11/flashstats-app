import streamlit as st
import warnings
import pandas as pd

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import requests
st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")
def last10matches(df_time_home, df_time_away):
    df_time_home.loc[:, 'Resultado'] = df_time_home.apply(lambda row: 'V' if row['FTHG'] > row['FTAG'] else ('D' if row['FTHG'] < row['FTAG'] else 'E'), axis=1)
    df_time_away.loc[:, 'Resultado'] = df_time_away.apply(lambda row: 'D' if row['FTHG'] > row['FTAG'] else ('V' if row['FTHG'] < row['FTAG'] else 'E'), axis=1)
    df_time_home.loc[:, 'Ambos Marcam'] = df_time_home.apply(lambda row: 'S' if row['FTHG'] > 0 and row['FTAG'] > 0 else 'N', axis=1)
    df_time_away.loc[:, 'Ambos Marcam'] = df_time_away.apply(lambda row: 'S' if row['FTHG'] > 0 and row['FTAG'] > 0 else 'N', axis=1)
    df_time_home.loc[:, f'Over 1.5'] = df_time_home.apply(lambda row: 'S' if (row['FTHG']) > 1.5 else 'N', axis=1)
    df_time_away.loc[:, f'Over 1.5'] = df_time_away.apply(lambda row: 'S' if (row['FTAG']) > 1.5 else 'N', axis=1)
    df_time_home.loc[:, f'Over 2.5'] = df_time_home.apply(lambda row: 'S' if (row['FTHG']) > 2.5 else 'N', axis=1)
    df_time_away.loc[:, f'Over 2.5'] = df_time_away.apply(lambda row: 'S' if (row['FTAG']) > 2.5 else 'N', axis=1)
    df_time_home.loc[:, 'Over 1.5 (Ambos)'] = df_time_home.apply(lambda row: 'S' if (row['FTHG'] + row['FTAG']) > 1.5 else 'N', axis=1)
    df_time_away.loc[:, 'Over 1.5 (Ambos)'] = df_time_away.apply(lambda row: 'S' if (row['FTHG'] + row['FTAG']) > 1.5 else 'N', axis=1)
    df_time_home.loc[:, 'Over 2.5 (Ambos)'] = df_time_home.apply(lambda row: 'S' if (row['FTHG'] + row['FTAG']) > 2.5 else 'N', axis=1)
    df_time_away.loc[:, 'Over 2.5 (Ambos)'] = df_time_away.apply(lambda row: 'S' if (row['FTHG'] + row['FTAG']) > 2.5 else 'N', axis=1)
    return pd.concat([df_time_home, df_time_away])

def show_last10matches(df, time, dividir):
    lista_estatistica_resultados = df['Resultado'].head(10).tolist()
    quantidade_resultados = df['Resultado'].head(10).value_counts()
    quantidade_resultados['V'] = 0 if 'V' not in quantidade_resultados else quantidade_resultados['V']
    quantidade_resultados['D'] = 0 if 'D' not in quantidade_resultados else quantidade_resultados['D']
    quantidade_resultados['E'] = 0 if 'E' not in quantidade_resultados else quantidade_resultados['E']
    quantidade_resultados = quantidade_resultados.sort_index()
    lista_estatistica_ambos_marcam = df['Ambos Marcam'].head(10).tolist()
    quantidade_ambos_marcam = df['Ambos Marcam'].head(10).value_counts()
    quantidade_ambos_marcam['S'] = 0 if 'S' not in quantidade_ambos_marcam else quantidade_ambos_marcam['S']
    quantidade_ambos_marcam['N'] = 0 if 'N' not in quantidade_ambos_marcam else quantidade_ambos_marcam['N']
    quantidade_ambos_marcam = quantidade_ambos_marcam.sort_index()
    lista_estatistica_over_1_5 = df[f'Over 1.5'].head(10).tolist()
    quantidade_over_1_5 = df[f'Over 1.5'].head(10).value_counts()
    quantidade_over_1_5['S'] = 0 if 'S' not in quantidade_over_1_5 else quantidade_over_1_5['S']
    quantidade_over_1_5['N'] = 0 if 'N' not in quantidade_over_1_5 else quantidade_over_1_5['N']
    quantidade_over_1_5 = quantidade_over_1_5.sort_index()
    lista_estatistica_over_2_5 = df[f'Over 2.5'].head(10).tolist()
    quantidade_over_2_5 = df[f'Over 2.5'].head(10).value_counts()
    quantidade_over_2_5['S'] = 0 if 'S' not in quantidade_over_2_5 else quantidade_over_2_5['S']
    quantidade_over_2_5['N'] = 0 if 'N' not in quantidade_over_2_5 else quantidade_over_2_5['N']
    quantidade_over_2_5 = quantidade_over_2_5.sort_index()
    lista_estatistica_over_1_5_ambos = df['Over 1.5 (Ambos)'].head(10).tolist()
    quantidade_over_1_5_ambos = df['Over 1.5 (Ambos)'].head(10).value_counts()
    quantidade_over_1_5_ambos['S'] = 0 if 'S' not in quantidade_over_1_5_ambos else quantidade_over_1_5_ambos['S']
    quantidade_over_1_5_ambos['N'] = 0 if 'N' not in quantidade_over_1_5_ambos else quantidade_over_1_5_ambos['N']
    quantidade_over_1_5_ambos = quantidade_over_1_5_ambos.sort_index()
    lista_estatistica_over_2_5_ambos = df['Over 2.5 (Ambos)'].head(10).tolist()
    quantidade_over_2_5_ambos = df['Over 2.5 (Ambos)'].head(10).value_counts()
    quantidade_over_2_5_ambos['S'] = 0 if 'S' not in quantidade_over_2_5_ambos else quantidade_over_2_5_ambos['S']
    quantidade_over_2_5_ambos['N'] = 0 if 'N' not in quantidade_over_2_5_ambos else quantidade_over_2_5_ambos['N']
    quantidade_over_2_5_ambos = quantidade_over_2_5_ambos.sort_index()
    df = df.iloc[:, 2:9].head(10).reset_index(drop=True)
    df.index += 1
    if dividir:
        col1, col2 = st.columns(2)
        col1.write("Mandante x Visitante")       
        for index, row in df.iterrows():
            if row['HomeTeam'] == time:
                col1.write(f"<img src='{row['LogoHome']}' style='width: 20px; height: 20px;'> :blue[{row['HomeTeam']}] {row['FTHG']} x {row['FTAG']} :red[{row['AwayTeam']}] <img src='{row['LogoAway']}' style='width: 20px; height: 20px;'>", unsafe_allow_html=True)
            else:
                col1.write(f"<img src='{row['LogoHome']}' style='width: 20px; height: 20px;'> :red[{row['HomeTeam']}] {row['FTHG']} x {row['FTAG']} :blue[{row['AwayTeam']}] <img src='{row['LogoAway']}' style='width: 20px; height: 20px;'>", unsafe_allow_html=True)
        col2.write(f"Resultado - {(quantidade_resultados[2]/10)*100}%")
        status_partida(col2, lista_estatistica_resultados, df)
        col2.write(f"Ambos Marcam - {(quantidade_ambos_marcam[1]/10)*100}%")
        status_partida(col2, lista_estatistica_ambos_marcam, df)
        col2.write(f"Mais de 1.5 gols {time} - {(quantidade_over_1_5[1]/10)*100}%")
        status_partida(col2, lista_estatistica_over_1_5, df)
        col2.write(f"Mais de 2.5 gols {time} - {(quantidade_over_2_5[1]/10)*100}%")
        status_partida(col2, lista_estatistica_over_2_5, df)
        col2.write(f"Mais de 1.5 gols (Na Partida) - {(quantidade_over_1_5_ambos[1]/10)*100}%")
        status_partida(col2, lista_estatistica_over_1_5_ambos, df)
        col2.write(f"Mais de 2.5 gols (Na Partida) - {(quantidade_over_2_5_ambos[1]/10)*100}%")
        status_partida(col2, lista_estatistica_over_2_5_ambos, df)
    else:
        st.write("Mandante x Visitante")
        for index, row in df.iterrows():
            if row['HomeTeam'] == time:
                st.write(f"<img src='{row['LogoHome']}' style='width: 20px; height: 20px;'> :blue[{row['HomeTeam']}] {row['FTHG']} x {row['FTAG']} :red[{row['AwayTeam']}] <img src='{row['LogoAway']}' style='width: 20px; height: 20px;'>", unsafe_allow_html=True)
            else:
                st.write(f"<img src='{row['LogoHome']}' style='width: 20px; height: 20px;'> :red[{row['HomeTeam']}] {row['FTHG']} x {row['FTAG']} :blue[{row['AwayTeam']}] <img src='{row['LogoAway']}' style='width: 20px; height: 20px;'>", unsafe_allow_html=True)
        st.write(f"Resultado - {(quantidade_resultados[2]/10)*100}%")
        status_partida(st, lista_estatistica_resultados, df)
        st.write(f"Ambos Marcam - {(quantidade_ambos_marcam[1]/10)*100}%")
        status_partida(st, lista_estatistica_ambos_marcam, df)
        st.write(f"Mais de 1.5 gols {time} - {(quantidade_over_1_5[1]/10)*100}%")
        status_partida(st, lista_estatistica_over_1_5, df)
        st.write(f"Mais de 2.5 gols {time} - {(quantidade_over_2_5[1]/10)*100}%")
        status_partida(st, lista_estatistica_over_2_5, df)
        st.write(f"Mais de 1.5 gols (Na Partida) - {(quantidade_over_1_5_ambos[1]/10)*100}%")
        status_partida(st, lista_estatistica_over_1_5_ambos, df)
        st.write(f"Mais de 2.5 gols (Na Partida) - {(quantidade_over_2_5_ambos[1]/10)*100}%")
        status_partida(st, lista_estatistica_over_2_5_ambos, df)

def dashboard_gols(df):
    try:
        df['FTHG'] = df['FTHG'].astype(int)
        df['FTAG'] = df['FTAG'].astype(int)
        df['GAHT'] = df['GAHT'].astype(int)
        df['GAAT'] = df['GAAT'].astype(int)
        gols_times_casa = df.groupby('HomeTeam')['FTHG'].sum()
        gols_times_visitante = df.groupby('AwayTeam')['FTAG'].sum()
        total_gols = gols_times_casa + gols_times_visitante
        finalizacoes_times_casa = df.groupby('HomeTeam')['GAHT'].sum()
        finalizacoes_times_visitante = df.groupby('AwayTeam')['GAAT'].sum()
        finalizacoes_times = finalizacoes_times_casa + finalizacoes_times_visitante
        gols_times = pd.concat([gols_times_casa, gols_times_visitante, total_gols, finalizacoes_times_casa, finalizacoes_times_visitante, finalizacoes_times], axis=1)
        gols_times.columns = ['Gols Casa', 'Gols Visitante', 'Total Gols', 'Total Finalizações Casa', 'Total Finalizações Visitante', 'Total Finalizações']
        gols_times.index.name = 'Times'
        colunas = st.multiselect(
            "Quais colunas deseja mostrar no gráfico?",
            [x for x in gols_times.columns],
            [gols_times.columns[0], gols_times.columns[1], gols_times.columns[2]])
        #A
        df_to_show = gols_times[colunas]
        st.bar_chart(df_to_show)
        st.dataframe(df_to_show)
    except Exception as e:
        st.error(f"Deu erro: {e}")

def status_partida(localizacao, array_jogos_resultado, array_jogos):
    # Definindo os quadrados coloridos com letras
    array_jogos = array_jogos[['HomeTeam', 'FTHG', 'FTAG', 'AwayTeam']]
    array_jogos = array_jogos.reset_index(drop=True)
    elementos = []
    for index, resultado in enumerate(array_jogos_resultado):
        if resultado == 'V':
            elementos.append(f'<div style="font-size: 1rem; user-select: none; border-radius:5px; background-color: green; color: white; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center; margin: 0 5px;" title="{array_jogos["HomeTeam"][index]} {array_jogos["FTHG"][index]} x {array_jogos["FTAG"][index]} {array_jogos["AwayTeam"][index]}">V</div>')
        elif resultado == 'D':
            elementos.append(f'<div style="font-size: 1rem; user-select: none; border-radius:5px; background-color: red; color: white; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center; margin: 0 5px;" title="{array_jogos["HomeTeam"][index]} {array_jogos["FTHG"][index]} x {array_jogos["FTAG"][index]} {array_jogos["AwayTeam"][index]}">D</div>')
        elif resultado == 'E':
            elementos.append(f'<div style="font-size: 1rem; user-select: none; border-radius:5px; background-color: yellow; color: black; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center; margin: 0 5px;" title="{array_jogos["HomeTeam"][index]} {array_jogos["FTHG"][index]} x {array_jogos["FTAG"][index]} {array_jogos["AwayTeam"][index]}">E</div>')
        elif resultado == 'S':
            elementos.append(f'<div style="font-size: 1rem; user-select: none; border-radius:5px; background-color: green; color: white; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center; margin: 0 5px;" title="{array_jogos["HomeTeam"][index]} {array_jogos["FTHG"][index]} x {array_jogos["FTAG"][index]} {array_jogos["AwayTeam"][index]}">S</div>')
        elif resultado == 'N':
            elementos.append(f'<div style="font-size: 1rem; user-select: none; border-radius:5px; background-color: red; color: white; width: 20px; height: 20px; display: flex; justify-content: center; align-items: center; margin: 0 5px;" title="{array_jogos["HomeTeam"][index]} {array_jogos["FTHG"][index]} x {array_jogos["FTAG"][index]} {array_jogos["AwayTeam"][index]}">N</div>')

    status_html = f"""
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 5px;">
        {''.join(elementos)}
    </div>
    """
    localizacao.markdown(status_html, unsafe_allow_html=True)


def dashboard_est_time(df):
    df['FTHG'] = df['FTHG'].astype(int)
    df['FTAG'] = df['FTAG'].astype(int)
    nome_times = df['HomeTeam'].unique() 
    col1_select, col2_select = st.columns([3, 1])
    time_selecionado = col1_select.selectbox('Selecione o time', nome_times)
    logoTime = df[df['HomeTeam'] == time_selecionado]['LogoHome'].iloc[0]
    col2_select.write(f"<img src='{logoTime}' style='width: auto;'>", unsafe_allow_html=True)
    df_time_home = df[df['HomeTeam'] == time_selecionado]
    df_time_away = df[df['AwayTeam'] == time_selecionado]
    estatistica_desejada = st.selectbox('Selecione a estatística desejada', 
                                          ['Gols', 'Últimos 10 jogos'])
    df_estatistica = pd.DataFrame()
    if estatistica_desejada == "Gols":
        df_estatistica.loc[0, 'Gols feitos em jogos dentro de casa'] = df_time_home['FTHG'].sum()
        df_estatistica.loc[0, 'Gols feitos em jogos fora de casa'] = df_time_away['FTAG'].sum()
        df_estatistica.loc[0, 'Gols feitos'] = df_time_home['FTHG'].sum() + df_time_away['FTAG'].sum()
        df_estatistica.loc[0, 'Gols sofridos em jogos dentro de casa'] = df_time_home['FTAG'].sum()
        df_estatistica.loc[0, 'Gols sofridos em jogos fora de casa'] = df_time_away['FTHG'].sum()
        df_estatistica.loc[0, 'Gols sofridos'] = df_time_home['FTAG'].sum() + df_time_away['FTHG'].sum()
        df_estatistica = df_estatistica.T
        df_estatistica.columns = ['Quantidade']
        st.dataframe(df_estatistica)
    elif estatistica_desejada == 'Últimos 10 jogos':
        df_estatistica = last10matches(df_time_home, df_time_away)
        df_estatistica['Date'] = pd.to_datetime(df_estatistica['Date'], format='%d.%m.%Y').dt.date
        df_estatistica = df_estatistica.sort_values(by='Date', ascending=False)
        show_last10matches(df_estatistica, time_selecionado, True)        
        
def dashboard_next_rounds(json, df):
    jogos = [f"{x['home']} x {x['away']}" for x in json]
    jogo_desejado = st.selectbox("Selecione o jogo desejado", jogos)
    home_team = jogo_desejado.split(' x ')[0]
    away_team = jogo_desejado.split(' x ')[1]
    df_home_time_in_home = df[df['HomeTeam'] == home_team]
    df_home_time_in_away = df[df['AwayTeam'] == home_team]
    df_away_time_in_home = df[df['HomeTeam'] == away_team]
    df_away_time_in_away = df[df['AwayTeam'] == away_team]
    df_estatistica1 = last10matches(df_home_time_in_home, df_home_time_in_away)
    df_estatistica1['Date'] = pd.to_datetime(df_estatistica1['Date'], format='%d.%m.%Y').dt.date
    df_estatistica1 = df_estatistica1.sort_values(by='Date', ascending=False)
    df_estatistica2 = last10matches(df_away_time_in_home, df_away_time_in_away)

    df_estatistica2['Date'] = pd.to_datetime(df_estatistica2['Date'], format='%d.%m.%Y').dt.date
    df_estatistica2 = df_estatistica2.sort_values(by='Date', ascending=False)
    
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        show_last10matches(df_estatistica1, home_team, False)
    with coluna2:
        show_last10matches(df_estatistica2, away_team, False)

def tab_pane():
    datasets_disponiveis = requests.get('http://127.168.0.1:3001/listar_datasets').json()
    torneios = [f'{torneio['country']} - {torneio['tournament']} - {torneio['season']} - {torneio['time']}' for torneio in datasets_disponiveis]
    selecao_torneio = st.selectbox("Selecione o torneio desejado", torneios)
    torneio_selecionado = next(torneio['id'] for torneio in datasets_disponiveis if f"{torneio['country']} - {torneio['tournament']} - {torneio['season']} - {torneio['time']}" == selecao_torneio)
    json_torneio = requests.get(f'http://127.168.0.1:3001/listar_dados/{torneio_selecionado}').json()
    df = pd.DataFrame(json_torneio)
    tab1, tab2, tab3 = st.tabs(["Gols Totais", "Estatistica por Time", 'Próximas Partidas'])
    with tab1:
        dashboard_gols(df)
    with tab2:
        dashboard_est_time(df)
    with tab3:
        # try:
            dividir_torneio_nome = selecao_torneio.split(' - ')
            json_next_rounds = requests.get(f'http://127.168.0.1:3001/next_rounds/{dividir_torneio_nome[0]}/{dividir_torneio_nome[1]}/{dividir_torneio_nome[2]}').json()
            dashboard_next_rounds(json_next_rounds, df)
        # except:
        #     st.write("Erro ao carregar os dados dos próximos jogos")
        
tab_pane()