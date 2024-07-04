import streamlit as st 
import funcoes_do_bancodedados as bc
# bc == funcoes_do_bancodedados
st.set_page_config(page_title='inicio')

# título e sub-título
with st. container():
    st.title('SISTEMA DE CADASTRO DE PRODUTOS')
    st.markdown('## EM DESENVOLVIMENTO')

# delete produto pelo o id
with st.popover('delete'):
    qualoid = st.number_input('DIGITE O ID DO PRODUTO:', value=None, placeholder=00)
    botaodelatar = st.button('deletar')
    if botaodelatar:
        deleteprod = bc.deletarProduto(qualoid)









    