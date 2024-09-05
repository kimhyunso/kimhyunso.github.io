---
title:  "이것이 코딩테스트다 - 11일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
이진탐색 (binarySerch)


## 이진탐색
데이터가 정렬이 되어있을 경우, 찾고자하는 값을 빠르게 찾을 수 있다.

시작점과 끝점, 중간지점을 지정하여 중간지점에 있는 원소보다 작다면 찾고자 하는 원소가 왼쪽에 있다는 것이고,

중간지점에 있는 원소보다 크다면 찾고자하는 원소가 오른쪽에 있다는 것이다.

## 코드
1. 재귀함수 이용

```python
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
target = 4

def binary_search(array, target, start, end):
    mid = (start + end) // 2

    if array[mid] == target:
        return array[mid]
    # 찾고자 하는 원소가 왼쪽에 있다는 뜻 0 ~ mid - 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 찾고자 하는 원소가 오른쪽에 있다는 뜻 mid + 1 ~ end
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

result = binary_search(array, target, 0, len(array) - 1)
print(result) # 4
```

2. 반복문 이용
```python
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
target = 4

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return array[mid]
        # 찾고자 하는 원소가 왼쪽에 있다는 뜻
        elif array[mid] > target:
            end = mid - 1
        # 찾고자 하는 원소가 오른쪽에 있다는 뜻
        elif array[mid] < target:
            start = mid + 1


result = binary_search(array, target, 0, len(array) - 1)
print(result)
```







