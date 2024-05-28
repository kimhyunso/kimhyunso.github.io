---
title:  "함수형 자바"
layout: single
categories:
    - functional
tags:
    - o'reilly
    - 함수형 프로그래밍
---

# SAM
1. `Function<T, R>`
2. `Consumer<T>`
3. `Supplier<T>`
4. `Predicate<T>`

## `Funcional<T, R>`
하나의 입력값에 대해 하나를 반환함
- T : 입력값
- R : 반환값
```java
@FunctionalInterface
public interface Function<T, R>{
    R apply(T t);
    // ...
}
```

## `Consumer<T>`
입력을 해도 반환하지 않음
- T : 입력값
```java
@FunctionalInterface
public interface Consumer<T>{
    void accept(T t);
    // ...
}
```