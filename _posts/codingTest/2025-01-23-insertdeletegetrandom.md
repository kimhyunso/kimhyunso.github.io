---
title:  "leetcode - 380. Insert Delete GetRandom O(1)"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
set


## 문제
https://leetcode.com/problems/insert-delete-getrandom-o1/description/

![problem](https://github.com/user-attachments/assets/b32c91e3-de76-4198-85f2-34b299bb9186)
{: .align-center}

그림과 같은 조건의 클래스를 만들어라


## 입출력 예시
### 예시 1
```
입력 
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"] 
[[], [1], [2], [2], [], [1], [2], []] 출력 
[null, true, false, true, 2, true, false, 2] 설명 
RandomizedSet randomizedSet = new RandomizedSet(); 
randomizedSet.insert(1); // 1을 세트에 삽입합니다. 1이 성공적으로 삽입되었으므로 true를 반환합니다. 
randomizedSet.remove(2); // 2가 세트에 없으므로 false를 반환합니다. 
randomizedSet.insert(2); // 2를 세트에 삽입하고 true를 반환합니다. 이제 세트는 [1,2]를 포함합니다. 
randomizedSet.getRandom(); // getRandom()은 1 또는 2를 무작위로 반환해야 합니다. 
randomizedSet.remove(1); // 1을 세트에서 제거하고 true를 반환합니다. 이제 집합에는 [2]가 포함됩니다. 
randomizedSet.insert(2); // 2는 이미 집합에 있었으므로 false를 반환합니다. 
randomizedSet.getRandom(); // 2가 집합에 있는 유일한 숫자이므로 getRandom()은 항상 2를 반환합니다.
```


## 조건
- -$2^{31}$ <= val <= $2^{31}$ - 1
- 최대 통화는 , , 로만 가능합니다 .2 * $10^5$ insertremovegetRandom
- 호출 되면 데이터 구조에 최소한 하나의 요소가 있게 됩니다 getRandom.

## 문제풀이
1. 생성자에서 set을 초기화한다.
2. `insert`시에 `set.add()`를 호출한다.
3. `remove`시에 `set.remove()`를 호출한다.
4. random에서는 set을 배열로 변경한 뒤, random클래스를 사용하여 set사이즈 만큼의 random한 값을 반환한다.


```java
import java.util.*;

class RandomizedSet {
    Set<Integer> set;

    public RandomizedSet() {
        set = new HashSet<>();
    }
    
    public boolean insert(int val) {
        return set.add(val);
    }
    
    public boolean remove(int val) {
        return set.remove(val);
    }
    
    public int getRandom() {
        Random random = new Random();
        return (int) set.toArray()[random.nextInt(set.size())];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```
