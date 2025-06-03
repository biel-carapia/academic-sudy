from sqlalchemy import create_engine

import pandas as pd

string_de_conexao = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
conexao = create_engine(string_de_conexao)

consulta = """SELECT id_transacao, id_produto, quantidade
FROM venda
WHERE id_cliente = 1"""

df = pd.read_sql(consulta, con=conexao)