# Importe a biblioteca NumPy
import numpy as np

# Crie um array NumPy de número inteiros
my_array = np.array([1, 2, 3, 4, 5])

# Imprima o array
print("Array original:")
print(my_array)

# Realize operações matemáticas com o array
squared_array = my_array ** 2 # Eleva cada elemento ao quadrado
sum_of_elements = np.sum(my_array) # Calcula a soma de todos os elementos

# Imprima os resultados
print("\nArray ao quadrado:")
print(squared_array)
print("\nSoma dos elementos:")
print(sum_of_elements)

#Acesse elementos do array
element_at_index_2 = my_array[2] # Acessa o elemento do índice 2
print("\nElemento do índice 2:", element_at_index_2)

