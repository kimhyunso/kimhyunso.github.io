---
title:  "leetcode - 14. Longest Common Prefix"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
투포인터

## 문제
- https://leetcode.com/problems/longest-common-prefix/description/

![14problem](https://github.com/user-attachments/assets/c3decf32-9294-47b3-94a2-7ca9bf3a6a70)
{: .align-center}

문자열 배열이 주어진다. 

문자열 배열에서 접두사가 중복되는 것을 리턴하라

## 입출력 예시
### 예시 1
```
입력: strs = ["flower","flow","flight"]
출력: "fl"
```

### 예시 2
```
입력: strs = ["dog","racecar","car"]
출력: ""
설명: 입력 문자열 사이에 공통된 접두사가 없습니다.
```

## 조건
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i]비어 있지 않으면 소문자 영어 문자로만 구성됩니다.


## 문제풀이
1. 주어진 문자 배열의 0번째 문자열을 초기화한다.
2. 주어진 문자 배열 만큼 반복문을 돈다.
3. 현재 문자열의 length와 1번에서 초기화한 문자열의 length 중 가장 작은 것을 선택하여 다시 반복한다.
    1. 같은 문자가 있다면 endIndex를 +1 하고,
    2. 같은 문자가 없다면 break하여 3번을 빠져나온다.
4. 1번에서 초기화한 문자열의 `substring()`을 사용하여 0부터 endIndex까지 덮어쓴다.
5. 1번에서 초기화한 문자열을 리턴한다.

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {     
        String word = strs[0];

        for (int i = 1; i < strs.length; i++) {
            int endIndex = 0;
            int from = Math.min(strs[i].length(), word.length());
            for (int j = 0; j < from; j++) {
                char target = strs[i].charAt(j);
                if (target == word.charAt(j)) {
                    endIndex++;
                } else {
                    break;
                }
            }
            word = word.substring(0, endIndex);
        }

        return word;
    }
}
```


