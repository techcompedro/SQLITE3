import sqlite3 as lite
from pathlib import Path

root_dir = Path(__file__).parent
db = 'db.sqlite3'
dbf = root_dir / db

connection = lite.connect(dbf)
cursor = connection.cursor()

TABELA = 'produtos'

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABELA} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '    
    'NOME TEXT, '
    'preco REAL, '
    'custo REAL, '
    'estoque INTEGER'
    ')'
)
connection.commit()


cursor.execute(
    f'INSERT INTO {TABELA} (id, nome, preco, custo, estoque)'
    'VALUES (NULL, "mouse", 5.60, 3.5, 300)'
)
connection.commit()


cursor.close()
connection.close()
