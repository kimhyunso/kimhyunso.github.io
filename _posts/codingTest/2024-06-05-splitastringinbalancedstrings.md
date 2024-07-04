---
title:  "99클럽 코테 스터디 5일차 TIL - 그리디 알고리즘"
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
그리디 알고리즘

# 오늘 공부한 내용
파이썬 리스트 push 하는 방법, if문을 사용하여 객체 안이 비어있는지 판별하는 방법

# 오늘의 회고
오늘은 L자 문자가 온 후 R자문자가 오면 카운팅을 하는 문제를 해결하였다.

처음 문제를 보고 스택을 사용하면 풀 수 있을 것이라고 생각했다.

스택을 사용해서 같은 문자가 들어오면 push하고 다른 문자가 들어오면 pop을 한다음

현재 스택이 비어있는지 확인한다. 비어있다면 갯수를 샌다.

쉬울 것이라고 생각했는데 몇가지 어려운 난관이 있었다.

첫번째로 객체가 비어있는 지 판단하는 방식이 나름 어려웠다.

값이 있다면 `True` / 없다면 `False`

```python
string = ''
if string:  # False
    print('string 안에 값이 없습니다.') 

string = '홍길동'
if string:  # True
    print('string 안에 값이 있습니다.')

lists = []
if lists:   # False
    print('배열 안에 값이 없습니다.')

lists = [1, 2]
if lists:   # True
    print('배열 안에 값이 있습니다.')
```

이런 부분과 더불어 리스트안에 데이터를 넣는 방법을 몰라 인터넷을 통해 찾아보기도 했다. `push()` 인줄 알았더니 `append()`였다..

이번에는 차분히 R이 스택에 들어왔을 때, L이 스택에 들어왔을 때의 상황들을 차근차근 해나가면서 풀어보았다.

차근차근 풀어보니 2시간이라는 시간이 지나고 어찌저찌 통과는 하게 되었다.

![통과](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/bac2df82-6217-426c-8d8f-67c06841c0b1)
{: .align-center}

하지만 다른 사람들의 풀이를 한번 확인해보았다.

그런데 나의 생각과는 다르게 단순한 로직이였다.

왼쪽의 갯수를 새고 오른쪽의 갯수를 샌 후 두 결과가 같으면 왼쪽갯수, 오른쪽 갯수의 변수를 0으로 만들고 카운팅을 하는 것이였다.

통과를 하긴 했지만 스택을 써야겠다는 생각이 굳어진 다음부터는 아무 생각도 하지 않고 구현에만 집작하여 풀이를 푼것 같다.

항상 되풀이하지만 잘 안되는 다른 방식의 접근들도 생각을 해볼 필요성이 있을 것 같다.

다음 문제는 한가지 생각에만 몰두되지 말고 다른 여러가지의 생각들을 해보고 직접 써가면서 패턴을 찾아 풀이를 해봐야겠다.

# 결과물
## 문제내용
문자열이 밸런스가 있다.

L의 갯수와 R의 갯수가 같은지 판단한다.

## 예시
![예시내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/172b2e6d-9c58-4936-b2e3-c7c364920afb)
{: .align-center}

만약 RLRRLLRLRL이라면 RL -> 1, RRLL -> 2, RL -> 3, RL -> 4 로서 4가된다.

## 풀이방법
스택을 사용하여 풀었다.

전의 문자 : prev_word / 현재 문자 : word

1. 문자를 스택에 push를 한다.
2. 전에 문자가 있는지 판단 후 전의 문자와 현재 문자가 같은지 판단한다.
3. 같다면 스택에 있는 데이터를 pop한다.
4. 다르면서 전의 문자가 비어있다면(= '') 스택에 push를 한 후 전의 문자를 비어준다.
5. 만약 스택이 비어있다면 갯수를 새고 전의 문자를 비어준다.
6. 다르다면 스택에 있는 데이터를 pop한다.

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        stack = []

        prev_word = ''

        for word in s:
            stack.append(word)
            if prev_word and prev_word != word:
                stack.pop()
         
            elif prev_word:
                stack.append(prev_word)
                prev_word = ''
                
            if not stack:
                answer += 1
                prev_word = ''
            else:
                prev_word = stack.pop()
                
        return answer

# 테스트 코드
solution = Solution()
solution.balancedStringSplit('RLRRLLRLRL')
```













