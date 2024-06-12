---
title:  "99클럽 코테 스터디 6일차 TIL - 그리디 알고리즘"
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
그리디 알고리즘

# 오늘 공부한 내용
`bit()` 함수, `count()` 함수, 슬라이싱, `replace()` 함수

# 오늘의 회고
오늘은 숫자를 비트로 변환시키고, 변환된 비트의 합을 출력하는 것이 과제였다.

처음에는 숫자를 먼저 비트로 변환시킨 후에 for문을 돌면서 비트의 합을 구하면 되겠구나 생각했다.

하지만 비트로 변환한 다음에는 문자열로 바뀌었는데 문자 안에 0b라는 문자가 포함되어 있었다.

포함되어 있는 0b 문자열을 없애기 위해 `replace()`함수를 사용하여 공백문자로 대체하고 for문을 돌면서 비트의 합을 구하는 로직을 구현했다.

첫번째로 통과에 성공했다. 기분은 좋았지만 간단한 로직 안헤 for문 안에 for문이라니 데이터양이 많아 n^2의 시간복잡도가 나올 수 도 있는 문제였다.

두번째로 리팩토링에 들어갔다. 첫번째로 리팩토링 한 것은 for문 안에 있는 for문을 없애는 것 이였다.

for문 안에 있는 for문은 `count()`함수를 사용해서 1의 갯수를 세는 것으로 해결했다.

두번째로 통과에 성공했다. 하지만 `replace()`함수가 굳이 필요한 것인가에 대한 고민이 들기 시작했다.

마지막으로 필요치 않은 `replace()` 함수를 없애고 항상 앞의 두자리가 0b라는 것을 생각하여 슬라이싱을 사용했다.

마지막으로 통과에 성공하게 되었다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/ce0e0c25-d0d3-42ab-8c7d-a93f0d5cbe55)
{: .align-center}

처음 해결을 할 때에는 이렇게 이렇게 만들어 나가면 되겠지 하며 되는데로 작성했다면 두번째 세번째에서 정교화하고 리팩토링을 하면서 더 많은 것을 알게된 시간인 것 같다.

다음번에도 한 번 해결했다고 해서 그만하지 않고 여러가지 다른 방법을 시도하거나 내 코드의 리팩토링 요소를 캐치해서 정교화 작업을 해나아가면 조금씩 알아가는 것이 넓어질 것 같다!

# 결과물
## 문제내용

매개변수로 넘겨준 숫자를 비트로 변환하고 변환된 비트를 더한 것을 배열에 담아 리턴한다.

![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/791c07c2-931d-48d3-940c-72f76405d045)
{: .align-center}

## 풀이방법
- `bin()` : 숫자를 비트로 변환시켜주는 함수
- `count(arg1)` : 해당 변수 안에서 arg1과 일치하는 문자의 갯수를 샌다.
- `replace(arg1, arg2)` : arg1을 arg2로 바꿔준다.
- 슬라이싱(slicing) : 인덱스를 통해 [~부터:~까지] 슬라이싱을 할 수 있다.

1. `bin()` 함수를 이용해서 bit로 변환시킨다. 
2. 변환된 숫자에서 `replace()` 함수또는 슬라이싱을 이용해서 0b 문자를 제거한다.
3. 해당 변수에서 1의 갯수를 샌다. 또는 해당 변수를 for문으로 돌려 전체의 합을 구한다.

```python
# 첫번째 풀이법
class Solution:
    def countBits(n: int) -> List[int]:
        result = []
        for num in range(n+1):
            bit_number = bin(num).replace('0b', '')
            count_sum = 0
            for i in range(len(bit_number)):
                count_sum += int(bit_number[i])
            result.append(count_sum)

        return result
# 두번째 풀이법
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            result.append(bin(num).replace('0b', '').count('1'))

        return result

# 세번째 풀이법
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            result.append(bin(num)[2:].count('1'))

        return result
```










