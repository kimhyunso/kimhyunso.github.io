---
title:  "이것이 코딩테스트다 - 13일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
dynamic programming (동적 프로그래밍)

## 동적 프로그래밍
큰 문제를 작게 나누어 해결한다.

## 대표적 문제
- 피보나치 수열

아래와 같이 $a_{n-1} + a_{n-2}$ 두 항을 더해 현재 항이 정해진다.

1, 1, 2, 3, 5, 8, 13 ...

점화식 : $a_n = a_{n-1} + a_{n-2}, a_1 = 1, a_2 = 1$

```python
def fibonaccy(x):
    if x == 1 or x == 2:
        return 1
    return fibonaccy(x - 1) + fibonaccy(x - 2)

print(fibonaccy(6)) # 8
```

## 메모이제이션
캐싱(chacing)이라고 불린다.

아래의 그림을 보자 피보나치 수열을 트리 구조로 바꾼 그림이다.

![피보나치수열트리구조](https://github.com/user-attachments/assets/b98462d2-b7f4-4526-ab52-d22450ad7883)
{: .align-center}

예를 들어 $f(5)$를 구하기 위해서는 $f(4)$ + $f(3)$을 구하여 만들어야한다.

중복되는 느낌이 있지 않은가? 실제로 확인해보면 $f(3)$이 3번이나 호출되는 것을 확인 할 수 있다.

어떻게 개선할 수 있을까? 여기에서 메모이제이션 기법이 들어간다.

결과값이 도출된 것은 미리 메모리상에 저장 후 사용하면 빠를 것이다.

메모이제이션이 적용된 아래의 그림을 확인해보자

![메모이제이션피보나치수열트리](https://github.com/user-attachments/assets/b87e30a4-acdc-45fa-b94d-b7cf4d75a9b3)
{: .align-center}

위의 트리보다는 중복이 없어져 좀 더 효율적으로 바뀐 것을 확인 할 수 있다.

### 메모이제이션 적용 코드
```python
n = int(input())
memo = [0] * n
memo[0] = 1
memo[1] = 1

def fibonaccy(x):
    if x == 1 or x == 2:
        return 1

    if memo[x - 1] != 0:
        return memo[x - 1]

    memo[x - 1] = fibonaccy(x - 1) + fibonaccy(x - 2)
    return memo[x - 1]

print(fibonaccy(n))
```

## 바텀업(bottom up) 방식(=상향식) vs 탑다운(top down) 방식(=하향식)
탑다운 방식은 주로 재귀함수를 사용

바텀업 방식은 주로 반복문을 사용 :: 전형적인 다이나믹 프로그래밍 형태

### 바텀업 방식
```python
n = int(input())
memo[0] * n
memo[0] = 1
memo[1] = 1

for i in range(2, n):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n - 1])
```




