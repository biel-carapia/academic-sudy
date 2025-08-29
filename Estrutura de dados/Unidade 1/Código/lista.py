# Criação de uma lista
frutas = ["maça", "banana", "cereja", "laranja"]

# Adicionando elementos
frutas.append("kiwi") # Adiciona ao final
frutas.insert(1, "manga") # Insere na posição 1, insere na posição mas não substitui o valor

# Removendo elementos
frutas.remove("banana") # Remove pelo valor
del frutas[0] # Remove pelo índice
frutas.pop() # Remove e retorna o última elemento

# Acessando elementos
print(frutas[2]) # Acessa o terceiro elemento
print(frutas[-1]) # Acessa o último elemento

# Modificando elementos
frutas[1] = "abacate" # Modifica o elemento na posição 1

# Verificando a existência de um elemento
if "abacate" in frutas:
    print("Abacate está na lista")

# Tamanho da lista
print("Lista: ", frutas)
print(len(frutas)) # Retorna o número de elementos na lista


'''
# Combinando listas
vegetais = ["cenoura", "batata"]
comida = frutas + vegetais # Combina listas


# Outras operações
frutas.sort() # Ordenar a lista
frutas.reverse() # Inverte a lista
frutas.count("laranja") # Conta quantas vezes um elemento aparece
frutas.index("laranja") # Encontra o índice de um elemento
copia_frutas = frutas.copy() # Faz uma cópia da lista
frutas.clear() # Limpa a lista, removendo todos os elementos

# List comprehension
quadrados = [x ** 2 for x in range(10)] # Cria uma lista de quadrados

# Imprimir listas
print(comida)
print(quadrados)

# Executando todas as operações
def demonstrar_operacoes_lista():
    print("Lista original:", frutas)
    print("Lista após adições:", frutas)
    print("Lista após remoções", frutas)
    print("Acesso a elementos:", frutas[0])
    print("Lista após modificação:", frutas)
    print("Tamanho da lista:", len(frutas))
    print("Lista combinada:", comida)
    print("Lista de quadrados:", quadrados)

demonstrar_operacoes_lista()

'''



# Criação de uma tupla
# minha_tupla = (1, 2, 3) # Criando uma tupla com três números inteiros
# outra_tupla = 4, 5, 6 # Criando uma tupla sem parênteses, é válida também


# Criação de um dicionário
# Exemplo 1
# dicionario_curso = {"nome" : "Ciências da Computação", "créditos" : 240}
# Criando um dicionário

# Exemplo 2
# info_estudante = {}

# Acessando as chaves do dicionário
# chaves = info_estudante.keys()
# print("Chaves:", chaves)  # Saída: Chaves: dict_keys(['nome', 'idade', 'curso'])
# Acessando os valores do dicionário
# valores = info_estudante.values()
# print("Valores:", valores)  # Saída: Valores: dict_values(['Ana Silva', 22, 'Engenharia de Software'])

# Criação de um conjunto
# Exemplo 1
# meu_conjunto = {1, 2, 3, 4, 5}
# meu_conjunto.add(6) # Adicionando elementos ao conjunto
# meu_conjunto.remove(2) # Removendo elementos do conjunto

# Exemplo 2
# União de conjuntos
# conjunto_a = {1, 2, 3}
# conjunto_b = {3, 4, 5}
# uniao = conjunto_a.union(conjunto_b)
# print(uniao) # Saida: {1, 2, 3, 4, 5}
