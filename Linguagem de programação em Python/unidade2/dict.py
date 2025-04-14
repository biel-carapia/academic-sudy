#Exemplo 1 - Criação de um dicionário vazio, seguindo de atribuição de chaves e valores
dici_1 = {}
dici_1['nome'] = 'Maria'
dici_1['idade'] = 25

#Exemplo 2 - Criação de um dicionário com pares chve: valor
dici_2 = {'nome': 'Maria', 'idade': 25}

#Exemplo 3 - Criação de um dicionário com uma lista de tuplas representado pares chav: valor
dici_3 = dict([('nome', 'Maria'), ('idade', 25)])

#Exemplo 4 - Criação de um dicionários usando a função built-in zip() e duas lista, uma para as chaves e outra para os valores.
dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))

#Teste se todas as contruções resulta em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) # Deve imprimir True
print(dici_1)