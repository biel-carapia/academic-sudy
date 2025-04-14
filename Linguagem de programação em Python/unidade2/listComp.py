linguagens = ["Python", "Java", "JavaScript", "C", "C#", "Swift"]
print("Antes da listcomp", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\nDepois da listcomp = ", linguagens)



# Função map!
# Aplica a uma função em toda a sequencia
# map(funcao, sequencia)
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
preco_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(preco_em_reais)


# Função filter!
# Filtra os elementos de uma sequência com base em uma função de teste (retorna true or false)
# filter(funcao_teste, sequencia)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)


# Tupla
# A ORDEM IMPORTA...
#EXEMPLOS DE MAIS TUPLAS E UTILIDADE
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

# A função enumerate() para obter tanto a posição quanto o valor de cada elemento na tupla