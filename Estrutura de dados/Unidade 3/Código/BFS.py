from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.poplelf()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            # Adiciona todos os vizinhos não visitados à filha 
            queue.extend(set(graph[vertex]) - visited)

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
bfs(graph, 'A') # Exemplo de saída: A B C D E F