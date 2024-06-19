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

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/745ba923-5194-4739-9c90-c98158152252)
{: .align-center}


내일도 한가지씩 알아갈 수 있도록 노력해야겠다.


# 결과물
## 문제내용

주어진 key 문자열에서 중복을 제거하고 앞에서 26자리의 문자만 알파벳순서대로 치환한다.

주어진 message를 위에서 치환한 문자로 바꾸어 결과를 반환한다.

대신 공백은 존재해야한다.

![문제예시](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/203ae737-0bb2-4f8a-8726-ebd7a36271f7)
{: .align-center}

## 풀이 방법



```python
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keys = ''.join(dict.fromkeys(key.replace(' ', '')))
        messages = message.replace(' ', '')
        alphabet_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
        result = ''
        alpha_dict = {}
        alpha_dict[' '] = ' '
        
        
        for i in range(len(keys)):
            if i > 25:
                i = 0
            alpha_dict[keys[i]] = alphabet_list[i]
            
        
        for context in message:
            result += alpha_dict[context]
            
        return result
       
```