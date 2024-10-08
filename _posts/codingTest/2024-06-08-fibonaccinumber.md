---
title:  "99클럽 코테 스터디 8일차 TIL - 다이나믹 프로그래밍"
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
다이나믹 프로그래밍 (=동적프로그래밍)

# 오늘 공부한 내용
`range()` 함수

# 오늘의 회고
오늘은 어제에 이어 다이나믹 프로그래밍 문제를 풀어보았다.

어제 공부 중 피보나치 수열을 공부했기때문에 문제자체는 어렵지 않았다.

하지만 시작이 1, 1, 2, 3 이런식으로 진행이 될 줄 알았는데 0부터 시작이였다. (0 1 1 2 3)

또한 n번째 인덱스의 값을 리턴해야되는 상황이였다. 

예시로 n번째 인덱스가 4일 경우 3을 리턴해야한다.

메모이제이션기법을 활용해서 n + 1 리스트를 1로 초기화한 후, 0번째 인덱스의 값을 0으로 초기화했다.

처음에는 반복문 조건을 주는 것이 어려웠다. 생각해보니 (0, 1, 1)은 고정이니 3번째 인덱스부터 시작하면 됬었다.

앞의 조건을 찾았으니 뒤의 조건을 찾아야하는데 n = 3일 경우, 1번은 돌아야하니 n + 1인덱스까지 반복문을 돌면 될 것 같았다.

그 후로는 다이나믹 프로그래밍 기법 중 bottomUp 방식을 활용하여 3번째 인덱스 부터 n + 1까지 인덱스까지 반복문을 활용했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/1f9194a0-e74f-4491-93aa-36d58c859510)
{: .align-center}

어제 오랜시간동안 공부하고 생각을 많이 해서 그런지 어렵지는 않았다.

하지만 자만하지 않고 내일 좀 더 분발해야 할 것 같다.

# 결과물
## 문제내용
전에 있던 수와 전전에 있던 수를 더해 현재의 수를 만든다.

점화식 : $f(a_n) = f(a_{n-1}) + f(a_{n-2})$

### 예시
1, 1, 2, 3, 5, 8 ...

![피보나치](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/1494ccb9-518a-41ff-b60c-92c2d0e81dca)
{: .align-center}

## 풀이방법
동적계획법과 메모이제이션 기법을 사용하여 풀이를 했다.

1. memo 리스트를 1로 초기화한다.
2. memo의 0번째 인덱스는 0으로 초기화한다. (0, 1, 1, 2) 이런식으로 진행되기 때문
3. 3번째 인덱스 부터 n + 1 인덱스까지 반복문을 돈다 

```python
# n = 3
memo[3] = memo[2] + memo[1]
# n = 4
memo[3] = memo[2] + memo[1]
memo[4] = memo[3] + memo[2]
# n = 5
memo[3] = memo[2] + memo[1]
memo[4] = memo[3] + memo[2]
memo[5] = memo[4] + memo[3]
```
4. 마지막으로 n번째 인덱스의 값을 리턴해준다.


```python
class Solution:
    def fib(self, n: int) -> int:
        memo = [1] * (n + 1)
        memo[0] = 0

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n] 


# 테스트 케이스
solution = Solution()

print(solution.fib(5))
```

















