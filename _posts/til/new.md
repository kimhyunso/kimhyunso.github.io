# 분할정복
## merge sort
1. 주어진 배열을 둘로 나눈다
2. 두 subarray 각각 정렬한다 (재귀)
3. 정렬된 두 subarray를 합쳐 하나의 정렬된 배열을 만든다.

Recursion Tree

## Binary Search
- 정렬된 배열

## 곱셈
- 카라츠바 알고리즘

x = 10^m a+b, y = 10^m c+d (m = [n/2])

xy = (10^m a+b)(10^m c+d) = 10^2m ac + 10^m bc + ad+ bd

bc + ad = ac + bd - (a - b)(c- d)

# DP (동적계획법)
중복된 계산 값을 줄이자

부분문제들의 값들을 저장하고 재사용하자

- 올바른 점화식을 찾는 것

1. 점화식 찾기
2. 답을 차곡차곡 table에 쌓아가는 방식으로 설계

### 피보나치
F_n = F_n-1 + F_n-2

T(n) = T(n - 1) + T(n - 2) + 1

T(n) > F_n

```
prev = 1
curr = 0

for i <- i to n
    next <- curr + prev
    prev <- curr
    curr <- next
return curr
```

### 점화식 유도방식
최단경로의 수 세기

2가지 

왼쪽 위, 오른쪽 아래

### LCS
A = m, B = n

1. A != B
max{L(i -1, j), L(i, j -1)}

2. A == B
max{
    L(i -1,j),
    L(i, j-1),
    L(i-1, j-1) + 1
}



# Greddy (탐욕법)


# Backtraking


