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
오늘은 그래프에 대해 공부를 했다.

그래프는 방향 그래프와 무방향 그래프가 있는데

이 문제는 무방향 그래프에 대해서 중앙에 있는 노드를 리턴하는 문제였다.

해당 문제에 패턴을 찾고자 일단 완전탐색을 할 수 있도록 모든 경우의 수를 구해보았다.

### 모든 경우의 수
```python
# edges = [[1,2],[2,3],[4,2]]

edges[0][0] == edges[1][0]
edges[0][0] == edges[1][1]
edges[0][0] == edges[2][0]
edges[0][0] == edges[2][1]

edges[0][1] == edges[1][0]
edges[0][1] == edges[1][1]
edges[0][1] == edges[2][0]
edges[0][1] == edges[2][1]
```

하지만 생각을 해보니 해당 문제에는 **모든 노드는 무조건 중앙과 연결**이 되어있다고 했다.

그래서 반복문을 통해 0번째 배열에 있는 값이 1번째 배열에 있는 값과 같다면 리턴하는 상황을 연출하면 풀 수 있을거라 생각했다.

결과적으로는 통과였다. 하지만 나는 중첩반복문을 사용했다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/b1691267-a4c5-4a1e-b125-9eec2b0acb33)
{: .align-center}

다른 사람의 코드를 참고해보니 `set` 자료구조를 사용하여 풀이를 한 것을 보게되었다.

합집합을 사용한 다음 해당 값을 리턴하면 되는 단순한 문제로 풀다니 이런 방법도 있겠구나 생각했다.

내일도 푼다음 다른 방법을 고민해보고 다른 사람들의 풀이방법들도 참고해야겠다.

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










