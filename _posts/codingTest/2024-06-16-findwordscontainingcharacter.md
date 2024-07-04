---
title:  "99클럽 코테 스터디 16일차 TIL - 배열"
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
배열, `find()` 함수와 `in`의 차이점, 문자열비교

# 오늘의 회고
어제와 같이 배열에 대해 공부를 했다.

문제는 배열 안에 주어진 문자와 같다면 배열의 인덱스를 List형태로 담아 `return`하는 문제였다.

문제는 상당히 쉬워 보였지만, 문자열을 비교하는 방법이 조금 난해했다.

문자열 비교는 3가지 방법으로 비교할 수 있다는 것을 알았다.

1. 반복문을 사용하기
2. `in` 연산자 사용하기
3. 함수사용하기

### 반복문을 사용하기
반복문을 사용하여 문자열을 찾는 방법은 말 그대로 반복하면서 하나하나씩 비교하는 것이다.

```python
target = 'x'
word = 'Alex'
result = 0

for char in word:
    if target == char:
        result += 1
        break
```

### `in`연산자 사용하기

`[찾고자하는 값] in [찾을 대상]`

```python
target = 'x'
word = 'Alex'
result = 0

if target in word:
    result += 1
```

### 함수사용하기
함수는 찾을 수 있는 방식이 너무 많아서 `find()`를 사용했다.


```python
target = 'x'
word = 'Alex'
result = 0

if word.find(target):
    result += 1
```

여기에서 문제가 있다. 함수 `find()`를 사용하게 된다면 x의 위치값을 리턴하기 때문에 아래와 같이 이루어질 경우, 카운팅을 할 수 없다


```python
target = 'x'
word = 'xAlex'
result = 0

if word.find(target):
    result += 1
```

처음에는 `find()`함수를 사용했지만 풀이에 실패한 후, `in` 연산자를 사용하여 풀이를 진행하였다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/dd509646-047b-40e5-9a01-631bd2083ad0)
{: .align-center}

오늘은 문자열 비교 방법과 `in` 연산자에 대해서 다시 생각할 수 있는 하루였다.

오늘보다 내일 더 진보하는 사람이 될 수 있도록 노력해야겠다.

# 결과물
## 문제내용

words 배열 안에 주어진 x가 있다면 해당 배열 인덱스를 리스트로 만들어 `return`하라

![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/2e9b47b9-848d-4dea-b266-13c0858915af)
{: .align-center}

```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        
        for index, word in enumerate(words):
            if word.find(x):
                result.append(index)
        
        return result
```



