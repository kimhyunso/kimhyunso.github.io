---
title:  "leetcode - validparentheses"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
스택

## 문제
문자열 s가 '(', ')', '{', '}', '[' 및 ']' 문자만을 포함할 때, 입력 문자열이 유효한지 판단하세요.

입력 문자열이 유효하려면 다음 조건을 만족해야 합니다:

1. 열린 괄호는 같은 유형의 괄호로 닫혀야 합니다.
2. 열린 괄호는 올바른 순서로 닫혀야 합니다.
3. 모든 닫는 괄호는 같은 유형의 열린 괄호에 대응해야 합니다.


## 입출력 예시
Example 1:

> Input: s = "()"
>
> Output: true

Example 2:
 
> Input: s = "()[]{}"
> 
> Output: true

Example 3:

> Input: s = "(]"
>
> Output: false

Example 4:

> Input: s = "([])"
>
> Output: true

## 문제 풀이
1. 여는 괄호와 닫는 괄호의 짝이되는 dictionary형태의 자료구조를 정의한다.
- (주의사항으로 아래와 같이 정의되어야만 한다. 이유는 여는 괄호가 무조건 우선이기 때문)
2. 입력받은 s를 반복하며, 여는 괄호를 stack에 `append`한다.
3. 만약 여는 괄호가 아니라면 stack에 데이터가 존재하고, stack 데이터가 여는 괄호와 동일하다면 stack에서 `pop`을 한다.
4. 만약 stack에 데이터가 존재하지 않는다면 `false`
5. 2 - 4번까지의 과정을 반복하다가 stack에 데이터가 존재하지 않으면 `false`를 데이터가 존재한다면 `true`를 리턴한다.


```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}' : '{', ']' : '[', ')' : '('}

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack and brackets[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
```
