import sys 

class Grafo: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0] * vertices for _ in range(vertices)] 

    # Função que encontra o vértice com a distância mínima do conjunto de vértices ainda não incluídos no caminho mais curto 
    def distancia_minima(self, distancias, visitados): 
        minimo = sys.maxsize 

        for v in range(self.V): 
            if distancias[v] < minimo and visitados[v] == False: 
                minimo = distancias[v] 
                vertice_minimo = v
        return vertice_minimo 

 

    # Função que imprime o caminho mais curto a partir do vértice inicial para o vértice alvo 
    def imprimir_caminho(self, antecessores, j): 
        if antecessores[j] == -1: 
            print(j, end=" ") 
            return 

        self.imprimir_caminho(antecessores, antecessores[j]) 
        print(j, end=" ") 

    # Função que implementa o algoritmo de Dijkstra 
    def dijkstra(self, origem): 
        distancias = [sys.maxsize] * self.V 
        distancias[origem] = 0 
        visitados = [False] * self.V 
        antecessores = [-1] * self.V 

        for _ in range(self.V): 
            u = self.distancia_minima(distancias, visitados) 
            visitados[u] = True 
            for v in range(self.V): 
                if self.grafo[u][v] > 0 and visitados[v] == False and distancias[v] > distancias[u] + self.grafo[u][v]: 
                    distancias[v] = distancias[u] + self.grafo[u][v] 
                    antecessores[v] = u 

        print() 
        for i in range(self.V): 
            print(f"{i}\t\t{distancias[i]}\t\t\t", end=" ") 
            self.imprimir_caminho(antecessores, i) 
            print()


# Exemplo de utilização do algoritmo de Dijkstra 

g = Grafo(9) 

g.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
    [4, 0, 8, 0, 0, 0, 0, 11, 0], 
    [0, 8, 0, 7, 0, 4, 0, 0, 2], 
    [0, 0, 7, 0, 9, 14, 0, 0, 0], 
    [0, 0, 0, 9, 0, 10, 0, 0, 0], 
    [0, 0, 4, 14, 10, 0, 2, 0, 0], 
    [0, 0, 0, 0, 0, 2, 0, 1, 6], 
    [8, 11, 0, 0, 0, 0, 1, 0, 7], 
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(0)