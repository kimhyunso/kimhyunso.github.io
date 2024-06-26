---
title:  "99클럽 코테 스터디 26일차 TIL - 힙"
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
힙

# 오늘 공부한 내용
힙

# 오늘의 회고

# 결과물
## 문제내용

## 풀이 방법
### 나의 문제 풀이방법
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
```python
class Solution:
	def deleteGreatestValue(self, grid: List[List[int]]) -> int:
		for row in grid:
			row.sort()
    	return sum(max(col) for col in zip(*grid))
```
