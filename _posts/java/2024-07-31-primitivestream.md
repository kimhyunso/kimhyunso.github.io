---
title:  "스트림 사용하기"
layout: single
categories:
  - java
tags:
  - o'reilly
  - 함수형 프로그래밍
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

```java
record User(UUID id, String group, LocalDateTime lastLogin, List logEntries) {}
```

### 요소변환
1. `Collectors.groupingBy`

사용자가 지정한 요소로 그룹을 묶는 방법 키-값 형태

```java
import static java.util.stream.Collectors.*;
List<User> users = new ArrayList<User>();

users.add(new User(UUID.randomUUID(), "student", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "student", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "student", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "admin", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "admin", LocalDateTime.now(), null));

Map<String, List<User>> userGroups = users.stream()
                .collect(groupingBy(User::group));

for (String group : userGroups.keySet()) {
    System.out.println(userGroups.get(group));
}
```

2. `Collectors.mapping`
요소들을 매핑하는 것

```java
import static java.util.stream.Collectors.*;
List<User> users = new ArrayList<User>();

users.add(new User(UUID.randomUUID(), "student", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "student", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "student", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "admin", LocalDateTime.now(), null));
users.add(new User(UUID.randomUUID(), "admin", LocalDateTime.now(), null));

Map<String, Set<UUID>> userGroups = users.stream()
                .collect(groupingBy(User::group, mapping(User::id, toSet())));

for (String group : userGroups.keySet()) {
    System.out.println(userGroups.get(group));
}
```

### 요소축소


































































