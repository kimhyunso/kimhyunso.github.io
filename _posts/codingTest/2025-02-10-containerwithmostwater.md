---
title:  "leetcode - 11. Container With Most Water"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
투포인터

## 문제
- https://leetcode.com/problems/container-with-most-water/description/

![leetcodeproblem](https://github.com/user-attachments/assets/9c0d6d0a-5ca1-4a07-af72-a4f0a6bc30a2)
{: .align-center}

물이 흘러 넘치지 않게 용기를 저장할 수 있는 최대치 값을 구하여라. 

자세한 사항은 예시를 보자

## 입출력 예시
### 예시 1
![leetcodeexample](https://github.com/user-attachments/assets/8d6d6731-9ef3-408b-8fd6-6bcaa903e66c)
{: .align-center}
```
입력: 높이 = [1,8,6,2,5,4,8,3,7]
출력: 49
설명: 위의 수직선은 배열 [1,8,6,2,5,4,8,3,7]로 표현됩니다. 이 경우 용기가 담을 수 있는 최대 물 면적(파란색 부분)은 49입니다.
```

### 예시 2
```
입력: 높이 = [1,1]
출력: 1
```

## 조건
- n == height.length
- 2 <= n <= $10^{5}$
- 0 <= height[i] <= $10^{4}$


## 문제풀이
- 핵심: 최소 높이와 width (인덱스)를 곱한 면적이 가장 큰 것을 고르는 것

1. left, right를 초기화한다. left는 0, right는 height의 length - 1이다.
2. left가 작을때 까지 반복하면서 최소 높이와 인덱스를 곱한 면적 값을 구한다.
3. 면적값과 `return`할 `int`값 중 가장 큰 값을 대입하도록 한다.
4. 만약 왼쪽에 있는 값이 오른쪽 값보다 작다면 left의 인덱스 위치값을 증가 시키고, 아니라면 right의 인덱스 위치값을 감소시킨다.
5. 3번에서 구한 가장 큰 값을 리턴한다.

```java
class Solution {
    public int maxArea(int[] height) {
        int result = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int area = (right - left) * Math.min(height[left], height[right]);
            result = Math.max(result, area);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return result;
    }
}
```
