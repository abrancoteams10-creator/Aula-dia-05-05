import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Explorador de Deputados 2022", layout="wide")

st.title("🏛️ Consulta de Deputados Federais (2022)")
st.markdown("Filtre a base de dados por estado para visualizar os parlamentares.")

# Função para carregar os dados
@st.cache_data
def load_data():
    # Certifique-se que o arquivo está na mesma pasta do script
    df = pd.read_csv('deputados_2022.csv')
    return df

try:
    df = load_data()

    # Barra lateral para filtros
    st.sidebar.header("Filtros de Pesquisa")
    
    # Opção de escolha via Estado (siglaUf)
    estados = sorted(df['siglaUf'].unique())
    estado_selecionado = st.sidebar.selectbox("Selecione o Estado (UF):", ["Todos"] + estados)

    # Filtragem lógica
    if estado_selecionado != "Todos":
        df_filtrado = df[df['siglaUf'] == estado_selecionado]
    else:
        df_filtrado = df

    # Métricas rápidas
    col1, col2 = st.columns(2)
    col1.metric("Total de Deputados exibidos", len(df_filtrado))
    col2.metric("Partidos representados", df_filtrado['siglaPartido'].nunique())

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

