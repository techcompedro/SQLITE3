import streamlit as st 
import funcoes_do_bancodedados as bc

st.set_page_config(page_title='vizualizar items da tabela')


#vizualizar tabela de todos os produtos
st.title('TABELA PRODUTO')
consulta = bc.vs()