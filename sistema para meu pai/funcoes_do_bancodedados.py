import mysql.connector
import pandas as pd
import streamlit as st
#Variavel para chamar a conexão
conexao = mysql.connector.connect(
host = 'localhost', #Aqui é onde está o banco, endereço do servidor
user = 'root', #É o tipo de usuário | super usuario (root)
password = '', #Senha do servidor
database = 'mercado' , #Banco de dados
)
cursor = conexao.cursor()

#Aqui vamos começar o CRUD
def inserirDados(nome_produto, preco, custo, estoque: int):
    #C - CREATE
    lucro = preco - custo
    comandoSQL = f'INSERT INTO produto (nome_produto, preco_venda_produto , preco_compra, lucro, estoque) VALUES ("{nome_produto}", {preco}, {custo}, {lucro}, {estoque})'
    cursor.execute(comandoSQL)
    conexao.commit() #ALTERAÇÃO DO BANCO

def deletarProduto(id: int ):
    comando_sql = f'DELETE FROM produto WHERE id_produto= "{id}"'
    cursor.execute(comando_sql)
    conexao.commit()


    
#consultarTodos
#R - READ - SELECT
comandoSQL = f'SELECT * FROM produto'
cursor.execute(comandoSQL)
    
resultadoConsulta = cursor.fetchall()
df = pd.DataFrame(resultadoConsulta, columns=cursor.column_names)
def vs():
    global df
    st.dataframe(df)


def consultarPeloId(id):
    #R - READ - SELECT
    id = int(input("Digite o código do produto "))
    comandoSQL = f'SELECT * FROM produto WHERE id_produto = {id}'
    cursor.execute(comandoSQL)

    resultadoConsulta = cursor.fetchall()
   
    print(resultadoConsulta)


