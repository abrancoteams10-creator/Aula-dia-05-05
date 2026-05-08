import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Deputados 2022", layout="wide")

st.title("🏛️ Explorador de Deputados 2022")

@st.cache_data
def load_data():
    try:
        # Tentativa 1: UTF-8 (Padrão moderno)
        return pd.read_csv('deputados_2022.csv', encoding='utf-8')
    except UnicodeDecodeError:
        # Tentativa 2: Latin-1 (Comum em arquivos Excel/Windows brasileiros)
        return pd.read_csv('deputados_2022.csv', encoding='latin1')

try:
    df = load_data()

    # --- CORREÇÃO DE COLUNA ---
    # Caso a coluna não se chame exatamente 'siglaUf', ajustamos aqui:
    coluna_uf = 'siglaUf' if 'siglaUf' in df.columns else df.columns[1] # Pega a 2ª coluna se não achar o nome

    # Filtro na Barra Lateral
    st.sidebar.header("Configurações")
    estados = sorted(df[coluna_uf].dropna().unique())
    estado_selecionado = st.sidebar.selectbox("Selecione o Estado:", ["Todos"] + estados)

    # Lógica de Filtragem
    if estado_selecionado != "Todos":
        df_filtrado = df[df[coluna_uf] == estado_selecionado]
    else:
        df_filtrado = df

    # Exibição de Resultados
    st.metric("Total de Deputados", len(df_filtrado))
    st.dataframe(df_filtrado, use_container_width=True)

    # Exibição da Tabela
    st.subheader(f"Lista de Deputados - {estado_selecionado}")
    st.dataframe(df_filtrado, use_container_width=True)

    # Gráfico simples por partido no estado selecionado
    st.divider()
    st.subheader("Distribuição por Partido")
    chart_data = df_filtrado['siglaPartido'].value_counts()
    st.bar_chart(chart_data)

except FileNotFoundError:
    st.error("Erro: O arquivo 'deputados_2022.csv' não foi encontrado. Certifique-se de que ele está no mesmo diretório do script.")
except Exception as e:
    st.error(f"Ocorreu um erro inesperado: {e}")

