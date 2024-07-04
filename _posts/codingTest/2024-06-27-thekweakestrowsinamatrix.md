---
title:  "99클럽 코테 스터디 27일차 TIL - 힙"
layout: archive
categories:
  - codingtest
tags:
  - 99클럽
  - 코딩테스트 준비
  - 개발자 취업
  - 항해99
  - TIL
---

# 오늘의 학습 키워드 
힙

# 오늘 공부한 내용
힙

# 오늘의 회고
오늘의 문제는 2차원 배열에서 각 row마다 1의 갯수를 카운팅 한 후 1의 갯수가 가장 적은 것부터 가장 많은 것까지 정렬하여 가장 갯수가 적은 행의 인덱스 리스트를 k번째까지 반환하는 문제였다.


### 예시
```python
mat = [
	[1, 1, 0, 0, 0],	# (0, 2)
	[1, 1, 1, 1, 0],	# (1, 4)
	[1, 0, 0, 0, 0],	# (2, 1)
	[1, 1, 0, 0, 0],	# (3, 2)
	[1, 1, 1, 1, 1]		# (4, 5)
], k = 3

# 2, 0, 3, 1, 4
result = [2, 0, 3]
```

처음에는 `dict`를 사용하여 키가 row의 카운팅 수가 되고 값이 row의 인덱스가 된 것을 `heap`으로 구성하여 최소값을 꺼내면 될 것이라 생각했다.

그런데 다시 생각해보니 굳이 `dict`를 사용하지 않고도 풀이할 수 있을 것 같다는 생각이 들어 `tuple`을 활용했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/562bd73d-bf48-4877-87ea-80ea5d66031d)
{: .align-center}

오늘도 하나씩 알아가는 계기가 된 것 같아 뿌듯했다.

내일도 꾸준하게 연습할 수 있도록 노력해야겠다.

# 결과물
## 문제내용
1은 군인 0은 민간인이다. 항상 1은 0의 왼쪽에 배치된다.

다음의 조건이 만족할 경우 군인의 수가 가장 약한 것부터 가장 강한 것 순으로 정렬해서 가장 약한 행의 인덱스 리스트를 k번째까지 반환하여라

1. i행에 있는 군인의 수가 j보다 적다.
2. 두 행 모두 군인의 수가 동일할 경우 i를 가장 약한 행으로 간주한다.



![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/0b4b5005-4796-4488-9c2f-acbb4899a3ad)
{: .align-center}


## 풀이 방법
### 나의 문제 풀이방법
1. `heap`과 결과 리스트를 초기화한다.
2. `heap`에 row의 1의 갯수와 인덱스를 `tuple` 형식으로 `push`한다.
3. k번째까지 `heap`에 있는 요소를 `pop()`한 결과를 반환한다.

```python
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        result = []
        
        for i in range(len(mat)):
            heapq.heappush(heap, (mat[i].count(1), i))
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
```


### 다른 사람의 문제 풀이방법
```python
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            mat[i] = [i, sum(mat[i])]

        mat.sort(key=lambda x: x[1])

        return [mat[i][0] for i in range(k)]
```
