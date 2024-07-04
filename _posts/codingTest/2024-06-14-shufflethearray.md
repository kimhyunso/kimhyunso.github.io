---
title:  "99클럽 코테 스터디 14일차 TIL - 배열"
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
배열

# 오늘 공부한 내용
배열


# 오늘의 회고
오늘은 배열에 대해 공부를 했다.

문제는 쉬운편이였다.

배열을 섞는 문제였는데, n이 주어진다면 0~n까지는 x배열이고 n+1~배열의마지막까지는 y배열로 바꾸어 x배열과 y배열을 섞는 문제였다.

단순히 배열 2개를 선언하여 x배열과 y배열을 만들고

결과 배열에 추가하여 문제를 제출했다.

결과는 통과였다.

![통과2](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/0fb849b3-4249-4ee6-9235-0b1049b8b0d8)
{: .align-center}

15분안에 푸는 문제라 쉬운편이였지만 안심하지말고 더욱 노력해야겠다.


# 결과물
## 문제내용

nums 배열안에 n번째 까지는 x배열이되고 n + 1부터 nums.length - 1 까지는 y배열이다.

아래와 같이 섞어라

> [x_1, y_1, x_2, y_2, x_3, y_3]

![Shuffle the Array문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/62aeeb92-475e-4840-ac15-9162e9c8cb2d)
{: .align-center}

## 풀이방법
1. x_nums 배열과 y_nums배열을 선언한다.
2. 반복문으로 0부터 n-1까지 x_nums에 추가시킨다.
3. 반복문으로 n부터 nums.length-1까지 y_nums에 추가시킨다.
4. n만큼 반복하며 result에 x_nums와 y_nums를 추가시킨다.

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_nums = []
        y_nums = []
        result = []
        
        for i in range(n):
            x_nums.append(nums[i])
        
        for i in range(n, len(nums)):
            y_nums.append(nums[i])
            
        for i in range(n):
            result.append(x_nums[i])
            result.append(y_nums[i])
        
        return result
```



