def dfs(graph, check, visited):
    visited[check] = True
    print(check, end = ' ')

    for i in graph[check]:
        if not visited[i]:
          dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)