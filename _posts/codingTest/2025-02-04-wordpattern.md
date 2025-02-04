---
title:  "leetcode - 290. Word Pattern"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
string

## 문제
- https://leetcode.com/problems/word-pattern

![problem](https://github.com/user-attachments/assets/6e658fcc-c2f8-45d4-b024-7d929b6457dc)
{: .align-center}

pattern과 문자열이 주어질 때, 하나의 문자열은 하나의 패턴에 일치한다.

pattern과 문자열이 같은 단어로 매핑되어 서로 같다면 true, 아니라면 false를 리턴하라


## 입출력 예시
### 예시 1
```
입력: 패턴 = "abba", s = "dog cat cat dog"
출력 : true
설명:
단사함수는 다음과 같이 성립할 수 있습니다.
'a'"dog"지도는 . 입니다 .
'b'"cat"지도는 . 입니다 .
```

### 예시 2
```
입력: 패턴 = "abba", s = "개 고양이 고양이 물고기"
출력 : false
```

### 예시 3
```
입력: 패턴 = "aaaa", s = "개 고양이 고양이 개"
출력 : false
```


## 조건
- 1 <= pattern.length <= 300
- pattern소문자 영어 글자만 포함합니다.
- 1 <= s.length <= 3000
- s소문자 영어 문자와 공백만 포함합니다 ' '.
- s 앞뒤 공백이 없습니다 .
- 모든 단어는 공백 하나로s 구분됩니다 .


## 문제풀이
1. map과 stringbuilder를 초기화한다.
2. words를 split하여 pattern length와 비교한 작은 값을 구해 반복문을 돈다.
3. map에 words가 없다면 집어넣는다.
4. pattern으로 map에서 찾아 builder로 string을 만든다.
5. builder로 만들어진 string과 s를 비교하여 리턴한다.

```java
class Solution {
    public boolean wordPattern(String pattern, String s) {
        StringBuilder appender = new StringBuilder();
        Map<Character, String> map = new HashMap<Character, String>();

        String[] words = s.split(" ");
        int minLength = Math.min(pattern.length(), words.length);

        for (int i = 0; i < minLength; i++) {
            char key = pattern.charAt(i);
            if (!map.containsValue(words[i])) {
                map.put(key, words[i]);
            }
        }

        for (int i = 0; i < pattern.length(); i++) {
            char key = pattern.charAt(i);
            appender.append(map.get(key) + " ");
        }


        return s.equals(appender.toString().trim());
    }
}
```