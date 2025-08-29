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


def verificar_caminhos_alternativos(arestas, orientado=True):
    # para cada aresta, verifica se ela for removida,
    # há um caminho alternativo?

    for aresta in arestas:
        print()
        u, v = aresta

        # Cria um grafo
        grafo = Grafo(orientado)
        # Insere arestas no grafo
        grafo.adicionar_aresta(arestas)

        # imprimir grafo
        grafo.mostrar_grafo()

        print("Remover {}, {}".format(u, v))
        # Remove uma das arestas
        grafo.remover_aresta(*aresta)

        print("Busca em largura")
        visitados = grafo.busca_em_largura(grafo, u)
        if v in visitados:
            print("Sim, há caminhos alternativos")
        else:
            print("Nenhum caminho alternativo")


aresta1 = [
    ('J', 'K'),
    ('J', 'N'),
    ('N', 'P'),
    ('P', 'C'),
    ('C', 'Q'),
    ('C', 'J'),
    ('Q', 'M'),
    ('M', 'L'),
    ('L', 'C'),
    ('K', 'L')
]
verificar_caminhos_alternativos(aresta1, orientado=True)
aresta2 = [
    ('E', 'D'),
    ('E', 'F'),
    ('E', 'A'),
    ('D', 'A'),
    ('D', 'I'),
    ('A', 'H'),
    ('I', 'A'),
    ('I', 'H'),
    ('H', 'G'),
    ('G', 'A'),
    ('G', 'B'),
    ('B', 'F'),
    ('F', 'A'),
]
verificar_caminhos_alternativos(aresta2, orientado=False)


