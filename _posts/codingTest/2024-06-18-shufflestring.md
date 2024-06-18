---
title:  "99클럽 코테 스터디 18차 TIL - 문자열"
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
`''.join()`함수, `dictional` 사용법, 리스트 `insert()` 함수

# 오늘의 회고

오늘 문제는 주어진 문자열을 주어진 인덱스 배열대로 섞는 것이였다.

처음에는 주어진 문자열을 리스트로 쪼개고 리스트를 하나 만들어 `insert(주어진 인덱스, 쪼갠 문자열 리스트)` 이렇게 구해진 리스트를 `join()` 함수를 통해 합치면 될 것이라고 생각했다.

그러나 `insert()`함수를 사용하니 반복문을 돌 수록 만든 리스트가 점차 늘어가는 것이였다.

이 방법은 아닌 것 같아 다른 방법을 시도했다.

### 첫번째 시도
```python
s = "codeleet", indices = [4,5,6,7,0,2,1,3]
result = [''] * len(s)

for i in range(len(s)):
    result.insert(indices[i], s[i])

return ''.join(result)
```

두번째 방법은 `dictional`에 key가 indices 리스트값이고 value가 s를 `split()`한 값을 넣었다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/f60fd665-19b3-4473-9ef2-cb4915f5c7f8)
{: .align-center}


오늘은 `dictional`와 리스트의 `insert()`함수를 공부할 수 있어서 좋았다.

내일도 한가지씩 알아갈 수 있도록 노력해야겠다.


# 결과물
## 문제내용


## 풀이 방법

```python
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restore_dict = {}
        result = ''
        
        for i in range(len(s)):
            restore_dict[indices[i]] = s[i]
        
        
        sort_index = sorted(restore_dict.keys())
        
        for i in sort_index:
            result += restore_dict[i]
        
        return result
```