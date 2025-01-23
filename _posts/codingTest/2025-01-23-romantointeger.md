---
title:  "leetcode - 13. Roman to Integer"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
로마 문자를 숫자로 변경


## 문제
https://leetcode.com/problems/roman-to-integer/description

![problem](https://github.com/user-attachments/assets/2a3c5335-b533-449f-aa03-32f90a1a317d)
{: .align-center}

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

위와 같이 심볼을 값으로 바꾸어 누적하여 리턴하라

단, 하기와 같이 6가지의 경우가 있다.

1. IV = 4, IX = 9
2. XL = 40, XC = 90
3. CD = 400, CM = 900

## 입출력 예시
### 예시 1
```
입력: s = "III"
출력: 3
```

### 예시 2
```
입력: s = "LVIII"
출력: 58
```

### 예시 3
```
입력: s = "MCMXCIV"
출력: 1994
```

## 조건
- 1 <= s.length <= 15
- s문자만 포함합니다 ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- 범위 내의 유효한 로마 숫자  가 보장 됩니다 .s[1, 3999]

## 문제풀이
1. map에 key: I, V, X, L, C, D, M, value: 값을 대입한다.
2. 반복문을 돌며 두 요소를 비교한다. (예를들어 첫번째 요소와 두번째 요소)
3. 만약 두 요소 중 두번째 요소가 더 크다면 첫번째 요소만큼 뺀다.
4. 다르다면 첫번째 요소를 누적한다.
5. 마지막으로 더해지지 않은 마지막 요소를 누적한 값을 리턴한다.

```java
import java.util.*;

class Solution {
    public int romanToInt(String s) {
        int res = 0;
        int romanLength = s.length() - 1;
        Map<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        for (int i = 0; i < romanLength; i++) {
            if (roman.get(s.charAt(i)) < roman.get(s.charAt(i + 1))) {
                res -= roman.get(s.charAt(i));
            } else {
                res += roman.get(s.charAt(i));
            }
        }

        return res + roman.get(s.charAt(romanLength));
    }
}
```
