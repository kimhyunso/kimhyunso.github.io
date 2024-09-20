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

아래와 같이 a_n-1 + a_n-2 두 항을 더해 현재 항이 정해진다.

1, 1, 2, 3, 5, 8, 13 ...

점화식 : $a_n = a_n-1 + a_n-2, a_1 = 1, a_2 = 1$

```python
def fibonaccy(x):
    if x == 1 or x == 2:
        return 1
    return fibonaccy(x - 1) + fibonaccy(x - 2)

print(fibonaccy(6))
```

## 메모이제이션
캐싱(chacing)이라고 불린다.

아래의 그림을 보자 피보나치 수열을 트리 구조로 바꾼 그림이다.

![피보나치수열트리](https://github.com/user-attachments/assets/b98462d2-b7f4-4526-ab52-d22450ad7883)
{: .align-center}

예를 들어 f(5)를 구하기 위해서는 f(4) + f(3)을 구하여 만들어야한다.
















