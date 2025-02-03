---
title:  "leetcode - 58. Length of Last Word"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
string

## 문제
![problem](https://github.com/user-attachments/assets/50e6de2b-a245-4b74-bbe6-b96ec604a251)
{: .align-center}

주어진 단어의 마지막 길이를 반환하라


## 입출력 예시
### 예시 1
```
입력: s = "Hello World"
출력: 5
설명: 마지막 단어는 길이가 5인 "World"입니다.
```

### 예시 2
```
입력: s = "fly me to the moon "
출력: 4
설명: 마지막 단어는 길이가 4인 "moon"입니다.
```

### 예시 3
```
입력: s = "luffy is still joyboy"
출력: 6
설명: 마지막 단어는 길이가 6인 "joyboy"입니다.
```

## 조건
- 1 <= s.length <= $10^{4}$
- s영어 문자와 공백으로만 구성됩니다 ' '.
- . 에는 최소한 하나의 단어가 들어있을 것입니다 s.


## 문제풀이
1. 주어진 문자열을 `trim`(공백제거) 한다.
2. 마지막 요소부터 반복하면서 문자열의 길이를 샌다.
3. 샌 갈이를 리턴한다.

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int length = 0;
        s = s.trim();
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                break;
            }
            length++;
        }
        
        return length;
    }
}
```