---
title:  "99클럽 코테 스터디 26일차 TIL - 힙"
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
힙

# 오늘 공부한 내용
힙

# 오늘의 회고
오늘의 문제는 주어진 2차원 배열 중 행마다 가장 큰 것을 고르고 행다마 골라진 것 중에 가장 큰 것을 골라 반환하는 문제였다.

처음에는 `heap`을 사용하여 최대 힙을 구성하여 풀이하면 될 것이라 생각했다.

python에서 heap을 구성하는 방법은 처음이였기에 인터넷 예제를 찾아보고 사용을 해보았다.

### heap
python에서는 heapq라는 라이브러리를 지원한다. 최소 힙을 구성한다.

`push()`를 할 때에는 `heappush()`를 사용하고 `pop()`를 할 때에는 `heappop()`을 사용해야한다.

최대 힙을 구성하기 위해서는 `-`를 사용하여 구성한다.

```python
import heapq

nums = [3, 5, 1, 2]
heap = []

for num in nums:
	heapq.heappush(heap, nums)
for _ in range(len(nums)):
	heapq.heappop(heap) # 1, 2, 3, 5


for num in nums:
	heapq.heappush(heap, -nums)
for _ in range(len(nums)):
	-heapq.heappop(heap) # 5, 3, 2, 1
```

heap을 사용할려고 하니 문제가 있었다.

row * column 만큼의 시간 복잡도가 들 수 있겠다는 생각이 들었다.

더 효율적인 방법을 고안하다가 row를 `sort()`하고 row끼리 묶은 것에서 가장 큰 것을 찾으면 되지 않을까하는 생각이 들었다.

하지만 row를 묶을 수 있는 방법을 잘 모르고 있엇다.

확인해보니 `zip()`이라는 내장함수가 있었다. `zip()`은 두가지의 배열을 묶어서 튜플형태로 반환해주는 방식이였다.

```python
nums1 = [3, 4, 6, 1]
nums2 = [2, 1, 4, 3]

for merge in zip(nums1, nums2):
	print(merge)   # (3, 2), (4, 1), (6, 4), (1, 3)
```

저번에 리스트를 언박싱하는 방법과 결합하여 풀이를 진행하였다. 결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/535719fb-ce06-4b62-96c2-05a49a6e0baa)
{: .align-center}

# 결과물
## 문제내용
주어진 2차원 배열상에서 row중 가장 큰 값을 찾아 삭제한다.

삭제된 값들 중 가장 큰 값을 더해서 반환하라


![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/cd49bc15-7274-4820-9fb2-f10b82e35c79)
{: .align-center}

## 풀이 방법
### 나의 문제 풀이방법
1. row를 오름차순으로 정렬한다.
2. `zip()`를 통해 `column`들을 묶어서 가장 큰 값을 더한다.
3. 더한 최종값을 반환한다.


```python
class Solution:
	def deleteGreatestValue(self, grid: List[List[int]]) -> int:
		result = 0
		for row in grid:
			row.sort()
		
		for col in zip(*grid):
			result += max(col)
		
		return result
```


### 다른 사람의 문제 풀이방법
1. row를 오름차순으로 정렬한다.
2. `zip()`함수를 통해 column들을 묶은 것에 가장 큰 값을 더해 반환한다.

```python
class Solution:
	def deleteGreatestValue(self, grid: List[List[int]]) -> int:
		for row in grid:
			row.sort()
    	return sum(max(col) for col in zip(*grid))
```
