---
title:  "leetcode - 28. Find the Index of the First Occurrence in a String"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
string

## 문제
![problem](https://github.com/user-attachments/assets/87d70a5a-0eaf-4e83-a146-93abf4a60b84)
{: .align-center}

haystack문자열에서 needle문자열이 있다면 0을 반환하고 없다면 -1을 반환하라.


## 입출력 예시
### 예시 1
```
입력: haystack = "sadbutsad", needle = "sad"
출력: 0
설명: "sad"는 인덱스 0과 6에서 발생합니다. 
첫 번째 발생은 인덱스 0에서 발생하므로 0을 반환합니다.
```

### 예시 2
```
입력: haystack = "leetcode", needle = "leeto"
출력: -1
설명: "leeto"는 "leetcode"에 없으므로 -1을 반환합니다.
```

## 조건
- 1 <= haystack.length, needle.length <= $10^{4}$
- haystackneedle소문자 영어 문자로만 구성됩니다 .

## 문제풀이
1. `haystack` 변수에 `indexOf()` 함수를 사용하여 문자열을 찾는다. 


```java
class Solution {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}
```





