from sqlalchemy import create_engine
import pandas as pd


class Database:
    def init(self):
        self._nome = 'mysql+pymysql ://mysql_user :mysql_passiord@mysql_host/mysql_db'
        self._con = create_engine (self._name)
 

    def query(self, q):
        df = pd.read_sql(q, con=self._con)
        return df

    def filmes_avaliados_por_usuario(self, id_cliente):
        query = f"""
        SELECT ID_USUARIO, ID_FILME, AVALIACAO, DATA
        FROM AVALIACOES
        WHERE ID USUARIO = {id_cliente}
        """
        df = self.query(query)
        return df