import streamlit as st
import pandas as pd

st.set_page_config(page_title="Deputados 2022", layout="wide")

st.title("🏛️ Explorador de Deputados 2022")

@st.cache_data
def load_data():
    try:
        # Tenta ler com vírgula, se falhar ou gerar apenas 1 coluna, tenta ponto e vírgula
        df = pd.read_csv('deputados_2022.csv', encoding='latin1', sep=None, engine='python')
        return df
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None

df = load_data()

if df is not None:
    # --- PADRONIZAÇÃO DE COLUNAS ---
    # Convertemos os nomes das colunas para minúsculas para facilitar a busca
    df.columns = [c.strip() for c in df.columns]
    colunas_reais = df.columns.tolist()
    
    # Identifica as colunas dinamicamente (busca por termos aproximados)
    col_uf = next((c for c in colunas_reais if 'uf' in c.lower()), None)
    col_partido = next((c for c in colunas_reais if 'partido' in c.lower()), None)
    col_nome = next((c for c in colunas_reais if 'nome' in c.lower()), None)

    if col_uf and col_partido:
        # Filtro na Barra Lateral
        st.sidebar.header("Filtros")
        estados = sorted(df[col_uf].dropna().unique())
        estado_selecionado = st.sidebar.selectbox("Selecione o Estado:", ["Todos"] + estados)

        # Lógica de Filtragem
        df_filtrado = df if estado_selecionado == "Todos" else df[df[col_uf] == estado_selecionado]

        # Métricas
        c1, c2 = st.columns(2)
        c1.metric("Total de Deputados", len(df_filtrado))
        c2.metric("Total de Partidos", df_filtrado[col_partido].nunique())

        # Exibição
        st.dataframe(df_filtrado, use_container_width=True)

        # Gráfico de Partidos
        st.subheader("Distribuição por Partido")
        st.bar_chart(df_filtrado[col_partido].value_counts())
    else:
        st.warning(f"Não encontrei colunas de UF ou Partido. Colunas detectadas: {colunas_reais}")
