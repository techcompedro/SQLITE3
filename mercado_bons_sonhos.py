import sqlite3 as lite
from pathlib import Path

root_dir = Path(__file__).parent
db = 'db.sqlite3'
dbf = root_dir / db

connection = lite.connect(dbf)
cursor = connection.cursor()

TABELA = 'produto'

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABELA} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '    
    'NOME TEXT, '
    'preco REAL, '
    'custo REAL, '
    'estoque INTEGER'
    'lucro REAL'
    ')'
)
connection.commit()

def add_produtos(nome: str, preco, custo, estoque, money):
    cursor.execute(
        f'INSERT INTO produto (id, nome, preco, custo, estoque, lucro)'
        f'VALUES (NULL, {nome}, {preco}, {custo}, {estoque}, lucro)'
    )
    connection.commit()

produto_nome = str(input('digite o nome do produto:'))
produto_preco = float(input('digite o preço do produto:'))
produto_custo = float(input('digite o preço de custo do produto:'))
calculo_do_lucro = produto_preco-produto_custo
pro01 = 100*produto_preco
pro02 = pro01/100
print(f'esse é de {pro02}% que é igual a R${calculo_do_lucro}')
produto_estoque = float(input('digite quantos produtos comprou para fazer o estoque:'))
add_produtos(produto_nome, produto_preco, produto_custo, produto_estoque, pro02)

cursor.close()
connection.close()
