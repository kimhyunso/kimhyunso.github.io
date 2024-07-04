---
title:  "99클럽 코테 스터디 1일차 TIL - 트리순환문제"
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
트리순환문제

# 오늘 공부한 내용
`Optional`, `null` -> `None`

# 오늘의 회고
많은 시간 자바를 이용하고 학습하다보니 파이썬으로 된 코드가 처음에는 어색했다.

파이썬이 자바랑 다른 부분이 있다보니 문법이 어색했고, 처음 `Optional` 키워드를 보았을 때

파이썬에도 `Optional`이라는 라이브러리가 있다는 것을 처음 알았다.

일단 문법은 파이썬 코딩도장이라는 곳에서 간단하기 복습을 하였다.

문제를 풀 때, 옛날에도 LeetCode를 이용한 적이 있었지만 영어로된 문제에 적지않아 당황했다.

일단 문제는 구글 번역기를 번역을 해보았고 이미지를 통해 어떻게 구현되어야하는지를 파악했다.

다른 문제는 입력값 중 배열에 `null`이 포함되어 있다보니 이건 뭐지?라는 생각을 가지게 되었다.

파이썬 `null`을 검색한 결과 파이썬은 `null`이 `None`으로 표기된다는 것을 알게되었다.

성격이 급하고 시간 압박도 있다보니 성급하게 코드를 작성했다.

작성 후 제출하고 곰곰히 생각해보니 재귀함수를 이용하면 빨리 풀 수 있겠다는 생각을 가지게 되어 다시 풀이에 돌입했다.

일단 vscode를 통해 입력값이 어떻게 들어올지를 예상하고 코드를 리팩토링했다.

그 결과 통과를 하여 기분이 좋았다!

내일 문제는 조금 더 신중하게 고민해서 풀어야겠다는 생각이 들었다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/b5b28315-4856-4e62-b70b-96c9b992ea33)
{: .align-center}

# 결과물
## 문제내용
FALSE = 0
TRUE = 1
OR = 2
AND = 3

![2331번문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6f6b3c30-d571-419f-a68f-cccb73bd2433)
{: .align-center}

위와 같이 작동한다.


**리프 노드 : 맨마지막에 있는 자식이 없는 노드**

리프 노드 왼쪽과 오른쪽에 `False` 혹은 `True`가 있다면 부모 노드의 값을 보고 연산하여 진행한다.


## 풀이방법
재귀함수를 사용하여 문제를 해결했다.

TreeNode를 아래 테스트 케이스와 같이 초기화하여 진행하였다.

> 현재 노드의 왼쪽과 오른쪽이 있는지 판단한다.
>
> 왼쪽과 오른쪽 노드가 있다면 현재 노드의 값을 체크하여 값이 2 또는 3이라면 다시 1번으로 돌아가 진행한다.
> 
> 왼쪽 또는 오른쪽이 없다면 (=리프노드) 현재 노드의 값을 `boolean`형태로 변환하여 반환한다. (무조건 `True` 혹은 `False`가 나옴)
>
> 모든 재귀를 마치면 1-1 부분의 값체크하는 부분을 실행하여 `or` 또는 `and` 연산을 진행한다.

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        value = root.val
    
        if left and right:
            if value == 2:
                return bool(self.evaluateTree(left) or  self.evaluateTree(right))
            elif value == 3:
                return bool(self.evaluateTree(left) and self.evaluateTree(right))

        return bool(value)

        
# 테스트 케이스
solution = Solution()

left_node = TreeNode(1, None, None)
right_node = TreeNode(3, TreeNode(0, None, None), TreeNode(1, None, None))
top_node = TreeNode(2, left_node, right_node)

# top_node = TreeNode(0, None, None)
result = solution.evaluateTree(top_node)

print(result)
```

















