---
title:  "leetcode - 122. Best Time to Buy and Sell Stock II"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array Rotation

## 문제
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

![problem](https://github.com/user-attachments/assets/d1e647ac-5730-437d-bf0d-a566863246c6)
{: .align-center}

최적의 매수/매도의 합산을 구하여라

## 입출력 예시
### 예시 1
```
입력: 가격 = [7,1,5,3,6,4]
출력: 7
설명: 2일차에 매수(가격 = 1)하고 3일차에 매도(가격 = 5), 이익 = 5-1 = 4.
그런 다음 4일차에 매수(가격 = 3)하고 5일차에 매도(가격 = 6)하면 이익은 6-3 = 3이 됩니다.
총 이익은 4 + 3 = 7입니다.
```

### 예시 2
```
입력: 가격 = [1,2,3,4,5]
 출력: 4
 설명: 1일차에 매수(가격 = 1)하고 5일차에 매도(가격 = 5), 이익 = 5-1 = 4.
총 이익은 4입니다.
```

### 예시 3
```
입력: 가격 = [7,6,4,3,1]
출력: 0
설명: 긍정적인 이익을 낼 방법이 없으므로 최대 이익 0을 달성하기 위해 주식을 매수하지 않습니다.
```

## 조건
- 1 <= prices.length <= 3 * 104
- 0 <= prices[i] <= 104

## 문제풀이
각각의 간격의 합이 배열의 마지막 요소 - 첫번째 요소의 값과 항상 같다.

이유는 총 거리는 변하지 않기때문이라고 한다. (chatgpt에게 물어봄)

### 예시
```python
array = [1, 5, 100]
# (5 - 1) + (100 - 5) = 99
array = [1, 5, 30, 100]
# (5 - 1) + (30 - 5) + (100 - 30) = 99
array = [1, 3, 5, 30, 100]
# (3 - 1) + (5 - 3) + (30 - 5) + (100 - 30) = 99
...
```

1. 1 ~ 배열의 마지막 길이까지 반복한다.
2. 만약에 배열의 먼저뻔 요소가 다음 요소보다 크다면 (다음 요소 - 먼저뻔 요소)를 진행하여 누적한다.
3. 누적한 결과값을 리턴한다.

```java
class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                total += prices[i] - prices[i - 1];
            }
        }
        return total;
    }   
}
```

