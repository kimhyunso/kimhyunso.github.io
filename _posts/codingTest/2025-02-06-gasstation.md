---
title:  "leetcode - 134. Gas Station"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
array

## 문제
- https://leetcode.com/problems/gas-station/description/

![problem](https://github.com/user-attachments/assets/1ecdd689-98c6-4300-8132-280edf182558)
{: .align-center}

무제한 가스 탱크가 달린 차가 있다. 다음 주유소까지 `cost[i]` 만큼의 비용이 들며, 각 주요소의 가스 주유량은 `gas[i]`이다.

주요소 중 한 곳에서 출발 하여 순환 경로를 따라 다시 시작 주요소에 도달할 수 있다면 시작 주요소의 위치를 리턴하고 아니라면 -1을 리턴하라


## 입출력 예시
### 예시 1
```
입력: 가스 = [1,2,3,4,5], 비용 = [3,4,5,1,2]
출력: 3
설명: 
스테이션 3(인덱스 3)에서 시작하여 가스 4단위로 채웁니다. 귀하의 탱크 = 0 + 4 = 4 
스테이션 4로 이동합니다. 귀하의 탱크 = 4 - 1 + 5 = 8 
스테이션 0으로 이동합니다. 귀하의 탱크 = 8 - 2 + 1 = 7 
스테이션 1로 이동합니다. 귀하의 탱크 = 7 - 3 + 2 = 6 
스테이션 2로 이동합니다. 귀하의 탱크 = 6 - 4 + 3 = 5 
스테이션 3으로 이동합니다. 비용은 5입니다. 귀하의 가스는 스테이션 3으로 돌아가기에 충분합니다. 
따라서 시작 인덱스로 3을 반환합니다.
```

### 예시 2
```
입력: 가스 = [2,3,4], 비용 = [3,4,3]
출력: -1
설명: 
다음 스테이션으로 이동할 가스가 충분하지 않으므로 스테이션 0이나 1에서 시작할 수 없습니다. 
스테이션 2에서 시작하여 4단위의 가스로 채워 보겠습니다. 탱크 = 0 + 4 = 4 
스테이션 0으로 이동합니다. 탱크 = 4 - 3 + 2 = 3 
스테이션 1로 이동합니다. 탱크 = 3 - 3 + 3 = 3 
가스 4단위가 필요하지만 3개만 있으므로 스테이션 2로 돌아갈 수 없습니다. 
따라서 어디에서 시작하든 회로를 한 바퀴 돌 수 없습니다.
```

## 조건
- n == gas.length == cost.length
- 1 <= n <= $10^{5}$
- 0 <= gas[i], cost[i] <= $10^{4}$

## 문제풀이
1. 가스 주유량의 총합보다 비용의 총합이 더 작다면 -1을 리턴한다. (가스 주유량보다 비용이 높기 때문에 순환할 수 없다)
2. 현재 차량의 가스에 가스 주유량 - 비용을 대입한다.
3. 현재 차량의 가스가 만약에 0보다 작다면 (다음 주요소로 이동할 수 없음) 현재 주유소에서 출발할 수 없으므로 차량의 가스를 0, start 포인트를 현재 주요소 + 1을 하여 다음 주요소의 시작 인덱스를 보관한다.
4. 주요소의 시작 인덱스를 리턴한다.


```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (sum(gas) < sum(cost)) {
            return -1;
        }

        int currentGas = 0;
        int start = 0;

        for (int i = 0; i < gas.length; i++) {
            currentGas += gas[i] - cost[i];
            if (currentGas < 0) {
                currentGas = 0;
                start = i + 1;
            } 
        }
        return start;
    }

    public int sum(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }
}
```