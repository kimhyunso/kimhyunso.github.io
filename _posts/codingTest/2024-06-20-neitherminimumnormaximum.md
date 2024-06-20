---
title:  "99클럽 코테 스터디 20차 TIL - 정렬"
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
드모르간 법칙

# 오늘의 회고
오늘의 문제는 정렬에 관한 문제였다.

주어진 숫자 리스트에서 minimum과 maximum 숫자를 제외하고 나머지 숫자 중 가장 작은 숫자를 반환하는 문제였다.

먼저 주어진 숫자 리스트를 오름차순으로 정렬한 뒤에 맨 리스트의 맨 첫번째 요소와 맨 마지막 요소를 제외한 후 나머지 요소 중 첫번째 요소만 결과값으로 반환하면 될 것이라 생각했다.

처음에는 컨디션의 문제인지 if문이 자꾸만 틀리기 시작했다. 아래와 같이 작성했다

```python
nums = [1, 2, 3, 4]
first = nums[0]
end = nums[len(nums) - 1]
result = []

for num in nums:
	# 첫번째 반복 : 1 != 1 : False / 1 != 4 : True
	# 두번째 반복 : 2 != 1 : True  / 2 != 4 : True
	# 세번째 반복 : 3 != 1 : True  / 3 != 4 : True
	# 마지막 반복 : 4 != 1 : True  / 4 != 4 : False
    if first != num or end != num:
        result.append(num)
```

위와 같이 `or`를 사용하게 되면 첫번째 요소와 마지막 요소도 포함하게 된다. 따라서 `and`로 바꾸어야 정상동작하는 것을 확인하였다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/29d8ea67-5928-41bf-9aed-3e876bd30885)
{: .align-center}

내일도 한가지씩 알아갈 수 있도록 노력해야겠다.

# 결과물
## 문제내용
주어진 리스트 안에서 최소값과 최대값을 제외한 나머지 중 제일 작은 요소를 반환하라

단, 최소값과 최대값을 제외한 나머지가 없다면 -1을 반환하라

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/ca52b661-c8f2-40f2-ab79-e191459ab8b6)
{: .align-center}


## 풀이 방법
1. 주어진 리스트를 정렬한다.
2. 리스트의 첫번째 요소와 반복하는 요소가 같지 않은지, 리스트의 마지막 요소와 반복하는 요소가 같지 않은지 판단한다.
3. 같지 않다면 결과 리스트에 추가한다.
4. 만약 결과 리스트에 값이 존재하지 않는다면 -1을 반환하고 존재한다면 맨 처음 요소를 반환한다.



```python
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        
        
        for num in nums:
            if num != nums[0] and num != nums[len(nums) - 1]:
                result.append(num)

        if not result:
            return -1
    
        return result[0]  
```