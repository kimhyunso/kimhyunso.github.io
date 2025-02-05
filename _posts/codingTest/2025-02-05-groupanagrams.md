---
title:  "leetcode - 49. Group Anagrams"
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

![problem](https://github.com/user-attachments/assets/d6ff44e2-0c40-44f7-ae03-3f806f5363cc)
{: .align-center}

주어진 문자열에서 에너그램으로 변환이 가능한 문자열들을 묶어 리턴하라.

## 입출력 예시
### 예시 1
```
입력: strs = ["먹다","차다","탄","먹었다","나트","박쥐"]
출력: [["bat"],["nat","tan"],["ate","eat","tea"]]
설명:
strs에는 재배열하여 형성할 수 있는 문자열이 없습니다 "bat".
문자열 "nat"과 "tan"문자는 재배열되어 서로를 형성할 수 있으므로 애너그램이라고 합니다.
문자열 "ate", "eat", 는 "tea"서로를 형성하도록 재배열될 수 있으므로 애너그램이라고 합니다.
```

### 예시 2
```
입력: strs = [""]
출력: [[""]]
```

### 예시 3
```
입력: strs = ["a"]
출력: [["a"]]
```

## 조건
- 1 <= strs.length <= $10^{4}$
- 0 <= strs[i].length <= 100
- strs[i]소문자 영어 글자로 구성됩니다.

## 문제풀이
- 핵심: map을 아래 예시와 같이 초기화하는 것이 목적이다.
- key는 정렬된 문자열이며, value는 해당 문자열의 인덱스이다.

### 예시
```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

map = { 
    "aet" : [0, 1, 3],
    "ant" : [2, 4],
    "bat" : [5]
}
```

1. 위의 예시 처럼 될 map과 인덱스 리스트, 문자열을 임시적으로 정렬시켜놓을 배열을 선언한다.
2. 문자열들을 정렬하며 임시적으로 선언한 문자열 배열에 대입한다.
3. 위의 예시와 같이 key가 만약 존재한다면 이미 존재한 배열리스트에 `append` 시키고, 만약 key가 존재하지 않을 경우 새로운 리스트를 만들어 인덱스를 삽입한다.
4. 만들어진 map에 있는 데이터를 순회하면서 해당 인덱스에 있는 문자열들을 그룹화하여 리턴한다.

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<Integer>> counter = new HashMap<>();
        List<Integer> indexs = new ArrayList<>();
        List<List<String>> answer = new ArrayList<>();    
        String[] tempStr = new String[strs.length];

        for (int i = 0; i < strs.length; i++) {
            char[] words = strs[i].toCharArray();
            Arrays.sort(words);
            tempStr[i] = new String(words);
        }

        for (int i = 0; i < strs.length; i++) {
            if (counter.containsKey(tempStr[i])) {
                indexs = counter.get(tempStr[i]);
            } else {
                indexs = new ArrayList<>();
            }

            indexs.add(i);
            counter.put(tempStr[i], indexs);
        }

        for (String key : counter.keySet()) {
            List<Integer> value = counter.get(key);
            List<String> group = new ArrayList<>();
            for (int i = 0; i < value.size(); i++) {
                group.add(strs[value.get(i)]);
            }
            answer.add(group);
        }

        return answer;
    }
}
```