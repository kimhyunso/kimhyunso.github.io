---
title:  "99클럽 코테 스터디 13일차 TIL - 배열"
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
배열

# 오늘 공부한 내용
배열

# 오늘의 회고
오늘은 문제가 쉽지않았다

문제는 room에 학생들의 현재위치와 빈 좌석들이 있을때 학생들이 최소로 움직여 빈 좌석으로 이동한다고 할때

최소의 합을 구하는 문제였다.

문제에 대해 고민하던 찰나 생각해보니 두 배열(=학생들, 빈 좌석들)을 반대로 정렬하고 

두 배열의 0번째 인덱스 ~ n번째 인덱스까지의 차이를 구한 후 모두 합하면 학생들의 움직임이 최소로되는 합이라는 것을 깨달았다.

### 예시
```python
seats = [2, 2, 6, 6] 
students = [1, 3, 2, 6]
# 반대로 정렬
seats = [6, 6, 2, 2] 
students = [6, 3, 2, 1]

seats[0] - student[0] = 0
seats[1] - student[1] = 3
seats[2] - student[2] = 0
seats[3] - student[3] = 1

0 + 3 + 0 + 1 = 4
```

처음에는 잘 되지 않았다. 이유는 무조건 빼기만 하면 음수가 나오기 때문에 결과값이 음수가 될 수 있기 때문이다.

따라서 절대값을 사용하거나 또는 `max`값에서 `min`값을 빼는 방식으로 다시 구현했다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/1e254639-0cee-4f9d-b95f-7759f24e87fd)
{: .align-center}

내일은 좀 더 분발할 수 있도록 노력해야겠다!

# 결과물
## 문제내용

학생들의 현재 위치와 빈 좌석들이 존재할때

학생들을 최소로 움직인 합계를 구하라

![Minimum Number of Moves to Seat Everyone 문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/53b75285-8767-4a7d-8b23-1f8f33e0fcc5)
{: .align-center}


## 풀이 방법
1. seats, students 배열들을 반대로 정렬시킨다.
2. 학생들이나 빈좌석만큼 반복하며, 좌석과 학생의 위치 값 중 큰 것과 작은 것의 차이를 구해 합계를 구한다.


```python
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort(reverse=True)
        students.sort(reverse=True)
        result = 0
        
        for i in range(len(seats)):
            result += max(seats[i], students[i]) - min(seats[i], students[i])
            
        return result
```







