---
title:  "이것이 코딩테스트다 - 7일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
dfs/bfs


## dfs
깊이 탐색 기법 : `O(N)` 시간 소요

- 스택사용

```python
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
```


## bfs
너비 탐색 기법 : `O(n)` 시간 소요

- 큐 사용

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end = ' ')

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
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

bfs(graph, 1, visited)
```







































