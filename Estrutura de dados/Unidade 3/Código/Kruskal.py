class Grafo: 
    def __init__(self, vertices): 
        self.V = vertices # Número de vértices 
        self.grafo = []  # Lista para armazenar as arestas 

    # Adiciona uma aresta ao grafo 
    def adicionar_aresta(self, u, v, w): 
        self.grafo.append([u, v, w]) 

    # Função para encontrar o representante do subconjunto de um elemento 'i' 
    def encontrar(self, pai, i): 
        if pai[i] == i: 
            return i 
        return self.encontrar(pai, pai[i]) 

    # Função que realiza a união de dois subconjuntos 'x' e 'y' 
    def unir(self, pai, rank, x, y): 
        raiz_x = self.encontrar(pai, x) 
        raiz_y = self.encontrar(pai, y) 

        # União por rank para otimização 
        if rank[raiz_x] < rank[raiz_y]: 
            pai[raiz_x] = raiz_y 
        elif rank[raiz_x] > rank[raiz_y]: 
            pai[raiz_y] = raiz_x 
        else: 
            pai[raiz_y] = raiz_x 
            rank[raiz_x] += 1 

    # Função principal que roda o algoritmo de Kruskal 
    def kruskal(self): 
        resultado = [] # Guarda a árvore de spanning mínima 
        i, e = 0, 0   # Índice usado para as arestas resultantes e arestas selecionadas, respectivamente 

        # Ordena todas as arestas em ordem crescente de peso 
        self.grafo = sorted(self.grafo, key=lambda item: item[2]) 
        pai = [] 
        rank = [] 

        # Inicializa os subconjuntos 
        for no in range(self.V): 
            pai.append(no) 
            rank.append(0) 

        # Número de arestas resultantes será igual a V-1 
        while e < self.V - 1: 
            u, v, w = self.grafo[i] 
            i = i + 1 
            x = self.encontrar(pai, u) 
            y = self.encontrar(pai, v)
            # Se a inclusão dessa aresta não causa ciclo, adicionamos ela ao resultado 
            if x != y: 
                e = e + 1 
                resultado.append([u, v, w]) 
                self.unir(pai, rank, x, y) 

        # Imprime as arestas selecionadas 
        print() 
        for u, v, peso in resultado: 
            print("d%" (u, v, peso)) 

 

# Exemplo de utilização do algoritmo de Kruskal 
g = Grafo(4) 
g.adicionar_aresta(0, 1, 10) 
g.adicionar_aresta(0, 2, 6) 
g.adicionar_aresta(0, 3, 5) 
g.adicionar_aresta(1, 3, 15) 
g.adicionar_aresta(2, 3, 4) 

g.kruskal()


# Explicação do código

# A classe Grafo é utilizada para representar o grafo e contém métodos para adicionar arestas, 
# encontrar e unir subconjuntos, além do algoritmo principal de Kruskal. 

# No método kruskal(), as arestas são ordenadas por peso e, em seguida, 
# são adicionadas ao resultado se não formarem um ciclo. 

# Os métodos encontrar() e unir() são usados para encontrar o representante 
# de um subconjunto e para unir dois subconjuntos, respectivamente. 

# O método adicionar_aresta() é utilizado para adicionar uma aresta ao grafo. 

# O código de exemplo cria um grafo com 4 vértices e 5 arestas e executa o algoritmo de 
# Kruskal sobre ele, imprimindo as arestas selecionadas para a árvore de spanning mínima (Alves, 2021). 