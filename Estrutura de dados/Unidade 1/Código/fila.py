from collections import deque

# usa deque para criar uma fila
fila = deque(["banana", "chocolate", "morango"])
print(fila) # deque(['banana', 'chocolate', 'morango'])
# adicionando um novo elemento
fila.append("abacaxi")
print(fila) # deque(['banana', 'chocolate', 'morango', 'abacaxi'])
# Remove o primeiro elemento adicionado à fila.
fila.popleft()
print (fila) # deque(['chocolate', 'morango', 'abacaxi'])