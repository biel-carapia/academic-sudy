class No:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class ArvoreBB:
    def __init__(self):
        self.root = None

    def inserir(self, key):
        if self.root is None:
            self.root = No(key)
        else:
            self._inserir_recursivo(self.root, key)

    def _inserir_recursivo(self, current_No, key):
        if key < current_No.key:
            if current_No.left is None:
                current_No.left = No(key)
            else:
                self._inserir_recursivo(current_No.left, key)
        else:
            if current_No.right is None:
                current_No.right = No(key)
            else:
                self._inserir_recursivo(current_No.right, key)

    def remover(self, key):
        self.root = self._remover_recursivo(self.root, key)

    def _remover_recursivo(self, current_No, key):  
        if current_No is None:
            return current_No      
        if key < current_No.key:
            current_No.left = self._remover_recursivo(current_No.left, key)
        elif key > current_No.key:
            current_No.right = self._remover_recursivo(current_No.right, key)
        else:
            if current_No.left is None:
                return current_No.right
            elif current_No.right is None:
                return current_No.left
            else:
                current_No.key = self._busca_valor_min(current_No.right)
                current_No.right = self._remover_recursivo(current_No.right, current_No.key)
        return current_No
    
    def _busca_valor_min(self, No):
        while No.left is not None:
            No = No.left
        return No.key
    
    def buscar(self, key):
        return self._busca_recursivo(self.root, key)
    
    def _busca_recursivo(self, current_No, key):
        if current_No is None or current_No.key == key:
            return current_No
        if key < current_No.key:
            return self._busca_recursivo(current_No.left, key)
        return self._busca_recursivo(current_No.right, key)
    
# Exemplo de uso
bst = ArvoreBB()
bst.inserir(3) # Adiciona tarefa com prioridade 3
bst.inserir(1) # Adiciona tarefa com prioridade 1
bst.inserir(4) # Adiciona tarefa com prioridade 4


# Verifica se a tarefa com prioriade 1 existe
print(bst.buscar(1) is not None)

# Remover a tarefa com prioridade 3
bst.remover(3)
print(bst.buscar(3) is not None)