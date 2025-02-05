---
title:  "leetcode - 242. Valid Anagram"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
string, map

## 문제
- https://leetcode.com/problems/group-anagrams/description/

![problem](https://github.com/user-attachments/assets/9ceae3af-c3c2-4f8a-bb45-62aeb42b1863)
{: .align-center}

주어진 두 문자를 애너그램 형태로 변경이 가능하다면 `true`, 아니면 `false`를 리턴하라

## 입출력 예시
### 예시 1
```
입력: s = "아나그램", t = "나가람"
출력 : true
```

### 예시 2
```
입력: s = "쥐", t = "자동차"
출력 : false
```


## 조건
- 1 <= s.length, t.length <= 5 * $10^{4}$
- s소문자 영어 문자로 구성 됩니다 t.

## 문제풀이
- 핵심 : 아래 예시와 같이 map을 구성한다.
- map의 key: 문자, value: 문자 카운트 숫자
- s의 문자들을 카운트 한 후에 t 문자를 카운트를 빼서 모든 숫자가 0이라면 `true`, 0이 아닌 것이 있다면 `false`

### 예시
```python
s = 'anagram'

map = {
    'a' : 3,
    'n' : 1,
    'g' : 1,
    'r' : 1,
    'm' : 1
}
```

1. map을 초기화한다.,
2. 위의 예시와 같이 만들기 위해 map을 key: 문자, value: 문자 카운트한 수로 만든다.
3. 주어진 t 문자열에서 문자들을 key가 같다면 value에서 뺀다.
4. 만약에 map안에 0이 아닌 value가 존재한다면 `false`를 리턴한다.
5. 위의 경우가 아닌 경우에 해당하니 `true`를 리턴한다.

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> counter = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char key = s.charAt(i);
            counter.put(key, counter.getOrDefault(key, 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            char key = t.charAt(i);
            counter.put(key, counter.getOrDefault(key, 0) - 1);
        }

        for (char key : counter.keySet()) {
            int value = counter.get(key);
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
}
```