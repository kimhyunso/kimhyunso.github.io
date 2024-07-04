---
title:  "99클럽 코테 스터디 17일차 TIL - 문자열"
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
문자열

# 오늘 공부한 내용
`lower()` 함수, `upper()` 함수, `itertools`, 패킹, 언패킹

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

이중반복문을 사용하여 풀이를 할 수 있지만 python에서는 `itertools`라는 라이브러리를 지원한다.

### `itertools` 예시
`itertools.combination()` 함수를 사용하여 아래와 같은 결과를 얻을 수 있다.

결과 `return`은 tuple이다.

```python
import itertools
find_list = [a, b, c]
n = 2

# [(a, b), (a, c), (b, c)]
result = list(itertools.combination(find_list, n))
```

### 패킹
여러개의 데이터를 하나로 묶어주는 것

### 예시
```python
num = '123'
result = list(num)

# tuple로 packing
student = '홍길동', 20220501
print(student) # ('홍길동', 20220501)
```

### 언패킹
여러개의 데이터의 묶음을 하나의 단위로 쪼개는 것

### 예시
```python
result = list(1, 2, 3)
print(*result) # 1 2 3

student = '홍길동', 20220501
tuple_to_student = tuple(student)
print(*tuple_to_student) # '홍길동' 20220501 
```

위의 라이브러리를 사용하여 조합을 찾았고 리스트와 튜플만 언패킹하면 될 것이라 생각했다. 

언패킹하는 방법은 위와 같이 *(아스트릭)을 사용하면 되기때문에 2중 언패킹을 할려면 두 개의 아스트릭을 사용하면 될 것이라 생각했다.

하지만 **에는 의미가 있었다. **은 dictional를 key와 value를 한번에 볼 수 있도록 하기위해서 언패킹하는 것이였다.

일단 어쩔 수 없이 반복문을 통해 해당 튜플을 꺼내서 튜플 안의 내용을 덧셈 연산 처리한 후 리턴하였다.

결과는 통과였다.

![조합통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/9b834edf-f1de-49ae-a394-13809062e3b3)
{: .align-center}

오늘은 그래도 언패킹의 개념을 다시한번 상기할 수 있어서 좋았던 날이였다.

내일도 시간이 나면 비기너 문제뿐만 아니라 종종 미들러 문제도 풀어보아야겠다.

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
`CombinationIterator` 클래스가 주어진다.

해당 클래스의 인스턴스를 생성하면 `null`을 출력하고

`next()` 함수를 실행하면 인스턴스 생성시 주어진 리스트와 갯수카운터에 의해 조합의 결과를 리턴한다.

`hasNext()` 함수를 실행하면 현재 조합의 결과가 있는지 없는지를 판단하여 `boolean`의 결과로 반환한다.

![조합문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/cde6f601-1357-4ea5-ac60-8323088ec49c)
{: .align-center}

## 풀이 방법
1. `__init__()` : `itertools.combinations()` 함수를 사용하여 조합결과를 `list`형식으로 초기화하고 combinationLength도 전역변수에 초기화한다.
2. `next()` : 조합 리스트를 거꾸로 정렬한다. (`pop()` 연산을 하기 위함) `pop()`을 하여 `tuple`을 꺼내고 combinationLength만큼 반복문을 돌며 결과를 더해 `return`한다.
3. `hasNext()` : 현재 조합 리스트의 길이가 0이상인지 판단한다.


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
