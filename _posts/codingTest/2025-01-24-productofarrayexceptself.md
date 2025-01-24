---
title:  "leetcode - 238. Product of Array Except Self"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
배열 순회


## 문제
https://leetcode.com/problems/product-of-array-except-self/description/

![problem](https://github.com/user-attachments/assets/26ab7a40-df2b-48a3-93bf-bdedfc42d271)
{: .align-center}

배열에서 순회시, 자신의 요소를 제외한 나머지 요소의 곱을 리턴하라.

단, 나눗셈은 사용불가하고 $O(n)$ 안에 통과해야한다.

## 입출력 예시
### 예시 1
```
입력: nums = [1,2,3,4]
출력: [24,12,8,6]
```

### 예시 2
```
입력: nums = [-1,1,0,-3,3]
출력: [0,0,9,0,0]
```

## 조건
- 2 <= nums.length <= $10^5$
- -30 <= nums[i] <= 30
- 입력은 32비트 정수 에 맞도록 생성answer[i] 됩니다 .


## 문제풀이
1. parameter 배열 크기만큼의 배열을 선언하고 1로 초기화한다.
2. 왼쪽부터 차례대로 곱해나간다.
3. 오른쪽부터 차례대로 곱해나간다.
4. 결과를 리턴한다.

2 ~ 3번 풀이는 아래 그림과 같다.

![ForExample](https://github.com/user-attachments/assets/89e012a6-6724-4c51-a68e-af9faf797826)
{: .align-center}

중요한 것은 왼쪽과 오른쪽으로 순회하며 값을 누적해 나가는 것이다.

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            answer[i] = 1;
        }

        int left = 1;
        for (int i = 0; i < nums.length; i++) {
            answer[i] *= left;
            left *= nums[i];
        }

        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }
        return answer;
    }
}
```





