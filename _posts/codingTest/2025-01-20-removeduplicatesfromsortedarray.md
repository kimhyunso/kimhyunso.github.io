---
title:  "leetcode - 26.Remove Duplicates from Sorted Array"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

들어가기 앞서, 위의 코딩테스트는 `python`을 위주로 진행하였지만, java를 사용하여 다시금 코딩테스트 문제들을 풀어보려한다.

## 주제
array 중복 해결

## 문제
https://leetcode.com/problems/remove-duplicates-from-sorted-array

![RemoveDuplicatesfromSortedArray](https://github.com/user-attachments/assets/410c1825-a277-41f9-bbd9-b89b05de4b6f)

array의 중복 요소를 지우고, array의 사이즈를 출력하라.


## 입출력 예시
### 예시1
입력: `nums = [1, 1, 2]`
출력: 2, `nums = [1, 2, _]`

### 예시2
입력: `nums = [0,0,1,1,1,2,2,3,3,4]`
출력: `5, nums = [0,1,2,3,4,_,_,_,_,_]`


## 조건
- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums내림차순이 아닌 순서 로 정렬됩니다 .


## 문제풀이
### set 이용
```java
import java.util.Set;
import java.util.Iterator;
import java.util.LinkedHashSet;

class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new LinkedHashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        Iterator<Integer> iterator = set.iterator();
        for (int i = 0; i < nums.length; i++) {
            if (iterator.hasNext()) {
                nums[i] = iterator.next();
            }
        }

        return set.size();
    }
}
```

### 반복문
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] != nums[i]) {
                nums[index] = nums[i];
                index++;
            }
        }

        return index;
    }
}
```