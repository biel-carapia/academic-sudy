# Definindo uma função chamada "soma"
def soma(a, b):
    resultado = a + b
    return resultado


resultado_soma = soma (5, 3)
#Imprimindo o resultado
print("A soma de 5 e 3 é: ", resultado_soma)


# Definindo uma função chamada "e_par"
def e_par(numero):
    #operador módulo %
    if numero % 2 == 0:
        return True
    else:
        return False
    

numero = 564646846133468446846168
if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} não é um número par.")