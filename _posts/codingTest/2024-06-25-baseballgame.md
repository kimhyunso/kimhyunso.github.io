---
title:  "99클럽 코테 스터디 25일차 TIL - 스택/큐"
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
스택/큐

# 오늘 공부한 내용
스택/큐

# 오늘의 회고
오늘의 문제는 문자열 배열일 주어지고 아래와 같은 조건이 있었다.

1. 숫자라면 `stack`에 `append()`
2. 'C' 라면 `stack`에서 `pop()`
3. 'D' 라면 `stack`의 마지막 요소 * 2
4. '+' 라면 `stack`의 마지막 요소 + `stack`의 마지막 전 요소

문제를 보고 조건문을 잘 사용하면 풀이가 쉽게 될 것이라 생각했다.

시간도 오래 걸리지 않고 풀이는 쉽게 되었지만, 다른 사람의 풀이와 비교해보니 풀이가 엉망이였다는 것을 깨달았다. 너무 성급하게 풀이를 했던 것 같다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/07432eb8-21c9-43f2-87eb-5b135f0870f2)
{: .align-center}

내일 문제는 좀 더 차분하게 풀 수 있도록 노력해야겠다.

# 결과물
## 문제내용
특이한 baseballgame을 할려고 한다. 문자열 배열이 주어진다. 문자열 배열을 하나씩 순회하면서 record에 작성한다.

1. 숫자라면 레코드에 그 숫자를 추가한다.
2. '+' 라면 현재 문자열 배열 마지막 요소와 마지막 이전 요소를 더한다.
3. 'C' 라면 레코드에서 숫자를 제거한다.
4. 'D' 라면 문자열 배열 마지막 요소 * 2을 한다.

![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/efbb3aa5-6f20-4fb3-ab95-7676487724f2)
{: .align-center}

![조건](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/b45a33a5-dc14-4eb9-acca-6189481a3f83)
{: .align-center}

## 풀이 방법
### 나의 문제 풀이방법
1. record를 초기화한다. 주어진 문자열 배열이 비어있을 때까지 요소를 순회한다.
2. 요소 문자열 배열 요소를 하나씩 `pop()`을 통해 target으로 잡는다.
3. target을 integer로 변환을 시도하다가 문제가 생기면 `Exception`에 있는 조건을 처리한다. (문제점)
4. target이 'C'일 경우 record에 추가되어있는 요소를 `pop()`한다.
5. target이 'D'일 경우 문자열 배열 마지막 요소가 음수인지 양수지인지 판단하여 * 2를 해준다. (문제점)
6. target이 '+'일 경우 문자열 배열 마지막 요소와 배열 이전 요소를 더한다.
7. record 요소를 모두 더한 값을 반환한다.

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
    
        
        while operations:
            target = operations.pop(0)
                        
            try:
                operation = int(target)
                record.append(operation)
            except Exception as e:
                if target == 'C':
                    record.pop()
                elif target == 'D':
                    if abs(record[len(record) - 2]) < 0:
                        record.append((record[len(record) - 1] * 2) * -1)
                    else:
                        record.append(record[len(record) - 1] * 2)
                elif target == '+':
                    record.append(record[len(record) -2] + record[len(record) - 1])
            
        return sum(record)
```            


### 다른 사람의 문제 풀이
1. stack을 초기화한다.
2. operations를 하나씩 순회하면서 꺼낸다.
3. 꺼낸 요소가 '+' 인지 판별한다.
    1. '+'가 맞다면 stack마지막 요소와 이전 요소를 더한 후 stack에 추가시킨다.
4. 꺼낸 요소가 'C' 인지 판별한다.
    1. 'C'가 맞다면 stack마지막 요소를 `pop()` 시킨다.
5. 꺼낸 요소가 'D' 인지 판별한다.
    1. 'D'가 맞다면 2 * stack의 마지막요소를 stack에 추가시킨다.
6. 모든 조건에 맞지 않는다면 stack에 꺼낸요소를 `integer`로 변환시켜 stack에 추가시킨다.
7. stack 요소에 있는 모든 요소를 더한 것을 반환한다.


```python
class Solution(object):
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
```