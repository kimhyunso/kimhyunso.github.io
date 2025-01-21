---
title:  "leetcode - 169. Majority Element"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array 중복 요소 체크

## 문제
https://leetcode.com/problems/majority-element/description/

![majorityElement](https://github.com/user-attachments/assets/522f907e-ee87-4ed2-8686-5a033021f5ba)
{: .align-center}

배열 안의 요소들 중 중복된 개수가 많은 요소를 리턴하라

## 입출력 예시
### 예시 1
```
입력: nums = [3,2,3]
출력: 3
```
### 예시 2
```
입력: nums = [2,2,1,1,1,2,2]
출력: 2
```


## 조건
- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109


## 문제풀이
1. 배열을 내림차순으로 정렬한다.
2. map에 key: 배열의 요소값, value: count값을 삽입한다.
3. map의 요소를 꺼내어 value가 가장 큰 값의 key를 저장 한다.
4. value가 가장 큰 값의 key를 리턴한다.


```java
import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        Iterator<Integer> iterator = map.keySet().iterator();
        int keyValue = 0;
        int maxValue = 0;

        while (iterator.hasNext()) {
            int key = iterator.next();
            int value = map.get(key);
            if (maxValue < value) {
                maxValue = value;
                keyValue = key;
            }
        }
    
        return keyValue;
    }
}
```