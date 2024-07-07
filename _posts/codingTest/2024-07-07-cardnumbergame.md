---
title:  "이것이 코딩테스트다 - 2일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---
## 문제
여러 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.

단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.

1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 갯수, M은 열의 갯수이다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있오록 전략을 세워야한다.

## 예시
```python
N, M = 3, 3
card_board = [
    [3, 1, 2],
    [4, 1, 4],
    [2, 2, 2]
]
'''
#1 행에서는 1
#2 행애서는 1
#3 행에서는 2
따라서 정답은 2
#1  #2  #3
3   4   2
1   1   2
2   4   2
'''
```

## 조건
첫째 줄에 숫자 카드들이 놓인 행의 갯수 N과 열의 갯수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= N, M <= 100)

둘째 줄 부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000이하의 자연수이다.


## 문제 풀이 아이디어
각 행마다 가장 작은 것을 모은 후, 그 중 가장 큰 것을 뽑아낸다.

## 문제 풀이 방법
1. n, m을 입력을 받은 후 card_board에 입력받은 카드들을 초기화한다.
2. card_board에 행에서 가장 작은 값을 result에 `append()`시킨다.
3. result값 중에서 가장 큰 요소를 찾는다.

```python
n, m = map(int, input().split())
card_board = []
result = []

for row in range(n):
    card_board.append(list(map(int, input().split())))

for row in card_board:
    result.append(min(row))

print(max(result))
```

## 다른 문제 풀이 방법
각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 아이디어가 중요

### 문제 풀이방법 1
1. n, m의 입력을 받고 result를 초기화한다.
2. n만큼 반복하며 행의 데이터를 입력받는다.
3. 입력받은 행의 데이터 중 가장 작은 값을 찾는다.
4. 가장 작은 값과 result를 비교하여 가장 큰 값을 찾는다.

### 문제 풀이방법 2
1. n, m를 입력받고 result를 초기화한다.
2. n만큼 반복하면서 행을 입력받는다.
3. min_value를 10001으로 초기화한다. 이유는 행데이터가 10000을 초과하지 않기 때문에 min_value와 행데이터 간 가장 작은 값을 찾고자함
4. 행 데이터를 뽑아 min_value와 행 데이터 중 작은 값을 찾는다.
5. result에 result와 min_value의 값 중 가장 큰 값을 찾은 후 반복한다.

```python
# min()함수를 이용한 답안
n, m = map(int, input().split())

result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
# 이중 반복문을 이용한 답안
n, m = map(int, input().split())

result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    # 10001을 대입하는 이유는 입력 조건이 10000 이하의 자연수 이기 때문에 10000보다 큰 수를 대입함으로써, 10001보다 작은 수를 판별하기 위함
    min_value = 10001
    for col in data:
        min_value = min(min_value, col)
    
    result = max(result, min_value)
print(result)
```




