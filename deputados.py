import streamlit as st
import pandas as pd

# Configuração da página (opcional)
st.set_page_config(page_title="Consulta Deputados 2022", layout="wide")

st.title('Deputados Federais - 2022')

st.image('https://www.rbsdirect.com.br/filestore/0/2/5/0/7/1/5_f03f083dd1c7353/5170520_d6f99c6fd82cd20.jpg?version=1575255600')

# Carregar os dados
# Certifique-se que o arquivo 'deputados_2022.csv' está na mesma pasta do script
df = pd.read_csv('deputados_2022.csv')

# --- CRIAÇÃO DOS FILTROS ---
st.sidebar.header("Filtros de Pesquisa")

# 1. Filtro de Estado (UF)
estados = ['Todos'] + sorted(list(df['siglaUf'].unique()))
estado_selecionado = st.sidebar.selectbox('Selecione o Estado (UF):', estados)

# 2. Filtro de Partido Político
partidos = ['Todos'] + sorted(list(df['siglaPartido'].unique()))
partido_selecionado = st.sidebar.selectbox('Selecione o Partido:', partidos)

# --- APLICAÇÃO DA LÓGICA DE FILTRO ---
df_filtrado = df.copy()

if estado_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['siglaUf'] == estado_selecionado]

if partido_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['siglaPartido'] == partido_selecionado]

# --- EXIBIÇÃO DOS RESULTADOS ---
st.subheader(f"Resultados: {estado_selecionado} / {partido_selecionado}")

# Métrica simples para mostrar quantos deputados foram encontrados
st.metric("Total de Deputados encontrados", len(df_filtrado))

st.dataframe(df_filtrado, use_container_width=True)


