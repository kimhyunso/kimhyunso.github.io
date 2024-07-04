---
title:  "99클럽 코테 스터디 11일차 TIL - 이진 탐색"
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
이진 탐색 (=binary search)

# 오늘 공부한 내용
이진 탐색

# 오늘의 회고
오늘도 이진탐색을 이용한 문제를 풀었다.

이진 탐색으로 풀어야한다는 것을 알았지만 조건 중 n 100미만인 것을 보고 완전 탐색을 통해 풀었다.

그 후 이진 탐색으로 풀이를 할려고 했지만 쉽지는 않았다.

가장 쉽지 않았던 부분은 카운팅을 하는 것이였다.

다른 사람의 풀이를 보니 아 이렇게 하면 되겠구나 하고 다시 한번 생각하게 되었다.

나만의 문제 풀이도 좋지만 다른 사람의 풀이를 보고 이렇게 생각할 수도 있고, 저렇게 생각할 수도 있다는 것을 많이 보아야 겠다.

![통과](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/707fb27d-6950-46a5-a274-b3d9d94bfb65)
{: .align-center}


# 결과물
## 문제내용

해당 2차원 배열 요소 중 음수인 데이터의 갯수를 카운팅하여 리턴하라


![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7bb9759a-5cd9-42f3-951c-181c995d33df)
{: .align-center}

## 풀이방법

해당 요소들을 하나 하나씩 확인하면서 0보다 작을 경우 카운팅을 한다.

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for nums in grid:
            nums.sort()
            for num in nums:
                if num < 0:
                    count += 1
                else:
                    break
        return count
```

### 이분 탐색법을 활용한 풀이

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = (right + left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (n - left)
        return count
```












