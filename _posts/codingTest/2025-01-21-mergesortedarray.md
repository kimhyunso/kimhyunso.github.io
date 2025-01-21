---
title:  "leetcode - 88. Merge Sorted Array"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array 병합

## 문제
https://leetcode.com/problems/merge-sorted-array/description/

![mergesortedarray](https://github.com/user-attachments/assets/d7eddbb8-f51d-43f5-8550-c78987ccda6f)
{: .align-center}

두 배열을 병합하고, 내림차순으로 정렬하라

## 입출력 예시
### 예시 1:
```
입력: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
 출력: [1,2,2,3,5,6]
```

### 예시 2:
```
입력: nums1 = [1], m = 1, nums2 = [], n = 0
 출력: [1]
```

### 예시 3:
```
입력: nums1 = [0], m = 0, nums2 = [1], n = 1
 출력: [1]
```

## 조건
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -109 <= nums1[i], nums2[j] <= 109


## 문제풀이
1. 0 ~ n, nums2의 요소 개수만큼 반복한다.
2. m = nums1의 마지막 요소 + 1 + nums2의 요소 개수만큼을 더해 해당 인덱스에 nums2를 대입한다.
3. `Arrays.sort()` 함수를 통해 num1을 정렬한다. 

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < n; i++) {
            nums1[m + i] = nums2[i];
        }
        Arrays.sort(nums1);
    }
}
```