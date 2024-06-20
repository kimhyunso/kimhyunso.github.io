---
title:  "99클럽 코테 스터디 19차 TIL - 문자열"
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
`''.join()`함수, 문자열 중복제거 (`dict.fromkeys()` 사용)

# 오늘의 회고
오늘의 문제는 주어진 문자열에서 중복을 제거하고 차례대로 a~z로 치환하여 주어진 메시지를 해독하는 문제였다.

일단 a~z까지는 26개로 고정이 되어있으므로 리스트를 선언하고 

딕셔너리를 사용하여 주어진 문자열을 key로 치환된 a~z까지의 문자열을 value로 만들면 성공할 수 있을 것이라고 생각했다.

하지만 문자열에서 중복제거하는 방법이 같은 문자인지 판단하고 하는 과정이 이중반복문을 사용해야하기 때문에 다소 귀찮다고 느껴졌다.

다른 방법이 있나 고민을 해보았지만 별도로 생각나는 것이 없었다.

구글에 python 문자열 중복제거 방법을 찾아보았다.

중복제거 방법은 여러가지가 있었다.

### 문자열 중복제거 방법
1. `set` 자료구조 사용

이 방법은 순서를 보장하지 않는다.

```python
word = 'abbccdd'
result = ''.join(set(word)) # bacd
```

2. `dict.fromkeys()` 내장함수 사용

이 방법은 순서를 보장하지만 python버전이 3.6이상이여야한다.

이 방식을 선택했다.

```python
word = 'abbccdd'
result = ''.join(dict.fromkeys(word)) # abcd
```

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/745ba923-5194-4739-9c90-c98158152252)
{: .align-center}

내일도 한가지씩 알아갈 수 있도록 노력해야겠다.

# 결과물
## 문제내용

주어진 key 문자열에서 중복을 제거하고 앞에서 26자리의 문자만 알파벳순서대로 치환한다.

주어진 message를 위에서 치환한 문자로 바꾸어 결과를 반환한다.

대신 공백은 포함해야한다.

![문제예시](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/203ae737-0bb2-4f8a-8726-ebd7a36271f7)
{: .align-center}

## 풀이 방법
1. 주어진 key 문자열에서 공백과 중복을 제거한다.
2. 알파벳 리스트를 만든다.
3. 주어진 key 문자열과 알파벳 리스트를 매칭시킬 `dictionary` 자료구조를 공백도 포함해야하기 때문에 `{' ', ' '}`와 같이 초기화한다.
4. 반복문을 돌며 방금 만든 `dictionary`에 key문자열과 매칭시킬 알파벳을 삽입한다.
5. 주어진 메시지 문자열에서 `dictionary`에 key값을 찾으면 매칭되는 value가 나와 문자열을 더한다.

```python
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keys = ''.join(dict.fromkeys(key.replace(' ', '')))
        alphabet_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
        result = ''
        alpha_dict = {' ' : ' '}
        
        for i in range(len(keys)):
            if i > 25:
                i = 0
            alpha_dict[keys[i]] = alphabet_list[i]
            
        
        for context in message:
            result += alpha_dict[context]
            
        return result       
```