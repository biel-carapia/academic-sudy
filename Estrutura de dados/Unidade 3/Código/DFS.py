def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for next_vertex in graph[start]:
        if next_vertex not in visited:
            dfs(graph, next_vertex, visited)


graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

dfs(graph, 'A') # Exemplo de saída: A B D E F C