---
title:  "99클럽 코테 스터디 12일차 TIL - 그래프"
layout: single
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
그래프

# 오늘 공부한 내용
그래프


# 오늘의 회고




# 결과물
## 문제내용

별처럼 생긴 그래프에서 중앙에 있는 노드를 리턴하라

단, 다른 노드는 무조건 중앙에 있는 노드와 연결되어 있다.


![그래프문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/101ab21d-30cc-4952-9d5a-cfcbd9166bb7)
{: .align-center}


## 풀이방법

첫번째 배열 0번째 인덱스 값과 두번째 배열 0번째 인덱스, 1번째 인덱스 값과 같은지 비교한다.

두번째 배열 0번째 인덱스와 세번째 배열 0번째 인덱스, 1번째 인덱스 값과 같은지 비교한다.

하나라도 같다면 해당 노드를 리턴한다.

```python
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:        
        for i in range(len(edges[0])):
            check_node = edges[0][i]
            for j in range(1, len(edges)):
                if check_node == edges[j][i]:
                    return check_node


```

> 합집합을 이용하여 첫번째배열과 두번째배열 중 같은 요소를 찾아 리턴한다.

```python
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()
```










