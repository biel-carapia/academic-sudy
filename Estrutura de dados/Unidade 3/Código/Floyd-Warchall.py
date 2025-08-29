def floyd_warchall(grafo):
    """
    Encontra o menor caminho entre todos os pares de vértices em um grafo ponderado.

    Parâmetros:
        grafo: Uma matriz de adjacências que representa o grafo ponderado.

    Retorna:
        Uma matriz de distância que armazena os menores caminhos entre todos os pares de vértices.
    """

    n = len(grafo)
    distancias = grafo.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancias[i][j] = min(distancias[i][j], distancias[i][k], distancias[k][j])
    
    return distancias

# Exemplo de uso
grafo = [[0, 3, 4, 0],
         [0, 0, 0, 5],
         [0, 0, 0, 3],
         [8, 0, 0, 0]]

distancias = floyd_warchall(grafo)

# Imprimir a matriz de distâncias
for i in range(len(distancias)):
    for j in range(len(distancias[0])):
        print(f"{distancias[i][j]:2}", end=" ")
    print()

# Mostrar o menor caminho entre alguns pares de vértices
print(f"Menor caminho entre A e B: {distancias[0][1]}")
print(f"Menor caminho entre A e C: {distancias[0][2]}")
print(f"Menor caminho entre D e C: {distancias[3][2]}")