---
title:  "leetcode - 151. Reverse Words in a String"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
문자열

## 문제
- https://leetcode.com/problems/reverse-words-in-a-string/

![problem](https://github.com/user-attachments/assets/9e26801a-0a74-488a-993a-b0a6188a4814)
{: .align-center}

문자열의 단어들을 반전시켜라

자간은 한 번의 공백만 허용한다.

## 입출력 예시
### 예시 1
```
입력: s = "the sky is blue"
출력: "blue is sky the"
```

### 예시 2
```
입력: s = "hello world"
출력: "world hello"
설명: 뒤집힌 ​​문자열에는 앞뒤 공백이 포함되어서는 안 됩니다.
```

### 예시 3
```
입력: s = "a good   example"
출력: "example good a"
설명: 두 단어 사이에 있는 여러 개의 공백을 반전된 문자열에서 하나의 공백으로 줄여야 합니다.
```

## 조건
- 1 <= s.length <= $10^{4}$
- s영어 문자(대문자와 소문자), 숫자, 공백을 포함합니다 ' '.
- . 에는 최소한 하나 의 단어가 있습니다 s.

## 문제풀이
1. 주어진 문자열을 공백을 기준으로 나눈다 (`split()`)
2. 나누어진 문자열 반대부터 0까지 반복한다.
   1. 나누어진 문자열의 길이가 1보다 크다면, (공백이 존재하기에 문자열 길이를 비교) `StringBuilder`에 문자열을 `append()` 한다.
3. 2-1에서 `append`된 문자열을 공백을 제거 (`trim()`) 하여 리턴한다.
   
```java
class Solution {
    public String reverseWords(String s) {
        StringBuilder appender = new StringBuilder();
        String[] words = s.split(" ");

        for (int i = words.length - 1; i >= 0; i--) {
            if (words[i].length() >= 1) {
                appender.append(words[i] + " ");
            }
        }

        return appender.toString().trim();
    }
}
```


