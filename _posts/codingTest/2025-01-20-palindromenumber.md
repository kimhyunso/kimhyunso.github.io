---
title:  "leetcode - 9. Palindrome Number"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
반복문

## 문제
https://leetcode.com/problems/palindrome-number/

정수가 주어지면, 첫번째 요소와 n번째 요소, 두번째 요소와 n - 1번째 요소 ...가 같다면 `true` 하나라도 틀리다면 `false`를 반환한다.

## 입출력 예시
### Example 1:
```
Input: x = 121
Output: true
```

### Example 2:
```
Input: x = -121
Output: false
```

### Example 3:
```
Input: x = 10
Output: false
```

## 조건
- -2^31 <= x <= 2^31 - 1

## 문제 풀이
1. parameter를 string으로 변환한다.
2. 변환된 string만큼 반복문을 돈다.
3. head는 처음부터 n번째 요소까지 참조한다.
4. tail은 n번째 요소부터 처음까지 참조한다.
5. head와 tail을 비교하여 다르면 `false`를 리턴한다.
6. 1~5 로직이 끝나면 `true`를 리턴한다.

```java
class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);

        for (int i = 0; i < str.length(); i++) {
            int head = str.charAt(i) - '0';
            int tail = str.charAt((str.length() - 1) - i) - '0';

            if (head != tail) {
                return false;
            }
        }

        return true;        
    }
}
```

