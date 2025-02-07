---
title:  "leetcode - 392. Is Subsequence"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
문자열

## 문제
- https://leetcode.com/problems/is-subsequence/

![problem](https://github.com/user-attachments/assets/2f118fe0-ed2b-4498-bc24-7b35e5e636af)
{: .align-center}

문자열 s, t 두 개가 주어진다. 

문자열 s가 t의 부분수열인지 확인하여 맞다면 `true`, 아니라면 `false`를 리턴하라


## 입출력 예시
### 예시 1
```
입력: s = "abc", t = "ahbgdc"
출력: true
```

### 예시 2
```
입력: s = "axc", t = "ahbgdc"
출력: false
```

## 조건
- 0 <= s.length <= 100
- 0 <= t.length <= $10^{4}$
- st소문자 영어 글자로만 구성됩니다 .


## 문제풀이
- 조건에 s.length와 t.length의 곲이 10000000 까지이기 때문에 $O(N^{2})$ (이중반복문)으로도 가능할거라 판단했다.

1. `s.length`와 `t.length`가 0미만이면 `false`를 리턴한다.
2. 이중반복문을 도는데 s의 문자들에 대해 t의 문자와 같은지 판단한다.
3. 만약에 s문자와 t의 문자가 같다면 t 문자열을 같은 문자 다음 문자부터 t 문자열 마지막까지 t에 덮어쓰고, count 갯수를 샌다. 그리고 t 문자열에 s 문자가 중복되어 있을 경우를 대비하여 `break`를 사용하였다.
4. count와 s의 `length`가 같은지 판별하여 리턴한다.


```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() < 0 || t.length() < 0) {
            return false;
        }
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char target = s.charAt(i);
            for (int j = 0; j < t.length(); j++) {
                char sequence = t.charAt(j);
                if (target == sequence) {
                    t = t.substring(j + 1, t.length());
                    count++;
                    break;
                }
            }
        }

        return count == s.length();
    }
}
```