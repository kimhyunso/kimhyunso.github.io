---
title:  "이것이 코딩테스트다 - 9일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
dfs/bfs

## 문제
아무개는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다.

미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야한다.

아무개의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.

미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 아무개가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

## 예시
```python
'''
101010
111111
000001
111111
111111
'''

'''
101010
234567
000008
111119
1111110
'''
```

## 조건
첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다. 

다음 N개의 줄에는 각각 M개의 정수 (0혹은 1)로 미로의 정보가 주어진다.

각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

## 문제 풀이 아이디어
상, 하, 좌, 우를 아래와 같이 표기한다.

- `dx = [-1, 1, 0, 0]`
- `dy = [0, 0, -1, 1]`

bfs를 사용하여 이전 노드의 값을 더하며 탈출에 필요한 최소 칸의 개수를 샌다.

## 문제 풀이 방법
1. N, M, map을 입력받고 deque 및 상, 하, 좌, 우를 초기화한다.
2. deque 안에 데이터가 있을 때까지 반복문을 돈다.
3. deque의 선입된 데이터(=x, y)를 추출한다.
4. 상, 하, 좌, 우 만큼 반복하면서 벽을 넘어가면 다시 반복하고, 해당 위치에 괴물이 있다면(=0) 다시 반복한다.
5. 해당 위치로 이동할 수 있다면(=1) 현재 위치에 전 노드의 값을 1 더한다.
6. map의 마지막 위치의 값을 반환한다.

```python
from collections import deque

N, M = map(int, input().split())
miro_map = []

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    miro_map.append(list(map(int, input())))

def bfs(miro_map, x, y):
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 만큼 반복
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 벽을 넘어가면 다시 반복
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 해당 위치가 괴물이 있으면 다시 반복
            if miro_map[nx][ny] == 0:
                continue

            if miro_map[nx][ny] == 1:
                miro_map[nx][ny] = miro_map[x][y] + 1
                queue.append((nx, ny))
    
    return miro_map[N - 1][M - 1]

print(bfs(miro_map, 0, 0))
```












































