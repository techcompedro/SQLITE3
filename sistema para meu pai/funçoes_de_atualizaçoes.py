import mysql.connector

#Variavel para chamar a conexão
conexao = mysql.connector.connect(
host = 'localhost', #Aqui é onde está o banco, endereço do servidor
user = 'root', #É o tipo de usuário | super usuario (root)
password = '', #Senha do servidor
database = 'mercado' , #Banco de dados
)
cursor = conexao.cursor()

#Aqui vamos começar o CRUD
def att_nome(id: int, novo_nome:str ):
    #UPATE - ATT OS DADOS, ATRAVÉS DO ID
    consultaSQL = f'UPDATE produto SET nome_produto = "{novo_nome}"\
    WHERE id_produto = {id}'
    cursor.execute(consultaSQL)
    conexao.commit()


def att_precovenda(id_pro: int, novo_preco):
    #UPATE - ATT OS DADOS, ATRAVÉS DO ID
    consultaSQL = f'UPDATE produto SET preco_venda_produto = {novo_preco}\
    WHERE id_produto = {id_pro}'
    cursor.execute(consultaSQL)
    conexao.commit()


def att_precocusto(id_prod: int, novo_preco):
    #UPATE - ATT OS DADOS, ATRAVÉS DO ID
    consultaSQL = f'UPDATE produto SET preco_compra = {novo_preco}\
    WHERE id_produto = {id_prod}'
    cursor.execute(consultaSQL)
    conexao.commit()


def att_estoque(id_produ: int, estoque):
    #UPATE - ATT OS DADOS, ATRAVÉS DO ID
    consultaSQL = f'UPDATE produto SET estoque = {estoque}\
    WHERE id_produto = {id_produ}'
    cursor.execute(consultaSQL)
    conexao.commit()


def att_tudo(id_produto: int, novo_nome, novo_preco, novo_custo, estoque:int):
    #UPATE - ATT OS DADOS, ATRAVÉS DO ID
    consultaSQL = f'UPDATE produto SET nome_produto = "{novo_nome}, preco_venda_produto = {novo_preco}, preco_compra = {novo_custo}, estoque = {estoque}"\
    WHERE id_produto = {id_produto}'
    cursor.execute(consultaSQL)
    conexao.commit()
 