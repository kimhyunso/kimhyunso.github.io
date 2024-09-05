---
title:  "이것이 코딩테스트다 - 11일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
sort

## 문제
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다.

이 수를 큰 수부터 작은 수의 순서로 정렬해야한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

## 조건
첫째 줄에 개수 N이 주어짐 (1 <= N <= 500) :: 모든 정렬 사용 가능

둘째 줄 수의 범위가 주어짐 (1이상 100,000이하의 자연수)


## 풀이 방법
1. `sort()` 정렬 사용
2. 선택정렬 사용

```python
N = int(input())
numbers = []

for i in range(N):
    numbers.append(int(input()))

# sort() 사용
numbers.sort(reverse=True)

# 선택정렬 사용
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers) - 1):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        

print(numbers)
```

## 문제
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 

각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

## 조건
첫 번째 줄에 학생의 수 N (1 <= N <= 100,000)

두 번째 줄에 학생이름과 정수가 공백으로 구분되어 입력됨, 문자열의 길이와 학생의 성적은 100이하의 자연수이다.

## 문제 풀이
1. `sortd()` 사용

```python
N = int(input())

array = []

for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    

array = sorted(array, key=lambda item:item[1])

for item in array:
    print(item[0], end=' ')
```






































