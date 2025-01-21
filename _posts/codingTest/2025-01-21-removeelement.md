---
title:  "leetcode - 27. Remove Element"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array 요소 제거

## 문제
https://leetcode.com/problems/remove-element/description/

![removeElements](https://github.com/user-attachments/assets/37a5ed97-6aa4-44dd-bd96-558344894b97)
{: .align-center}

배열 안의 요소를 제거하고 배열 사이즈를 리턴하라

## 입출력 예시
### 예시 1
```
입력: nums = [3,2,2,3], val = 3
출력: 2, nums = [2,2,_,_]
```

### 예시 2
```
입력: nums = [0,1,2,2,3,0,4,2], val = 2
출력: 5, nums = [0,1,4,0,3,_,_,_]
```

## 조건
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100


## 문제풀이
1. arraylist를 선언
2. val과 nums 요소가 같지 않다면 arraylist 삽입
3. nums 배열에 arraylist 요소 대입
4. arraylist의 사이즈 반환

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int removeElement(int[] nums, int val) {
          List<Integer> numbers = new ArrayList<>();
          for (int num : nums) {
              if (num != val) {
                  numbers.add(num);
              }
          }

          for (int i = 0; i < numbers.size(); i++) {
              nums[i] = numbers.get(i);
          }
          return numbers.size();
    }
}
```