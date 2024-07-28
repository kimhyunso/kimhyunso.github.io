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

![dfs](https://github.com/user-attachments/assets/66db5eb5-3e79-4059-9c04-0b298364fcad)
{: .align-center}


```python
def dfs(graph, node, visited):
    visited[node] = True
    print(node, end = ' ')

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

dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5
```


## bfs
너비 탐색 기법 : `O(n)` 시간 소요

- 큐 사용

![bfs](https://github.com/user-attachments/assets/1c39b3bc-1a5c-44a9-a7e0-5286d734b2ac)
{: .align-center}

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

bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
```







































