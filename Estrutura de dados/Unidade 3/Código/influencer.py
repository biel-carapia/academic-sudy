class Grafo: 
    def __init__(self): 
        self.adjacencias = {} 

def adicionar_vertice(self, vertice): 
    if vertice not in self.adjacencias: 
        self.adjacencias[vertice] = [] 

def adicionar_aresta(self, vertice_origem, vertice_destino): 
    self.adicionar_vertice(vertice_origem) 
    self.adicionar_vertice(vertice_destino) 
    self.adjacencias[vertice_origem].append(vertice_destino) 

def grau_entrada(self, vertice): 
    grau = 0 
    for vizinhos in self.adjacencias.values(): 
      if vertice in vizinhos: 
        grau += 1 
    return grau 

def identificar_influenciadores(self): 
    influenciadores = [] 
    for usuario in self.adjacencias: 
      grau_entrada_usuario = self.grau_entrada(usuario) 
      if all(grau_entrada_usuario > self.grau_entrada(vizinho) for vizinho in self.adjacencias[usuario]): 
        influenciadores.append(usuario) 
    return influenciadores 

# Exemplo de uso do algoritmo 

rede_social = Grafo() 
rede_social.adicionar_aresta('Alice', 'Bob') 
rede_social.adicionar_aresta('Alice', 'Carol') 
rede_social.adicionar_aresta('Bob', 'Alice') 
rede_social.adicionar_aresta('Bob', 'Dave') 
rede_social.adicionar_aresta('Carol', 'Alice') 
rede_social.adicionar_aresta('Carol', 'Dave') 
rede_social.adicionar_aresta('Dave', 'Bob') 
rede_social.adicionar_aresta('Dave', 'Carol') 
rede_social.adicionar_aresta('Dave', 'Eve') 
rede_social.adicionar_aresta('Eve', 'Dave') 

influenciadores = rede_social.identificar_influenciadores() 
print("Rede de influenciadores: ", influenciadores) 