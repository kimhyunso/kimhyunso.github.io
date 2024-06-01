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
매개변수 O 반환 O
- T : 입력타입
- R : 반환타입
```java
@FunctionalInterface
public interface Function<T, R>{
    R apply(T t);
    // ...
}
```

## `Consumer<T>`
매개변수 O 반환 X
- T : 입력타입
```java
@FunctionalInterface
public interface Consumer<T>{
    void accept(T t);
    // ...
}
```
## `Supplier<T>`
매개변수 X 반환 O
- T : 반환타입
```java
@FunctionalInterface
public interface Supplier<T>{
    T get();
    // ...
}
```

## `Predicate<T>`
매개변수 O 반환 `boolean`
- T : 매개변수
```java
@FunctionalInterface
public interface Predicate<T>{
    boolean test(T t);
    // ...
}
```

## 합성함수
- `andThen()`
- `compose()`
```java


```






