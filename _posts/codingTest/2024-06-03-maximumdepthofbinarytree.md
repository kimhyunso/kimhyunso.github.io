---
title:  "99클럽 코테 스터디 3일차 TIL - 트리의 깊이문제"
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
재귀함수 복습, `max()`함수 사용방법

# 오늘의 회고

오늘도 어제와 같이 트리를 순환하여 depth가 몇 인지를 파악하는 문제를 풀었다.

마찬가지로 트리 문제이기 때문에 재귀함수를 통해 풀면 쉽게 풀 수 있을 것이라 판단했다.

그러나 이번에도 마찬가지로 쉽게 풀리지 않았다. 

처음 시작점을 잘 못 잡은 탓인지 3개의 depth에서는 4개가 나오고 2개의 depth에서는 1개가 나오는 상황이 일어났다.

어떻게 풀어야할지 생각에 잠긴 끝에 왼쪽 노드를 세고 오른쪽 노드를 센 다음 둘 중 큰 것을 고르면 되겠다는 생각이 떠올랐다.

오늘도 1시간 남짓한 시간안에 풀게되어 너무 마음이 아프다.

다음에는 더 차분하게 풀 수 있도록 노력해야겠다!

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/524f4eb5-8412-4533-8525-e9bf0ec8eae8)
{: .align-center}

# 결과물
## 문제내용
밑의 왼쪽 그림과 같이 트리가 있을 때 깊이를 구하여라

![104번문제](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/a4e39275-7a59-4e56-a94b-ad02d63dc802)
{: .align-center}

## 풀이방법
재귀함수를 사용하여 문제를 해결했다.

> 첫번째. 왼쪽 노드의 갯수를 샌다
>
> 두번째. 오른쪽 노드의 갯수를 샌다.
>
> 세번째. 왼쪽 노드와 오른쪽 노드 둘 중 큰 값을 고른다. + 1 (루트 노드를 새지 않았기 때문에 **중요**)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 테스트 코드

left_node = TreeNode(9, None, None)
right_node = TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))
top_node = TreeNode(3, left_node, right_node)

# top_node = TreeNode(1, None, TreeNode(2, None, None))

solution = Solution()
result = solution.maxDepth(top_node)

print(result)
```

















