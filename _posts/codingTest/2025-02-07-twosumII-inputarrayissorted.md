---
title:  "leetcode - 167. Two Sum II - Input Array Is Sorted"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
배열

## 문제
- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

![problem](https://github.com/user-attachments/assets/5a0edd91-aa01-4925-9c2f-c67aab318e27)
{: .align-center}

배열과 `target`이 주어졌을 때 해당 배열에서 `target`이 되는 인덱스 배열을 반환하라

## 입출력 예시
### 예시 1
```
입력: 숫자 = [ 2 , 7 , 11, 15 ], 목표 = 9
출력: [1, 2]
설명: 2와 7의 합은 9입니다. 따라서 인덱스 1 = 1, 인덱스 2 = 2입니다. [1, 2]를 반환합니다.
```

### 예시 2
```
입력: 숫자 = [ 2 , 3, 4 ], 목표 = 6
출력: [1, 3]
설명: 2와 4의 합은 6입니다. 따라서 인덱스 1 = 1, 인덱스 2 = 3입니다. [1, 3]을 반환합니다.
```

### 예시 3
```
입력: 숫자 = [ -1 , 0 ], 목표 = -1
출력: [1,2]
설명: -1과 0의 합은 -1입니다. 따라서 인덱스 1 = 1, 인덱스 2 = 2입니다. [1, 2]를 반환합니다.
```


## 조건
- 2 <= numbers.length <= 3 * $10^{4}$
- -1000 <= numbers[i] <= 1000
- numbers감소하지 않는 순서 로 정렬됩니다 .
- -1000 <= target <= 1000
- 테스트는 정확히 하나의 솔루션 이 존재하도록 생성됩니다 .


## 문제풀이
- 핵심: 배열의 처음 인덱스 값과 배열의 마지막 값을 더하여 `target`보다 크다면 배열의 마지막 인덱스를 감속하여 반복, `target`보다 작다면 배열의 처음 인덱스를 증가하여 반복한다. (이를 투포인터라고 한다.) [$O(N)$]

1. 처음과 끝을 변수로 지정한다.
2. 반복문을 돌며 배열의 처음 인덱스 값과 마지막 인덱스 값을 더한 것을 `target`과 비교한다.
3. 2번에서 더한 값보다 target이 크다면 처음 인덱스를 증가한다.
4. 2번에서 더한 값보다 target이 작다면 마지막 인덱스를 감소한다.
5. 결과를 담는 배열에 [start + 1, end + 1]를 담아 리턴한다.


```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;
        int[] result = new int[2];

        for (int i = 0; i < numbers.length; i++) {
            int sum = numbers[start] + numbers[end];
            if (sum > target) {
                end--;
            } else if (sum < target) {
                start++;
            }
        }

        result[0] = start + 1;
        result[1] = end + 1;

        return result;
    }
}
```

- 위의 결과와 같은 방식이지만 `for`를 `while`로 바꿨을 뿐 결과는 $O(N)$이다.


```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        return twoPoint(0, numbers.length - 1, numbers, target);
    }

    public int[] twoPoint(int start, int end, int[] numbers, int target) {
        while (start < end) {
            int number = numbers[start] + numbers[end];

            if (target == number) {
                return new int[]{start + 1, end + 1};
            } else if (number > target) {
                end--;
            } else if (number < target) {
                start++;
            }
        }
        return new int[]{-1, -1};
    }
}
```