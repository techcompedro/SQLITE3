import streamlit as st 
import funcoes_do_bancodedados as bc
import pandas as pd

st.set_page_config(page_title='cadastro de produtos')


# inserir produto
with st.container():
    nome = st.text_input('DIGITE O NOME DO PRODUTO:', placeholder='CARACTERE NO MÁXIMO 25')
    preco = st.number_input('DIGITE O PREÇO DO PRODUTO', value=None, placeholder="0,00")
    custo = st.number_input('DIGITE O CUSTO DO PRODUTO', value=None, placeholder= "0,00")
    estoque = st.number_input('DIGITE O ESTOQUE', value=None, placeholder=0)

    botaocadastrar = st.button('cadastra')
    if botaocadastrar:
        st.write(botaocadastrar)
        
        inserirproduto = bc.inserirDados(nome, preco, custo, estoque)
        st.write('PRODUTO CADASTRO COM SUCESSO')
