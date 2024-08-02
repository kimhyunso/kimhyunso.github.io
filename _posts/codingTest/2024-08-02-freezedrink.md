---
title:  "이것이 코딩테스트다 - 8일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
dfs/bfs

## 문제

N x M 크기의 얼음 틈이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.

구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.

이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크름의 개수를 구하는 프로그램을 작성하시오.

다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

## 예시
```python
'''
00110
00011
11111
00000
'''
```

## 조건
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1000)

두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다.

이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

## 문제 풀이 아이디어
구멍이 뚫여있는 부분 (=0)이 연결되어 있다 생각하고 dfs를 통해 0이 연결되어 있는 부분의 갯수를 샌다.


## 문제 풀이 방법
1. N, M, 2차원 리스트의 맵 정보를 입력받는다.
2. dfs를 구현한다.
3. 만약 x, y가 맵의 범위를 벗어난다면 `False`를 리턴한다.
4. 만약 맵이 구멍이 뚫여있다(=0)면 상, 하, 좌, 우를 모두 재귀적으로 호출하여 방문한 상태(=1)로 만든다.
5. 반복문을 이용하여 전체 그래프를 순회한다.


```python
N, M = map(int, input().split())

ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input())))

def dfs(x, y):

    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if ice_map[x][y] == 0:
        ice_map[x][y] = 1

        # 상, 하, 좌, 우 모두 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, y) == True:
            result += 1

print(result)
```
















