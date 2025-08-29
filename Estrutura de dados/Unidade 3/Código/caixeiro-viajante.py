import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for column in range(vertices)] for row in range(vertices)]

    def adicionar_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def encontrar_menor_distancia(self, distancia, visitante):
        min = sys.maxsize
        for v in range(self.V):
            if distancia[v] < min and visitante[v] == False:
                min = distancia[v]
                min_index = v
        return min_index
    
    def dijkstra(self, origem):
        distancias = [sys.maxsize] * self.V
        distancias[origem] = 0
        visitados = [False] * self.V

        for cout in range(self.V):
            u = self.encontrar_menor_distancia(distancias, visitados)
            visitados[u] = True

            for v in range(self.V):
                if self.grafo[u][v] > 0 and visitados[v] == False and distancias[v] > distancias[v] + self.grafo[u][v]:
                    distancias[v] = distancias[u] + self.grafo[u][v]

        self.imprimir_solucao(distancias)

    def imprimir_solucao(self, distancias):
        print("Cidade \tDistância da Origem")
        for i in range(self.V):
            print(f"{i} \t\t{distancias[i]}")


# Exemplo de uso

g = Grafo(4)
g.adicionar_aresta(0, 1, 10)
g.adicionar_aresta(0, 2, 15)
g.adicionar_aresta(1, 3, 12)
g.adicionar_aresta(2, 3, 10)    
g.dijkstra(0)
