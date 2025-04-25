import pandas as pd
from datetime import date
from datetime import datetime as dt

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

print(df_selic.info())
print(df_selic)


#verificar duplicidade de linhas (passo muito importante), utilizando a função drop_duplicate()
df_selic.drop_duplicates(keep='last', inplace=True)
#mantem o último registro (keep='last')
#atráves do parâmetro inplace=True, faz com que a tranformação seja salva no DataFrame
#no nosso caso nao existe linhas duplicadas.

print(df_selic)


#adicionando colunas
data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autor"

print(df_selic.info())
df_selic.head(10)


df_selic.loc(0)

df_selic.loc([0, 20, 70, 90, 100])

teste = df_selic['valor'] < 0.01
print(type(teste))

print(teste)