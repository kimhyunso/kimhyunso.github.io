---
title:  "leetcode - 42. Trapping Rain Water"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
투포인터

## 문제
- https://leetcode.com/problems/trapping-rain-water/description/

![42problem](https://github.com/user-attachments/assets/7aedc368-2b06-4aac-82a0-551cc960ad64)
{: .align-center}

물이 고일 수 있는 최대값을 구하여라

자세한 사항은 예시를 보며 참고해보자

## 입출력 예시
### 예시 1
![leetcodeexample](https://github.com/user-attachments/assets/fdab1b99-0cc5-462b-ac58-2f071e1ee606)
{: .align-center}

```
입력: 높이 = [0,1,0,2,1,0,1,3,2,1,2,1]
출력: 6
설명: 위의 고도 지도(검은색 부분)는 배열 [0,1,0,2,1,0,1,3,2,1,2,1]로 표현됩니다. 이 경우 6단위의 강수량(파란색 부분)이 갇힙니다.
```

### 예시 2
```
입력: 높이 = [4,2,0,3,2,5]
출력: 9
```

## 조건
- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= $10^{5}$


## 문제풀이
- 핵심: 투포인터를 사용하여 왼쪽에서 가장 큰 기둥을 찾고, 오른쪽에서 가장 큰 기둥을 찾아 값을 누적해나가는 방식

1. 투포인터를 사용할 것이기 때문에 왼쪽과 오른쪽을 초기화한다. (0, length - 1)
2. 왼쪽에서 가장 큰 기둥을 구할 변수와 오른쪽에서 가장 큰 기둥을 구할 변수를 선언한다.
3. 왼쪽이 오른쪽보다 작을 경우 반복한다.
4. maxLeft, maxRight변수에 왼쪽과 오른쪽에서 가장 큰 기둥의 값을 찾는다.
5. 결과를 리턴할 결과값에 (왼쪽에서 가장 큰 기둥 값 - 현재 기둥 값) 과 (오른쪽에서 가장 큰 기둥 값 - 현재 기둥 값)을 누적한다.
6. 만약에 왼쪽의 기둥이 오른쪽 기둥보다 이하라면 왼쪽 인덱스 값을 증가시키고 아니라면 오른쪽 인덱스 값을 감소시켜 반복한다.
7. 5번에서 누적된 결과값을 리턴한다.

```java
class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxLeft = 0;
        int maxRight = 0;
        int water = 0;

        while (left < right) {
            maxLeft = Math.max(maxLeft, height[left]);
            maxRight = Math.max(maxRight, height[right]);

            water += maxLeft - height[left];
            water += maxRight - height[right];

            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return water;
    }
}

```

