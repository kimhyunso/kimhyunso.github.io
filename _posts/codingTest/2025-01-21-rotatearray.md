---
title:  "leetcode - 189. Rotate Array"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array Rotation

## 문제
https://leetcode.com/problems/rotate-array/description/

![arrayRotation](https://github.com/user-attachments/assets/86cf458c-5b91-41c9-8499-1556083d5c81)
{: .align-center}

주어진 배열을 주어진 k만큼 오른쪽으로 회전시켜라

## 입출력 예시
## 예시 1
```
입력: nums = [1,2,3,4,5,6,7], k = 3
출력: [5,6,7,1,2,3,4]
설명: 
오른쪽으로 1단계 회전: [7,1,2,3,4,5,6] 
오른쪽으로 2단계 회전: [6,7,1,2,3,4,5] 
오른쪽으로 3단계 회전: [5,6,7,1,2,3,4]
```

## 예시 2:
```
입력: nums = [-1,-100,3,99], k = 2
출력: [3,99,-1,-100]
설명:  
오른쪽으로 1단계 회전: [99,-1,-100,3] 
오른쪽으로 2단계 회전: [3,99,-1,-100]
```

## 조건
- 1 <= nums.length <= $10^5$
- $-2^{31}$ <= nums[i] <= $2^{31}$ - 1
- 0 <= k <= $10^5$


## 틀린 문제풀이
1. k만큼 반복문을 돌린다.
2. 배열의 마지막 요소를 변수에 대입한다.
3. 배열의 길이 - 1 부터 1까지 감소하며 배열의 마지막 요소가 마지막 - 1번째 요소에게 덮어쓰도록 만든다.
4. 배열의 0번째에 2번의 변수를 대입한다.

```java
class Solution {
    public void rotate(int[] nums, int k) {
        int lastLength = nums.length - 1;
        for (int i = 0; i < k; i++) {
            int lastNum = nums[lastLength];
            for (int j = lastLength; j > 0; j--) {
                nums[j] = nums[j - 1];
            }
            nums[0] = lastNum;
        } 
    }
}
```

### 문제의 원인
위의 틀린 문제풀이는 이중 반복문을 사용했다.

문제의 요점은 첫 번째 반복에서 k만큼을 반복하고, 두 번째 반복문에서 nums.length - 1만큼 반복한다는 점이다. 빅오 표기법에 의해 아래와 같은 수식이 된다.

$O(k * (nums.length - 1))$ 

하지만 조건을 자세히 보면 k의 최대값은 $10^5$ = 1000000 nums.length의 최대값도 $10^5$ = 1000000 이다. 결국 k와 num.length를 곱하면 1000000000000이라는 말도 안되는 수치가 되어 timeout이 나게된다.

## 문제 풀이
1. k가 배열의 길이보다 커질 수 없도록 하기 위해 모듈러 연산을 한다.
2. nums배열의 첫번째부터 마지막 요소까지 거꾸로 배치되게 한다.
3. nums배열의 첫번째부터 k만큼의 요소까지 거꾸로 배치되게 한다.
4. nums배열의 k번째부터 마지막 요소까지 거꾸로 배치되게한다.

그림으로 설명한다면 다음과 같다.


![ForExample](https://github.com/user-attachments/assets/6b2b7a20-2c63-4397-8ccd-489827bda738)
{: .align-center}



여기에서의 발상은 배열을 거꾸로 뒤집은 다음 배열을 두가지로 나누어 생각하는 것이다.

1. 0 ~ k까지 배열 -> 거꾸로 뒤집는다.
2. k ~ 마지막 배열 -> 거꾸로 뒤집는다.


```java
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1); 
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;

            start++;
            end--;
        }
    }
}
```



