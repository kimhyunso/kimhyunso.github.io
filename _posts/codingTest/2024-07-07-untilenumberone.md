---
title:  "이것이 코딩테스트다 - 2일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
그리디

## 문제
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.

단, 두 번째 연산은 N이 K로 나누어 떨어질 경우에만 해당한다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N이 1이 될 때까지 과정을 수행하는 최소 횟수를 구하여라

## 예시
```python
N, K = 17, 4
'''
1번 N에서 1을 뺀다. => 16 count 1
2번 N을 K로 나눈다. => 4 count 2
2번 N을 K로 나눈다. => 1 count 3
결과 : 3
'''
```

## 조건
첫째 줄에 N(2 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.

이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

## 문제 풀이 아이디어
N이 1이 될 때까지 반복하며 N이 K로 나누어 떨어질 경우 `N = N // K`를 하고, 나누어 떨어지지 않는다면 `N = N - 1`을 한다.


## 문제 풀이 방법
1. N, K를 입력받고, count를 초기화한다.
2. N이 1이 아니라면 (즉, 1이라면 반복문 탈출) 반복한다.
3. 만약 N이 K로 나누어 떨어진다면 N을 K로 나눈 값을 N에 저장하고 횟수를 샌다.
4. N이 K로 나누어 떨어지지 않는다면 N-1을 N에 저장하고 횟수를 샌다. 

```python
N, K = map(int, input().split())
count = 0

while N != 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1

print(count)
```

## 다른 문제 풀이 방법
### 문제풀이 방법 1
사실 5번의 방법이 필요한 것인지 잘 모르겠다.

1. n, k를 입력받고 result를 초기화한다.
2. n이 k 보다 크거나 같다면 반복한다.
3. n이 k로 나누어 떨어지지 않을때까지 n-1를 하고 횟수를 샌다.
4. n이 k로 나누어 떨어진다면 n을 k로 나누고 횟수를 샌다.
5. n이 1보다 클 경우 n-1을 하고 횟수를 샌다.

### 문제풀이 방법 2
1. n, k를 입력받고 result를 초기화한다.
2. n을 k로 나누고 k를 곱함으로써 k로 나누어 떨어지는 수를 만든다.
3. n에서 2번의 수를 뺌으로써 횟수를 알 수 있다. (예시)
4. n을 2번의 수를 덮어쓴다. (n은 k로 나누어떨어지는 수)
5. n이 k보다 작다면 반복문을 탈출한다.
6. n이 k보다 크다면 n-1을 하고 횟수를 샌다.

### 예시
```python
n, k = 25, 3
# n이 k보다 작을때까지 반복
target = (n // k) * k # 8 * 3 => 24
result += (n - target) # 25 - 24 => 1
n = target # n = 24
if n < k:
    break
result += 1
n //= k # 24 / 3 => 8
```

```python
# 문제 풀이 방법 1
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1 

while n > 1:
    n -= 1
    result += 1

print(result)

# 문제 풀이 방법 2
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
```
