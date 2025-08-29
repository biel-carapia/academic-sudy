# Algoritmo de Kruskal: Paisagismo 
class Grafo:
    def __init__(self, orientado=False): 
        # dict em que as chaves são o nomes de vértices origem 
        # e os valores são os pares de vértice destino e custo 
        self._lista_de_adjacencias = dict() 
        self.orientado = orientado 

    @property 
    def vertices(self): 
        return set(self._lista_de_adjacencias.keys())
    
    def arestas(self, v_origem=None): 
        if v_origem: 
            # obtém arestas do vértice 
            return self.v_arestas(v_origem) 

        # retorna arestas do grafo inteiro 
        arestas_do_grafo = [] 
        for v_origem in self.vertices: 
            # acumula as arestas de todos os vértices 
            arestas_do_grafo += self.v_arestas(v_origem) 
        return arestas_do_grafo
    
    def v_arestas(self, v_origem): 
        # retorna arestas de um vértice 
        arestas = [] 
        for v_destino, custo in self._lista_de_adjacencias[v_origem]: 
            arestas.append((v_origem, v_destino, custo)) 
        return arestas 
    
    def inserir_aresta(self, u, v, custo): 
        # cria uma chave `u` com valor lista vazia no dicionário, 
        # se chave `u` não existir 
        self._lista_de_adjacencias.setdefault(u, []) 

        # cria uma chave `v` com valor lista vazia no dicionário, 
        # se chave `v` não existir 
        self._lista_de_adjacencias.setdefault(v, []) 

        # adiciona a aresta ao vértice `u` 
        self._lista_de_adjacencias[u].append((v, custo)) 

        if not self.orientado: 
            # se é um grafo orientado 
            # adiciona a aresta ao dicionário do vértice `v` 
            self._lista_de_adjacencias[v].append((u, custo)) 

    def inserir_arestas(self, arestas): 
        for aresta in arestas: 
            self.inserir_aresta(*aresta) 

    def imprimir(self): 
        total = 0 
        for u, v, custo in self.arestas(): 
            print("{}".format(u, v, custo), end=' ') 
            total += custo 

        if not self.orientado: 
            # divide por 2 para descontar a duplicidade 
            total = total / 2 
        print() 
        print("{}".format(total))

    #72 

    def kruskal(grafo): 
        # cria conjunto de arestas da MST 
        arestas_mst = set() 

        # cria um dicionário para armazenar 
        # o conjunto de vértices para cada vértice 
        # que inicialmente é o próprio vértice 
        conjuntos = {v: {v} for v in grafo.vertices} 

        # ordena todas as arestas do grafo 
        arestas_ordenadas = sorted( 
            grafo.arestas(), 
            key=lambda aresta: aresta[-1] 
        ) 

        # para cada aresta, em ordem crescente 
        for aresta in arestas_ordenadas: 
            # obtém u, v e custo, da aresta 
            u, v, custo = aresta 
            if conjuntos[u].isdisjoint(conjuntos[v]): 
                # os conjuntos de u e o de v são conjuntos disjuntos 
                # adiciona aresta ao conjunto MST 
                arestas_mst.add(aresta) 
                # une os conjuntos v e u 
                uniao = conjuntos[u] | conjuntos[v] 
                # conjunto de u, conterá conjunto de v 
                conjuntos[u] = uniao 
                # conjunto de v, conterá conjunto de u 
                conjuntos[v] = uniao 

        mst = Grafo() 
        mst.inserir_arestas(arestas_mst) 
        return mst 
    
    #106 

    def solicitar_locais(): 
        qtd = int(input()) 
        locais = [] 
        for i in range(qtd): 
            local = input() 
            locais.append(local) 

        return locais
    
    def solicitar_distancias(locais): 
        from itertools import combinations 
        distancias = [] 
        for u, v in combinations(locais, 2): 
            distancia = input("".format(u, v)) 
            distancias.append((u, v, float(distancia))) 
        return distancias
    

print() 

arestas = [ 
    ('Parquinho', 'Lago', 2.2), 
    ('Quadras', 'Lago', 5.5), 
    ('Parquinho', 'Quadras', 8.6), 
    ('Lanchonete', 'Lago', 6), 
] 

g1 = Grafo() 
g1.inserir_arestas(arestas) 
mst = g1.kruskal(g1) 
mst.imprimir() 

print() 
print() 
locais = g1.solicitar_locais() 
arestas = g1.solicitar_distancias(locais) 

g2 = Grafo() 
g2.inserir_arestas(arestas) 
mst = g2.kruskal(g2) 
mst.imprimir()