---
title:  "leetcode - 80. Remove Duplicates from Sorted Array II"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array 중복 요소 제거

## 문제
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

![RemoveDuplicatesfromSortedArrayII](https://github.com/user-attachments/assets/48d35c19-94da-43c2-80a7-de2161a5fa94)
{: .align-center}

배열 안의 중복된 요소들을 제거하고 해당 배열의 요소 사이즈를 리턴하라

단, 추가적인 memory 배열을 선언하지 않아야한다.

## 입출력 예시
### 예시 1
```
입력: nums = [1,1,1,2,2,3]
출력: 5, nums = [1,1,2,2,3,_]
```
### 예시 2
```
입력: nums = [0,0,1,1,1,1,2,3,3]
출력: 7, nums = [0,0,1,1,2,3,3,_,_]
```

## 조건
- 1 <= nums.length <= $3 * 10^4$
- $-10^4$ <= nums[i] <= $10^4$
- nums내림차순이 아닌 순서 로 정렬됩니다 .


## 문제풀이
1. 비교 요소와 다음 요소들을 비교하여 같다면 중복횟수를 카운팅한다.
2. 카운팅된 값이 2이상이면 비교 요소의 값을 `int`의 max 값인 21억으로 변경한다.
3. 변경된 데이터를 카운팅한다.
4. 배열의 요소들을 내림차순으로 정렬한다.
5. 배열의 사이즈에서 변경된 데이터를 카운팅한 값의 차이를 리턴한다.

다음 그림과 같다.

![ForExample](https://github.com/user-attachments/assets/c763955a-2c99-4960-9534-3e531d3f2662)
{: .align-center}


```java
import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
        int modifyCount = 0;
        for (int i = 0; i < nums.length; i++) {
            int duplicateCount = 0;
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    duplicateCount++;
                }

                if (duplicateCount >= 2) {
                    nums[i] = Integer.MAX_VALUE;
                    modifyCount++;
                    break;
                }
            }
        }
        Arrays.sort(nums);
        return nums.length - modifyCount;
    }
}
```