---
title:  "99클럽 코테 스터디 22일차 TIL - 스택/큐"
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
스택/큐

# 오늘 공부한 내용
스택/큐, `remove()`, `pop()`, 인덱스 슬라이싱

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

처음에는 배열들을 `reverse()` 한 후에 학생이 선호하는 샌드위치가 아닐 경우 `pop()`을 시키고 `append()`를 하면 될 것 같다는 바보같은 생각을 했다.

배열들을 `reverse()`하고 `pop()`을 진행하게 된다면 자기자신을 다시 `append()`하고 무한 반복을 하게된다.

다음으로 생각한 것은 첫번째 있는 학생요소와 샌드위치요소를 비교하여 같다면 인덱스 슬라이싱을 통해 현재 배열을 덮어쓰는 방식으로 풀이하면 될 것이라 생각했다.

문제는 조건문이였다.

처음에는 무한루프를 작성했다가 실패했다.

다음번에는 샌드위치 리스트 안에 학생요소가 없다면 반복을 돌 수 있도록 적용을 했다.

조건을 적용한 후, 위의 생각한 풀이방식을 적용하니 `index out of range` 오류가 나왔다.

차근차근 디버깅을 통해 보니 반복하면서 학생들 리스트와 샌드위치의 리스트가 전부 `pop()`이 되어 빈리스트가 나오는 것이였다. 그래서 `lenth`를 비교할 수 있도록 조건문을 보강하게 되었다.

결과는 통과였다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/756bfd0b-0d45-4d1e-878f-316693c1d806)
{: .align-center}

다른 사람들의 풀이를 보니 어떤 사람은 `Counter` 라이브러리를 통해 풀이한 사람이 있었다.

`Counter`는 **중복되는 갯수를 새는 것**이다. 다음 예시와 같다.

### `Counter` 예시
```python
from collections import Counter
result = [1, 1, 0, 0]
Counter(result) # {1 : 2, 0 : 2}
```

오늘은 다른사람의 풀이도 보고 스택과 인덱스 슬라이싱에 대해서 다시 상기하는 좋은 시간이였다.

내일도 다른 사람의 풀이를 보고 이렇게 풀 수도 있다는 것을 배울 수 있도록 노력해야겠다.

# 결과물
## 문제내용

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6cf48f79-536e-4d47-a0a1-855c6ba372f7)
{: .align-center}

## 풀이 방법
### 나의 문제 풀이방법
1. 샌드위치 리스트 안에 요소가 있고 학생요소 안에 샌드위치 요소가 없을 때까지 반복한다.
2. 만약 학생의 0번째 요소와 샌드위치의 0번째 요소가 같다면 학생 리스트와 샌드위치 리스트 1번째 요소부터 마지막 요소까지 인덱스 슬라이싱을 한다.
3. 만약 학생 요소가 있다면 첫번째 학생요소를 학생 리스트의 맨 뒤로 보낸다.
4. 마지막으로 학생 요소의 갯수를 반환한다.

```python
# 나의 문제 풀이
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        index = 0
        
        while len(sandwiches) > 0 and students[index] in sandwiches:

            if students[index] == sandwiches[index]:
                students = students[index + 1:]
                sandwiches = sandwiches[index + 1:]

            if students:
                students.append(students.pop(index))
            
        return len(students)
```

### 다른 사람의 문제 풀이
1. `Counter`를 사용하여 학생요소의 중복된 갯수를 `myCounter` 변수에 할당한다.
2. 샌드위치가 `myCounter` 없을 경우 `break`
3. 샌드위치가 `myCounter`에 있을 경우 -1을 통해 줄여나간다.
4. 마지막으로 `myCounter`의 갯수를 반환한다.

```python
# 다른사람의 문제 풀이
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

