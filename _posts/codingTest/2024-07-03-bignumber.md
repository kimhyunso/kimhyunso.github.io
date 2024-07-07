---
title:  "이것이 코딩테스트다 - 1일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---
## 문제
주어진 수열 중 가장 큰 수를 M번 더하여 결과를 만든다. 

단, 더하는 횟수가 K번째일 때에는 같은 요소를 더할 수 없다.

## 예시
```python
n, m, k = 5, 7, 2
numbers = [3, 5, 4, 2, 1]

# 5 + 5 + 4 + 5 + 5 + 4 + 5 = 33
```

## 문제 풀이 아이디어
m번만큼 반복하면서 numbers에 값에서 최대값인 요소를 더한다.

만약, m번 만큼 반복 중 m이 k의 나머지 연산자로 나누어 떨어질 때 다음으로 큰 요소를 더한다.


## 문제 풀이 방법
1. `map(int, input().split(' '))` 입력받은 문자를 `int`형으로 변환한다.
2. `list(map(int, input().split(' ')))` 입력받은 문자들을 `int`형으로 변환 후 `list`로 만든다.
3. 가장 큰 값을 찾는다. 숫자 리스트에서 가장 큰 값을 지운다.
4. 1부터 m + 1까지 반복을 하면서 가장 큰 값을 더해 나간다.
5. 만약, m이 (k + 1) 나머지 연산자로 나누어 떨어지는지 확인 후 다음으로 큰 숫자를 더한다.

```python
n, m, k = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))


max_target = max(numbers)
numbers.remove(max_target)
result = 0

for i in range(1, m + 1):
    if i % (k + 1) == 0:
        result += max(numbers)
    else:
        result += max_target
        
print(result)
```

## 다른 문제 풀이 방법
`sort()`를 사용할 것, 문제의 핵심은 결국 첫번째로 가장 큰 요소와 두번째로 가장 큰 요소를 순차에 맞게 더하는 것

```python
n, m, k = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
numbers.sort()

result = 0

max_first = numbers[-1]
max_second = numbers[-2]

for i in range(1, m + 1):
	if i % (k + 1) == 0:
		result += max_second
		continue

	result += max_first

print(result)
```