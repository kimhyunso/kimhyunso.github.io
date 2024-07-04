---
title:  "99클럽 코테 스터디 24일차 TIL - 스택/큐"
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
스택/큐

# 오늘 공부한 내용
스택/큐

# 오늘의 회고
오늘의 문제는 상점 품목의 가격이 정수 배열로 제공 되고 할인을 받을 수 있다.

할인을 받을 수 있는 방법은 `j > i` 이고, `prices[j] <= prices[i]`이다.

### 예시
```python
prices = [8, 4, 6, 2, 3]
# i = 0, j = 1 prices[j] <= prices[i]

# i = 1, j = 2 prices[j] <= prices[i]
# i = 1, j = 3 prices[j] <= prices[i]

# i = 2, j = 3 prices[j] <= prices[i]

# i = 3, j = 4 prices[j] <= prices[i]
```

이렇게 패턴을 찾고 보니 이중 반복문을 사용하여 풀이하면 될 것이라 생각했다.

마침 조건에도 최대 500을 넘지 않았다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/65fc9cd5-b41b-4753-8f4c-2136d9ba13a1)
{: .align-center}

다른 사람의 풀이를 보니 더 간결하게 풀이한 것이 있어 같이 첨언하겠다.

내일은 다른 사람의 풀이도 보고 다른 자료구조를 사용하는 방법을 생각해서 풀이해볼 수 있도록 노력해야겠다.

## 코드 피드백
스택을 활용해서 풀이하면 더 좋을 것

스택 활용은 내일...


# 결과물
## 문제내용

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/cec5815a-0b4d-4cbd-945d-945b422ed826)
{: .align-center}

![제약조건](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/153a2553-370c-486c-942d-5217dcaa37d9)
{: .align-center}

## 풀이 방법
### 나의 문제 풀이방법
1. 이중 반복문을 돈다. (이중 반복문 중 두번째 반복문 조건이 i + 1 부터 시작해야된다.)
2. `prices[j] <= prices[i]` 이하인지 판별한다.
3. 맞다면 `target`을 `prices[j]`로 바꾸고 두번째 반복문을 탈출한다.
4. 현재 `prices[i]`와 `target`을 뺀 것을 result 배열에 추가한다.
5. 추가된 result 배열을 반환한다.

```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        
        for i in range(len(prices)):
            target = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    target = prices[j]
                    break
            
            result.append(prices[i] - target)

        return result
```            


### 다른 사람의 문제 풀이
1. 이중 반복문을 돈다. (이중 반복문 중 두번째 반복문 조건이 i + 1 부터 시작해야된다.)
2. `prices[j] <= prices[i]` 이하인지 판별한다.
3. 맞다면 `prices[i]`에 `prices[i] - prices[j]`를 뺀 것을 덮어쓴 후 탈출한다.
4. `prices` 배열을 반환한다.

```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        
        return prices
```