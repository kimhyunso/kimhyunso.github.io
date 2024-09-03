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
두 개의 배열 A와 B가 있다. 

두 개의 배열에서 K번 바꿔치기를 진행하여, 배열 A의 모든 원소를 더한 값을 가장 크게 만들고 싶다.

## 조건
첫 번째 줄에 N, K가 공백으로 구분되어 입력됨 (1 <= N <= 100,000, 0 <= K <= N)

두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력됨 모든 원소는 10,000,000보다 작은 자연수

세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력됨 모든 원소는 10,000,000보다 작은 자연수

## 문제 풀이방법
1. 배열 A를 오름차순 정렬
2. 배열 B를 내림차순 정렬
3. K만큼 반복하면서 배열 A의 원소가 배열 B의 원소보다 작을 경우 원소들을 스와프한다.
4. 배열 A의 요소들을 더한다.

```python
N, K = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

for i in range(K):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break

print(sum(arrayA))
```

















