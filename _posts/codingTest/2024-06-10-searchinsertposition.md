---
title:  "99클럽 코테 스터디 10일차 TIL - 이진 탐색"
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
이진 탐색 (=binary search)

# 오늘 공부한 내용
이진 탐색, 투 포인터

# 오늘의 회고
오늘은 두 가지 문제를 풀었다.

첫번째 문제는 nums 숫자 리스트 안에 두 숫자의 합이 target 보다 작은 것을 찾는 문제였다.

문제자체는 투 포인터로도 풀 수 있는 문제였지만, 입력값인 n이 50 초과가 될 수 없다는 조건을 보고 이중반복문을 통해 처리할 수 있을 것이라 판단했다.

결과는 통과였다.

![통과1](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/ed74f680-4335-4762-a2ed-b8cf246364c8)
{: .align-center}

하지만 이번 기회에 투 포인터가 무엇인지 공부를 하기로 했다.

유튜브를 통해 투 포인터 알고리즘을 검색하니 여러가지 방식의 설명글이 있었다.

### 투 포인터
투 포인터는 부분 연속된 수열을 찾아 합이 주어진 값과 일치하는 등의 최적의 해를 찾는 알고리즘이다.

이게 무슨 말일까?

예를 들어 [1, 3, 4, 5, 6, 2] 와 같은 리스트가 있다고 가정하자

만약 n = 5인 부분 연속된 수열을 찾고 싶다면, 리스트를 정렬했을 시에 [1, 2, 3, 4, 5, 6] 과 같이 됨으로 [2, 3], [5]가 최적의 해일 것이다.

두번째 문제는 이진탐색을 이용한 풀이를 강제했다.

조건에 `O(log n)` 시간복잡도 만큼 풀이를 하라고 나와있었기 때문이다.

일단 중앙값을 찾고 찾고자하는 값보다 작다면 오른쪽에 있다는 뜻이고, 찾고자하는 값보다 크다면 왼쪽에 있다는 생각을 가지고 풀이를 시작했다.

하지만 그럼에도 문제가 풀리지 않아서 이진 탐색의 기본적인 구조를 찾아보고 직접 사용해보았다.

### binary search (이진탐색)
배열을 정렬 한다. 중앙을 기점으로 찾고자 하는 대상보다 크다면 왼쪽 = 오른쪽 - 1, 작다면 오른쪽 = 왼쪽 + 1

이렇게 하는 이유는 반복문을 돌면서 계속해서 절반씩 찾아가는 과정을 만들 수 있기 때문이다.

## left 일때 예시
![left](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/e5241964-08fc-445b-b960-2b4e62a6a458)
{: .align-center}

## right 일때 예시
![right](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/af96cd72-b94d-4eb6-8f13-f40c4a76f7bc)
{: .align-center}


결과는 통과였다.

![이진탐색통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/d32c1d52-2772-4924-bb2d-59a7b57bfe6c)


이번에는 갑작스러운 문제 변동이 있었지만 두 문제 모두 풀이에 성공했다는 것과 여러가지를 공부해보았다는 점에서 많이 배웠던 것 같다.

내일은 다른 방법의 풀이도 생각해보고 적용가능 여부를 판단하여 적용할 수 있도록 노력해보아야겠다.

# 결과물
## 첫번째 문제 내용
숫자 리스트 nums가 주어진다.

숫자 리스트 안에서 두 숫자를 더해 target보다 작다면 카운팅을 한다.

**nums의 길이는 1이상 50이하**

### 예시
![문제예시](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/6fbfd72d-5e95-4a96-a9aa-df2ba7656545)
{: .align-center}

## 풀이방법
완전 탐색을 이용해 풀이함

nums의 길이가 50을 초과할 수 없다는 조건을 보고 n^2의 시간이 걸려도 풀 수 있다는 판단

1. nums의 길이만큼 반복
2. 1번의 반복 + 1 부터 nums의 길이 부터 반복
3. 만약 두 합계가 target보다 작을 시 카운팅

```python
from typing import List

# 완전 탐색 풀이
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
                    break

        return count
```

## 두번째 문제 내용

nums 리스트 안에 target이 있다면 target의 인덱스 번호를 리턴


target이 nums 리스트 안에 없다면 

1. 왼쪽 : 1을 리턴
2. 오른쪽 : 배열의 길이를 리턴

![문제내용](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/25d1004f-cbe5-4467-a1ae-a5fad2a87f2c)
{: .align-center}

## 풀이방법
이진 탐색을 통해 풀이함

1. left : 배열의 0번째 인덱스 / right : 배열의 길이 - 1 선언 
2. left가 right 이하일때만 반복
3. mid = (left + right) // 2로 초기화
4. 1.1. nums[mid]에 있는 값이 target과 같다면 mid(=index) 리턴
5. 1.2. nums[mid]에 있는 값이 target보다 크다면 right = mid - 1 연산
6. 1.3. nums[mid]에 있는 값이 target보다 작다면 left = mid + 1 연산
7. 2번 반복
8. left 리턴 (left값은 항상 배열의 맨마지막 + 1이거나 1이 된다.)

## left 일때 예시
![left](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/e5241964-08fc-445b-b960-2b4e62a6a458)
{: .align-center}


## right 일때 예시
![right](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/af96cd72-b94d-4eb6-8f13-f40c4a76f7bc)
{: .align-center}


```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return left
```























