def divide(x, y):
    assert y != 0, "Divisão por zero!"
    return x / y

result = divide(6, 0) # Vai dar erro pela divisão ser por ZERO
#result = divide(6, 2) # Vai funcionar corretamente
print(result)


def calcular_media(notas):
    assert len(notas) > 0, "A lista de notas não pode estar vazia"

    soma = sum(notas)
    media = soma / len(notas)
    return media


#Exemplo 1: Lista de notas vazia
notas_vazias = []
media = calcular_media(notas_vazias) # Isso lançará uma AssertionError


# Exemplo 2: Lista de notas válida
notas_validas = [8, 7, 9, 6, 8]
media = calcular_media(notas_validas) # Isso funcionará corretamente
print(media)