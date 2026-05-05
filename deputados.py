import streamlit as st
import pandas as pd

st.title('Deputados Federais')

st.image('https://www.rbsdirect.com.br/filestore/0/2/5/0/7/1/5_f03f083dd1c7353/5170520_d6f99c6fd82cd20.jpg?version=1575255600')

# Carregando os dados
df = pd.read_csv('deputados_2022.csv')

# --- Adicionando o Selectbox ---
# Criamos uma lista com os estados únicos presentes no CSV
estados = df['siglaUf'].unique() 

# Criamos a caixa de seleção na barra lateral ou no corpo principal
estado_selecionado = st.selectbox('Selecione o Estado (UF):', estados)

# Filtrando o DataFrame com base na escolha do usuário
df_filtrado = df[df['siglaUf'] == estado_selecionado]

# Exibindo o resultado filtrado
st.write(f"Exibindo deputados de: **{estado_selecionado}**")
st.dataframe(df_filtrado)



