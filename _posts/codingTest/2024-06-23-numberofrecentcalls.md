---
title:  "99클럽 코테 스터디 23일차 TIL - 스택/큐"
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
스택/큐

# 오늘 공부한 내용
`deque`

# 오늘의 회고
오늘의 문제는 문제 내용을 이해하기가 어려웠다.

문제를 읽고 또 읽어 보아도 어떤 메커니즘으로 돌아가는지 이해가 잘 되지 않았다.

다른 블로그를 찾아 문제의 해설을 보게 되었다. (문제 풀이법은 보지 않았다.)

문제의 해설을 10번정도 읽었을 때 비로소 문제를 파악할 수 있었다.

문제 내용은 특정 시간 t마다 함수 `ping()`이 호출되고 최근 3000ms 동안 호출된 `ping()`함수의 갯수를 구하는 문제였다.

문제풀이는 리스트를 초기화 한 후 `ping()` 함수를 호출한 t시간을 `append()` 한 후 리스트의 반복문을 돌면서 (t - 3000) 보다는 크거나 같고 현재 t보다 작거나 같으면 count를 증가시키는 방법으로 풀이를 했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/12e0710b-91a3-433c-832e-ea290e00c3da)
{: .align-center}

이번 문제는 주어진 조건에 t가 10억까지라는 것을 보고 반복문으로 안될 수도 있을 것 같다는 생각을 하게 되었다.

하지만 통과는 해서 기분은 좋았지만 통과에 오래 걸린 점을 보고 다른 사람의 문제 풀이를 찾아보았다.

다른 사람의 문제 풀이를 보니 `deque` 자료구조를 사용하여 `deque` 안에 인덱스 0번째가 t - 3000보다 작을 경우 삭제하고 `deque`의 길이를 반환하는 방식으로 구성을 했다.

다른 사람의 문제 풀이를 보니 아차했다. 내일은 다른 방식도 고려를 해서 풀이할 수 있도록 노력해야겠다.

# 결과물
## 문제내용

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6b6d2717-e196-4275-ac73-c18761a810ad)
{: .align-center}

![예시](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/12350666-a6ce-4572-be4e-2d457c0a22ff)
{: .align-center}


![조건](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/d576c5e8-7e7e-41c5-96c5-c922e8d9be4d)
{: .align-center}

## 풀이 방법
### 나의 문제 풀이방법
1. requests 리스트, time을 초기화한다.
2. `ping()` 함수가 호출이 되면 t시간을 추가 시킨다.
3. requests 리스트를 순회하면서 t - 3000 보다 크거나 같고 t 보다 작거나 같은지 판단한다.
4. 같다면 갯수를 샌다.
5. 샌 갯수를 반환한다.


```python
class RecentCounter:

    def __init__(self):
        self.requests = []
        self.time = 3000

    def ping(self, t: int) -> int:
        self.requests.append(t)
        count = 0
        
        for request in self.requests:
            if t - self.time <= request and t >= request:
                count += 1
                
        return count
```


### 다른 사람의 문제 풀이
1. q를 `deque`로 초기화를 한다.
2. q안에 데이터가 존재하고 q의 0번째 인덱스가 t - 3000보다 작을경우 반복하여 맨 앞에있는 요소를 삭제한다.
3. q안에 t를 추가한다.
4. q의 길이를 반환한다.

```python
class RecentCounter:
    def __init__(self):
        self.q = collections.deque([])

    def ping(self, t):
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        self.q.append(t)
        return len(self.q)
```
