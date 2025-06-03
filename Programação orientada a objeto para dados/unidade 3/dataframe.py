import pandas as pd

dados = {
    'id_cliente': [101, 102, 103, 104],
    'saldo': [500, 6500, 7000, 800],
    'tipo_de_conta': ['corrente', 'poupança', 'corrente', 'corrente']
}

df = pd.DataFrame(dados)

print(df[df['tipo_de_conta'] == 'poupança'])


df.loc[:2, 'id_cliente']

df.iloc[1:, 1:]