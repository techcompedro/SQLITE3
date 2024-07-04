
import streamlit as st 
import funçoes_de_atualizaçoes as fa
# fa == funçoes_de_atualizaçoes

st.set_page_config(page_title='modificar_dados_do _produto')





    # modificar nome == grupo 01 {esse codigo ja esta ok}
with st.expander('MODIFICAR o nome do produto'):
    id01 = st.number_input("Digite o código do produto: ", value=None, placeholder= "0")
    nome01 = str(st.text_input('Digite o nome do produto:'))
    atualizar01 = st.button('atualizar')
    if atualizar01:
            modificarnome = fa.att_nome(id01, nome01)


    # modificar preço de venda == grupo 02 {esse codigo ja esta ok}
with st.expander('MODIFICAR o preço de venda'):
    id02 = st.number_input("escreva o código do produto:", value=None, placeholder= "0")
    novo_preco = st.number_input("Digite o preço de venda para o produto: ", value=None, placeholder= "0,00")
    atualiza02 = st.button('inserir')
    if atualiza02:
            modificar_preco_venda = fa.att_precovenda(id02, novo_preco)


    # modificar preço de custo == grupo 03 {esse codigo ja esta ok}
with st.expander('MODIFICAR o preço de custo'):
    id03 = st.number_input("qual é o código do produto: ", value=None, placeholder= "0")
    novo_preco_de_custo = st.number_input('Digite o preço de custo:', value=None, placeholder= "0,00")
    atualizar03 = st.button('enviar')
    if atualizar03:
            modificar_preco_custo = fa.att_precovenda(id03, novo_preco_de_custo)


    # modificar estoque == grupo 04 {esse codigo ja esta ok}
with st.expander('MODIFICAR estoque'):
    id04 = st.number_input("me fale qual é o código do produto: ", value=None, placeholder= "0")
    estoque = st.number_input('Digite o quantidaade de estoque:', value=None, placeholder= "0")
    atualizar04 = st.button('concluido')
    if atualizar04:
            modificar_estoque = fa.att_estoque(id04, estoque)
        
