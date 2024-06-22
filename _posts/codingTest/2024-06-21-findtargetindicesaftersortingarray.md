---
title:  "99클럽 코테 스터디 21일차 TIL - 정렬"
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
정렬

# 오늘 공부한 내용


# 오늘의 회고
오늘은 비교적 문제가 쉬운편이였다.

주어진 리스트를 정렬 후 리스트 안에서 target이 되는 숫자를 찾아 그 인덱스를 반환하는 문제였다.

리스트는 100 이하라 반복문을 사용하면 풀 수 있을 것이라 생각했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/320a617c-6c80-40b8-9e69-a34ea189bfb2)
{: .align-center}

너무 쉽다고 해서 너무 자만하지 않고 내일도 한가지씩 알아갈 수 있도록 노력해야겠다.

# 결과물
## 문제내용
주어진 리스트에서 target이 되는 숫자의 인덱스번호를 모두 반환하라

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/3000242f-425f-4aa0-a4fb-57e5e9ebac74)
{: .align-center}

## 풀이 방법
1. 주어진 리스트를 정렬한다.
2. 반복문을 돌며 target과 같은지 판별한다.
3. target과 같다면 새로운 리스트에 추가하여 반환한다.


```python
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        
        return result
```
