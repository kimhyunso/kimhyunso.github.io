---
title:  "JAVA 함수형 프로그래밍 - 스트림2"
layout: single
categories:
  - java
tags:
  - o'reilly
  - 함수형 프로그래밍
  - 스트림
---

## 원시스트림 및 박싱된 스트림
박싱된 스트림은 오토박싱을 진행하여 오버헤드가 발생한다.

|원시타입|원시 스트림|박싱된 스트림|
|-|-|-|
|`int`|`IntStream`|`Stream<Integer>`|
|`long`|`LongStream`|`Stream<Long>`|
|`double`|`DoubleStream`|`Stream<Double>`|


```java
Stream<Integer> integerStream = Stream.of(1, 2, 3, 4);

IntStream intStream = IntStream.rangeClosed(1, 4);
intStream.forEach(System.out::println); // 1, 2, 3, 4
```

## 컬렉터 (Collectors)

### 다운스트림 컬렉터
보조 스트림 파이프라인과 같음

1. 변환
2. 축소
3. 평탄화
4. 필터링
5. 복합 컬렉터 연산

































































