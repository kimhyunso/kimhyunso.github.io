---
title:  "99클럽 코테 스터디 17차 TIL - 문자열"
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
문자열

# 오늘 공부한 내용
`lower()` 함수, `upper()` 함수, `itertools`

# 오늘의 회고
오늘은 문자열에 대해서 공부를 했다.

문제는 2차원 배열안에 0번째 인덱스는 type이고, 1번째 인덱스는 color, 2번째 인덱스는 name라고 한다.

아래와 같은 예시가 있을 때 key와 value가 주어진다면 key에서 value가 같은 카운팅을 새는 문제였다.


### 예시
```python
[   # name  color  name
  ["phone","blue","pixel"],
  ["computer","silver","lenovo"],
  ["phone","gold","iphone"]
] 
# count = 1
key = 'name'
value = 'computer'
```

일단 ruleKey에 따라서 index를 다르게 한 뒤 반복문을 돌며 배열의 인덱스번째와 주어진 ruleValue와 값이 같다면 카운팅하는 것을 생각했다.

또한 문자열이 여기서는 다르지 않지만, 문자열에는 대문자와 소문자가 있기 때문에 둘다 무조건 소문자로 변환 후 비교하도록 했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/9f216835-d5cc-4bf8-a5dd-7c83f05f5078)
{: .align-center}

오늘은 시간이 남아 미들러 문제도 풀이를 해보았다.

미들러 문제는 조합의 문제였다.

조합의 정의는 아래와 같다.

> 서로 다른 원소를 가진 집합에서 중복이 없고 순서와 상관 없이 선택하는 경우의 수
>
> 예를 들어 n = 2, [A, B, C]가 있다면 해당 배열로 조합가능한 결과를 만들어라 AB, AC, BC가 된다.


![조합통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/9b834edf-f1de-49ae-a394-13809062e3b3)
{: .align-center}



내일도 시간이 남으면 미들러 문제도 풀이해보고 다른 사람들의 풀이도 보도록 노력해야겠다.

# 결과물
## 문제내용

아래와 같은 2차원 배열이 존재할 경우, 0번째는 type, 1번째는 color, 2번째는 name이다.

ruleKey와 인덱스 위치가 같고, ruleValue와 해당 인덱스의 값이 같은 것을 카운팅하라

```python
[     # type   color   name
    ['phone', 'blue', 'pixel'],
    ['computer', 'silver', 'lenovo'],
    ['phone', 'gold', 'iphone']
], ruleKey = 'color', ruleValue = 'silver'
```


![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7810f18e-c45d-471c-9a95-524f64b2977e)
{: .align-center}

## 풀이 방법
1. default_index를 조건에 따라 0, 1, 2로 초기화한다.
2. items배열을 반복문을 돌며 하나씩 순회하며 items배열의 default_index 인덱스 번째와 ruleValue가 같은지 판단한다.
3. 같다면 카운팅을 한다.


```python
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        default_index = 0
        result = 0
        
        if ruleKey == 'color':
            default_index = 1
        elif ruleKey == 'name':
            default_index = 2
            
        for item in items:
            if item[default_index].lower() == ruleValue.lower():
                result += 1
                
        return result
```

# 미들러 문제
## 문제 내용
![조합문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/cde6f601-1357-4ea5-ac60-8323088ec49c)
{: .align-center}

## 풀이 방법


```python
import itertools

# 순열문제
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combination_char = list(itertools.combinations(characters, combinationLength))
        self.combinationLength = combinationLength

    def next(self) -> str:
        result = ''
        self.combination_char.sort(reverse=True)
        tuple_char = self.combination_char.pop()
        for i in range(self.combinationLength):
            result += tuple_char[i]
        
        return result
        

    def hasNext(self) -> bool:
        return len(self.combination_char) > 0
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
