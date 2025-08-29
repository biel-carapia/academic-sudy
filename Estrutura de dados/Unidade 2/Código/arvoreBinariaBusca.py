class No:
    def __init__(self, key):
        self.lelt = None
        self.right = None
        self.val = key

def inserir(root, key):
    if root is None: # Verifica se a variavel root = "Raiz" está VÁZIA
        return No(key)
    else:
        if root.val<key:
            root.right = inserir(root.right, key) # Insere a direita
        else:
            root.lelt = inserir(root.lelt, key) # Insere a esquerda
    return root        


raiz = No(14) # Raiz da árvore com o primeiro valor 

sequence = [4, 18, 0, 21, 17, 1, 8, 13] 



