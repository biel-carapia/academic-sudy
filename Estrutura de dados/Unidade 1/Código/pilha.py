pilha = []

# Operação de push com o método append()
pilha.append(4)
pilha.append(1)
pilha.append(5)
pilha.append(1)
pilha.append(6)

# Retorna todos os valores inseridos na pilha ao topo
print(pilha)

# Operação de pop com o método pop()
pilha.pop() # Remove o elemento do topo e retorna o último elemento

print(pilha)


# IMPLEMENTAÇÃO COM CLASSES

# class Pilha:
#    def __init__(self):
#        self.items = []

#    def empilhar(self, item):  
#        self.items.append(item)

#    def desempilhar(self):
#        if self.items:
#            return self.items.pop() 
#        return None

# Exemplo de uso da pilha
#my_stack = Pilha()
#my_stack.empilhar(1)
#my_stack.empilhar(2)
#my_stack.empilhar(3)


# Removendo elementos
#print("Elemento removido:", my_stack.desempilhar())  # Remove e retorna o elemento no topo da pilha

