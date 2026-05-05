import streamlit as st
import pandas as pd

st.title('Deputados Federais')

st.image('https://www.rbsdirect.com.br/filestore/0/2/5/0/7/1/5_f03f083dd1c7353/5170520_d6f99c6fd82cd20.jpg?version=1575255600')

df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

st.title('Buscador de deputados por Estado: ')
Estado = st.text_input('Digite a sigla do estado: ')
