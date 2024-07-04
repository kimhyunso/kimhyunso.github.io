---
title:  "99클럽 코테 스터디 15일차 TIL - 배열"
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
어제와 같이 배열에 대해 공부를 했다.

문제자체는 어렵지 않았다.

인덱스 0번째 요소부터 마지막 인덱스 요소까지 값이 같다면 카운팅을 하는 문제였다.

조건을 보니 100을 초과하긴 힘든 것을 파악하고 n^2인 이중반복문을 사용해도 괜찮을 것이라고 판단하게 되었다. (n^2 = (10000))



결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/dd509646-047b-40e5-9a01-631bd2083ad0)
{: .align-center}

문제가 쉽다고 해서 자만하지 않고 다른사람들의 풀이와 비교도 해보고 문제 접근방법을 다른 각도로 생각해볼 수 있도록 노력해야겠다.

# 결과물
## 문제내용

[1, 2, 3, 1, 1, 3] 과 같은 배열이 있다면

인덱스 (0, 3)의 값이 같고 인덱스 (0, 4), (3, 4), (2, 5)의 값이 같다. 해당 같은 값이 있는 인덱스를 카운팅하라

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/caeeee05-a548-47ce-adfc-4395a62023f5)
{: .align-center}

![조건](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/a732d6a6-ded4-46b5-b9e1-b516425291c6)
{: .align-center}


## 풀이방법
1. 배열의 길이 만큼 반복한다. (=i)
2. i + 1부터 배열의 길이 까지 반복한다. (=j)
3. 배열의 i와 배열의 j가 같은 지 비교한다.
4. 같다면 카운팅을 한다.

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            target = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1

        return result        
```



