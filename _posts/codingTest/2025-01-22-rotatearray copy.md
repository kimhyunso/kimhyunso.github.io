---
title:  "leetcode - 136. Single Number"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array 중복되지 않은 요소 찾기

## 문제
https://leetcode.com/problems/single-number/description/

![problem](https://github.com/user-attachments/assets/ee53d470-ef8d-42c5-b3b9-95650b48b7a2)
{: .align-center}

배열 중 중복되지 않는 요소를 찾아서 리턴하라


## 입출력 예시
### 예시 1
```
입력: nums = [2,2,1]
출력 : 1
```

### 예시 2
```
입력: nums = [4,1,2,1,2]
출력 : 4
```

### 예시 3
```
입력: nums = [1]
출력 : 1
```


## 조건
- 1 <= nums.length <= 3 * $10^4$
- -3 * $10^4$ <= nums[i] <= 3 * $10^4$
- 배열의 각 요소는 두 번 나타나지만, 그 중 한 요소는 한 번만 나타납니다.

## 문제풀이
1. map을 선언한다. map의 형식은 key: 배열의 요소, value: 요소 갯수이다.
2. 배열만큼 반복하면서 map을 위와 같은 형식으로 초기화해준다.
3. value를 확인하여 만약에 value가 1이라면 해당 key값을 변수에 대입한다.
4. key값을 담은 변수를 리턴한다.

```java
import java.util.*;

class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        int result = 0;

        for (int i = 0; i < nums.length; i++) {
            counter.put(nums[i], counter.getOrDefault(nums[i], 0) + 1);
        }

        for (int key : counter.keySet()) {
            if (counter.get(key) == 1) {
                result = key;
                break;
            }
        }

        return result;
    }
}
```
