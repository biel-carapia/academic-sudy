class Anotacao:
    def __init__(self, pagina, paragrafo, texto):
        self.pagina = pagina
        self.paragrafo = paragrafo
        self.texto = texto
        self.chave = (pagina, paragrafo) # Uma tupla como chave para ordenação

class NodoB:
    def __init__(self, t):
        self.chaves = [] # Lista de anotações
        self.filhos = [] # lista de nodos filhos
        self.t = t # Grau mínimo da árvore B (determina o número máximo de chaves)

class ArvoreB:
    def __init__(self, t):
        self.raiz = NodoB(t)
        self.t = t

    def inserir(self, anotacao):
        # Implementação simplificada da inserção
        # Esta função deve localizar o nodo e inserir a anotação, dividindo o nodo se necessário
        return 0

    def remover(self, pagina, paragrafo):
        # Implementação simplificada de remoção 
        # Esta função deve localizar a anotação e removê-la, realizando a fusão de nodos se necessário 
        return 0
    
    def consultar(self, pagina, paragrafo): 
        # Retorna a anotação na localização especificada, se existir
        return 0

    def listar_anotacoes(self): 
        # Retorna uma lista de todas as anotações, em ordem 
        return 0
