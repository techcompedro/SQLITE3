import sqlite3 as lite
from pathlib import Path

root_dir = Path(__file__).parent
db = 'banco_de_dados.sqlite3'
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
    'estoque INTEGER,'
    'lucro REAL'
    ')'
)
connection.commit()

def add_produtos(nome: str, preco: float, custo: float, estoque: int, lucro: float):
    cursor.execute(
        'INSERT INTO produto (NOME, preco, custo, estoque, lucro) VALUES (?, ?, ?, ?, ?)',
        (nome, preco, custo, estoque, lucro)
    )
    connection.commit()

produto_nome = input('Digite o nome do produto:')
produto_preco = float(input('Digite o preço do produto:'))
produto_custo = float(input('Digite o preço de custo do produto:'))
calculo_do_lucro = produto_preco - produto_custo
pro01 = calculo_do_lucro / produto_custo
pro02 = pro01 * 100
print(f'Esse é de {pro02:.2f}% que é igual a R${calculo_do_lucro:.2f}')
produto_estoque = int(input('Digite quantos produtos comprou para fazer o estoque:'))

add_produtos(produto_nome, produto_preco, produto_custo, produto_estoque, calculo_do_lucro)



cursor.execute(f"SELECT * FROM {TABELA}")


dados = cursor.fetchall()



for linha in dados:
    print(linha)





cursor.close()
connection.close()
