import sqlite3
from pathlib import path

root_dir = path(__file__).parent
db_nome = 'dab-sqlite3'
db_arquivo = root_dir/db_nome
table_nome = 'pessoa'
con = sqlite3.connect(db_arquivo)
cursor = con.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {table_nome}'
    '('
    'ID INTEGER PRIMARY KEY AUTOINCREMENT'
    'NOME TEXT'
    'IDADE INTEGER'
    "PESO REAL"
    ')'
)

cursor.commit()
print('conexão feita')


cursor.close()
con.close()
