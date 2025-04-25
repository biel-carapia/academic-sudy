import sqlite3

# CREATE (criação da tabela e inserção de dados de exemplo)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''
  CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
  )
''')


dados_exemplo = [
    ('João', 'joao@gmail.com', '123-456-7890'),
    ('Maria', 'maria@gmail.com', '987-654-3210'),
    ('Pedro', 'pedro@gmail.com', '555-555-5555')
]
cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()


# READ (Leitura e exibição dos contatos)
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print("Contatos: ")
for contato in contatos:
  print(contato)


# UPDATE (atualização do número de telefone do contato com ID 2)
novo_telefone = '999-999-9999'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()


# DELETE (Exclusão de contato com ID 1)
contato_id_para_excluir = 1


cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir,))
conn.commit()
# Fechando a conexão
conn.close()
