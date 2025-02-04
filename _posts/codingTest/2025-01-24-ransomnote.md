---
title:  "leetcode - 383. Ransom Note"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
map

## 문제
- https://leetcode.com/problems/ransom-note


![problem](https://github.com/user-attachments/assets/c286ed18-3c31-441d-91ef-1c57ab5bed12)
{: .align-center}

ransomNote와 magazine이라는 두 문자열이 주어졌을 때, magazine에 있는 글자를 사용하여 ransomNote를 만들 수 있으면 true를 반환하고, 그렇지 않으면 false를 반환하라

magazine에 있는 각 글자는 ransomNote에서 한 번만 사용할 수 있다.

## 입출력 예시
### 예시 1
```
입력: ransomNote = "a", magazine = "b"
출력: false
```

### 예시 2
```
입력: ransomNote = "aa", magazine = "ab"
출력: false
```

### 예시 3
```
입력: ransomNote = "aa", magazine = "aab"
출력: true
```


## 조건
- 1 <= ransomNote.length, magazine.length <= $10^5$
- ransomNote소문자 영어 문자로 구성 됩니다 magazine.

## 문제풀이
1. map을 초기화한다.
2. map = key: `magazine.charAt()` / value: count값
3. 만약 ransomNote의 character값이 map에 존재하지 않거나, map의 count값이 0 이하라면 `false`
4. map에 존재하고 0 초과라면 map의 count값을 -1 뺀다
5. 마지막은 `true`를 리턴한다.


```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();
        
        for (char key : magazine.toCharArray()) {
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        for (char key : ransomNote.toCharArray()) {
            if (!map.containsKey(key) || map.get(key) <= 0) {
                return false;
            }
            map.put(key, map.get(key) - 1);
        }

        return true;
    }
}
```





