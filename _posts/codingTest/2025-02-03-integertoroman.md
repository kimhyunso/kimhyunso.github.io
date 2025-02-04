---
title:  "leetcode - 12. Integer to Roman"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
Integer to Roman

## 문제
- https://leetcode.com/problems/integer-to-roman


![problem](https://github.com/user-attachments/assets/f100c9af-911f-459d-aad3-4e4a6a100848)
{: .align-center}

정수가 주어지면 해당 정수를 로마 숫자로 변경하라

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
입력: num = 3749
출력: "MMMDCCXLIX"
설명:
3000 = MMM은 1000(M) + 1000(M) + 1000(M)으로 표현 
 700 = DCC는 500(D) + 100(C) + 100(C)으로 표현 
  40 = XL은 50(L)에서 10(X)을 뺀 값으로 표현 
   9 = IX는 10(X)에서 1(I)을 뺀 값으로 
표현 주: 49는 변환이 소수점 자릿수를 기준으로 하기 때문에 50(L)에서 1(I)을 뺀 값이 아닙니다.
```

### 예시 2
```
입력: num = 58
출력: "LVIII"
설명:
50 = L 
 8 = 8
```

### 예시 3
```
입력: num = 1994
출력: "MCMXCIV"
설명:
1000 = M 
 900 = CM 
  90 = XC 
   4 = IV
```

## 조건
- 1 <= num <= 3999

## 문제풀이
1. map을 초기화한다. (순서가 있는 map을 만들기 위해 무조건 `LinkedHashMap`으로 초기화한다.) map에 위의 로마숫자들을 초기화한다.
2. map의 key만큼 반복하며 주어진 num과 map의 value를 나누었을 때 0이 아니라면 해당 key값을 builder에 append시킨다.
3. num를 value만큼 나눈 나머지로 변경한다. (ex: 321 % 100 = 21)
4. builder에 append된 string을 `return` 한다.



```java
class Solution {
    public String intToRoman(int num) {
        Map<String, Integer> dictionary = new LinkedHashMap<>();
        StringBuilder result = new StringBuilder();

        dictionary.put("M", 1000);
        dictionary.put("CM", 900);
        dictionary.put("D", 500);
        dictionary.put("CD", 400);
        dictionary.put("C", 100); 
        dictionary.put("XC", 90);
        dictionary.put("L", 50);
        dictionary.put("XL", 40);
        dictionary.put("X", 10);
        dictionary.put("IX", 9);
        dictionary.put("V", 5);
        dictionary.put("IV", 4);
        dictionary.put("I", 1);

        Set<String> keys = dictionary.keySet();
        for (String key : keys) {
            int value = dictionary.get(key);
            int condition = num / value;
            if (condition != 0) {
                for (int i = 0; i < condition; i++) {
                    result.append(key);
                }
            }
            num %= value;
        }

        return result.toString();
    }
}
```