---
title:  "99클럽 코테 스터디 22차 TIL - 스택/큐"
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
스택/큐

# 오늘의 회고
오늘의 문제는 스택과 큐를 사용하여 풀이하는 문제였다.

python은 `[]` 빈 대괄호를 선언하는 것으로 범용 자료구조이기 때문에 큐와 스택을 구현할 수 있다.

문제의 내용은 이렇다.

샌드위치를 먹을려고 하는 학생들이 있다. 

학생들은 샌드위치의 모양이 동그란 모양을 선호하는 학생이 있고, 네모난 모양을 선호하는 학생이 있다.

동그라미는 0으로 표기하고 네모난 모양은 1로 표기한다.

### 예시
```python
students = [1, 1, 0, 0]
sandwiches = [0, 0, 1, 1]
```

샌드위치는 `stack`으로 되어있다.

학생들은 줄을 서다가 자신이 선호하는 샌드위치가 아닐 경우 다시 줄을 선다.






결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/756bfd0b-0d45-4d1e-878f-316693c1d806)
{: .align-center}


# 결과물
## 문제내용

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6cf48f79-536e-4d47-a0a1-855c6ba372f7)
{: .align-center}



## 풀이 방법




```python
# 나의 문제 풀이
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        index = 0
        
        while len(sandwiches) > 0 and sandwiches[index] in students:

            if students[index] == sandwiches[index]:
                students = students[index + 1:]
                sandwiches = sandwiches[index + 1:]

            if students:
                students.append(students.pop(index))
            
        return len(students)

# 다른 사람의 문제 풀이1
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #brute
        students = deque(students)
        sandwiches = deque(sandwiches)
        check = True
        idx = 0
        while check : 
            check = False
            if len(sandwiches) != 0 :
                idx = sandwiches[0]
            for i in range(len(students)) : 
                temp = students.popleft()
                if idx == temp : 
                    sandwiches.popleft()
                    check = True
                    break
                else : 
                    students.append(temp)
        return len(sandwiches)  

# 다른사람의 문제 풀이2
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        myCounter = Counter(students)
        for sandwich in sandwiches:
            if not myCounter[sandwich]:
                break
            else:
                myCounter[sandwich] -= 1
        return myCounter.total()
```
