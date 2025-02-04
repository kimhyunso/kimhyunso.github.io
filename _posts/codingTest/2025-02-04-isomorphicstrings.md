---
title:  "leetcode - 205. Isomorphic Strings"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
string

## 문제
- https://leetcode.com/problems/isomorphic-strings/description

![problem](https://github.com/user-attachments/assets/bc1e9922-e21e-47ef-b5da-093611099635)
{: .align-center}

문자열 두 개가 주어질 때, 두 개의 문자들 하나하나씩을 매핑하여 같은 문자가 되는지 판단하여 `true`, `false`를 리턴하라


## 입출력 예시
### 예시 1
```
입력: s = "계란", t = "추가"
출력 : true
설명:
문자열 s과 문자열은 t다음과 같이 동일하게 만들 수 있습니다.
'e'. 에 매핑합니다 'a'.
'g'. 에 매핑합니다 'd'.
```

### 예시 2
```
입력: s = "foo", t = "bar"
출력 : false
설명:
문자열 s및 는 모두 및 에 매핑되어야 t하므로 동일하게 만들 수 없습니다 .'o''a''r'
```

### 예시 3
```
입력: s = "논문", t = "제목"
출력 : true
```

## 조건
- 1 <= s.length <= 5 * 104
- t.length == s.length
- s, t유효한 ASCII 문자로 구성될 수 있습니다 .


## 문제풀이
1. map과 stringbuilder를 초기화한다.
2. s가 key가되고 t가 value가 되어 map을 초기화한다.
3. s의 key로 map을 조회하여 stringbuilder에 append한다.
4. stringbuilder에 append되어 있는 문자열과 비교하고자 하는 문자열 t가 같은지 비교하여 리턴한다.

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> map = new HashMap<>();
        StringBuilder appender = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char key = s.charAt(i);
            char value = t.charAt(i);
            if (!map.containsValue(value)) {
                map.put(key, value);
            }
        }

        for (int i = 0; i < s.length(); i++) {
            char key = s.charAt(i);
            appender.append(map.get(key));
        }
        
        return t.equals(appender.toString());
    }
}
```