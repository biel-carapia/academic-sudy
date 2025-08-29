class Grafo:
    def __init__(self):
        self.grafo = {} 

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, origem, destino, peso=1):
        if origem not in self.grafo:
            self.adicionar_vertice(origem)
        if destino not in self.grafo:
            self.adicionar_vertice(destino)
        self.grafo[origem].append((destino, peso))

    def mostrar_grafo(self):
        for vertice, arestas in self.grafo.items():
            print(f"{vertice}: {arestas}")

# Exemplo de uso
grafo = Grafo()
grafo.adicionar_vertice("A")
grafo.adicionar_vertice("B")
grafo.adicionar_vertice("C")
grafo.adicionar_aresta("A", "B", 5)
grafo.adicionar_aresta("A", "C", 10)
grafo.adicionar_aresta("B", "C", 3)

grafo.mostrar_grafo()

# Outra forma de representar sem o peso 

#class Grafo: 
    #def __init__(self): 
        #self.vertices = {} # Dicionário para armazenar os vértices e suas adjacências 

    #def adicionar_vertice(self, vertice): 
        #if vertice not in self.vertices: 
            #self.vertices[vertice] = [] # Inicializa a lista de adjacências vazia para o vértice 

    #def adicionar_aresta(self, origem, destino): 
        #if origem in self.vertices and destino in self.vertices: 
            #self.vertices[origem].append(destino) # Adiciona destino à lista de adjacências de origem 

    #def mostrar_vertices(self): 
        #print() 
        #for vertice in self.vertices: 
            #print(vertice)

    #def mostrar_arestas(self): 
        #print() 
        #for origem in self.vertices: 
            #for destino in self.vertices[origem]: 
                #print(f"{origem} -> {destino}") 

 

# Cria um objeto grafo 
#grafo = Grafo() 

# Adiciona vértices ao grafo 
# grafo.adicionar_vertice('A') 
# grafo.adicionar_vertice('B') 
# grafo.adicionar_vertice('C') 
# grafo.adicionar_vertice('D') 

# Adiciona arestas ao grafo 
# grafo.adicionar_aresta('A', 'B') 
# grafo.adicionar_aresta('A', 'C') 
# grafo.adicionar_aresta('B', 'C') 
# grafo.adicionar_aresta('C', 'D') 

# Mostra os vértices e as arestas do grafo 
# grafo.mostrar_vertices() 
# grafo.mostrar_arestas() 