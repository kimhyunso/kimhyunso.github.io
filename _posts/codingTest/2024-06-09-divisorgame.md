---
title:  "99클럽 코테 스터디 9일차 TIL - 다이나믹 프로그래밍"
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
다이나믹 프로그래밍 (=동적프로그래밍)

# 오늘 공부한 내용
패턴 찾기

# 오늘의 회고
오늘은 문제의 패턴을 찾을려고 노력했다.

문제를 보고 이해하는데 시간이 조금 걸렸다.

해당 문제는 엘리스가 이기면 `True` 지면 `False`를 리턴하는 문제였다.

게임은 엘리스가 먼저 시작하며, 엘리스와 밥은 자신이 선택한 x만큼 움직일 수 있다. 단, 아래와 같은 조건이 있다.

> 0 < x < n and x % 2 == 0

또한 누군가 x만큼 움직이면 n - x 만큼 n의 숫자가 줄어든다.

가장 중요한 조건 중 하나는 엘리스와 밥은 항상 최선의 선택을 한다는 것이였다.

패턴을 찾기 위해 아래 이미지와 같이 트리구조로 엘리스가 이길때와 질때를 따져보았다.

패턴을 보니 n이 짝수일 때에는 엘리스가 이기고, 홀수일때에는 밥이 이기는 패턴을 찾아내었다.

또한 반복적으로 패턴이 보이기도 했다.

예를 들어 f(4), f(3) 등 여러개의 노드들이 중복된 것을 볼 수가 있었다.

### n = 4일때
엘리스가 이김
![트리4](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/12de76aa-4d08-45ba-94c7-f29f3bb59bdf)
{: .align-center}
### n = 5일때
밥이 이김
![트리5](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/a0b20fcd-62df-40fa-8c7a-eea710e29c37)
{: .align-center}
### n = 6일때
엘리스가 이김
![트리6](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/833b0fd4-242b-4f81-90e5-9a1d3534ec9b)
{: .align-center}
### n = 7일때
밥이 이김
![트리7](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/eabdfc0b-f69c-4ba0-b0f5-cd4b0eb1da58)
{: .align-center}


동적계획법을 이용하여 풀이를 할려고 했지만 굳이 짝수일때에는 엘리스가 이기고 홀수 일때에는 밥이이기니 홀짝프로그램처럼 코드를 작성했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/4bbd5556-8cc4-41e4-a66c-dfbd4793fa83)

너무 간단하기는 했다. 그래서 코드 리팩토링을 하니 아래 이미지와 같은 결과가 도출되었다.
```python
def solution(n:int) -> bool:
  return n % 2 == 0
```

두번째로 통과하였다.

![두번째통과](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/30a03b1e-df22-4999-a7d1-564700999c5f)
{: .align-center}

오늘은 문제가 일정한 패턴을 찾으면 쉽게 풀리는 경우였다.

하지만 문제가 쉽다고해서 자만하지는 않아야겠다!

내일 더 정진해서 패턴을 찾아보고 차분히 여러가지 방향을 찾아 풀 수 있도록 노력해야겠다.

# 결과물
## 문제내용
엘리스와 밥은 게임을 한다.

게임은 엘리스가 먼저 시작하며, 엘리스와 밥은 자신이 선택한 x만큼 움직일 수 있다. 단, 아래와 같은 조건이 있다.

- 0 < x < n and x % 2 == 0

x만큼 움직이면 n - x 만큼 n의 숫자가 줄어든다.

단, 엘리스와 밥은 최선의 선택만을 한다.

### 예시

n = 3

엘리스먼저 1칸을 움직이고, 밥이 1칸을 움직여서 엘리스는 다음칸을 움직일 수 없게됨 따라서, 엘리스의 패배


![문제예시](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/6cf3bcb4-5baa-46ea-a7da-e0b924901ddf)
{: .align-center}

엘리스가 패배하면 `False`를 이긴다면 `True`를 리턴하라

## 풀이방법
아래 이미지와 같이 n의 경우를 트리구조로 만들어보았다.

### n = 4일때
엘리스가 이김
![트리4](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/12de76aa-4d08-45ba-94c7-f29f3bb59bdf)
{: .align-center}
### n = 5일때
밥이 이김
![트리5](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/a0b20fcd-62df-40fa-8c7a-eea710e29c37)
{: .align-center}
### n = 6일때
엘리스가 이김
![트리6](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/833b0fd4-242b-4f81-90e5-9a1d3534ec9b)
{: .align-center}
### n = 7일때
밥이 이김
![트리7](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/eabdfc0b-f69c-4ba0-b0f5-cd4b0eb1da58)
{: .align-center}

이런 패턴을 생각할 때 n이 1부터 7까지 엘리스와 밥이 돌아가며 이긴다는 패턴이 보였다.

따라서 짝수일 때에는 엘리스가 이기고, 홀수 일때는 밥이 이긴다.

```python
# 첫번째 풀이
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False

# 두번째 풀이
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
```


















