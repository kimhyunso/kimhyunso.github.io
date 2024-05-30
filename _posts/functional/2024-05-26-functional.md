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
하나의 매개변수에 대해 하나의 결과를 반환
> T : 매개변수
>
> R : 반환값
```java
@FunctionalInterface
public interface Function<T, R>{
    R apply(T t);
    // ...
}
Function<Integer, Integer> result = x -> x * 2;

result.apply(10); // 20
```

## `Consumer<T>`
매개변수는 있으며 반환은 `Void`
> T : 매개변수
```java
@FunctionalInterface
public interface Consumer<T>{
    void accept(T t);
    // ...
}

Consumer<String> result = name -> System.out.println(name);

result.accept("hongildong"); // hongildong
```

## `Supplier<T>`
반환값은 있고 매개변수가 없음
> T : 반환값
```java
@FunctionalInterface
public interface Supplier<T>{
    T get();
    // ...
}

Supplier<String> result = () -> "Hello World!";

result.get(); // Hello World!
```

## `Predicate<T>`
> T : 매개변수
>
> `boolean` : 반환값
```java
@FunctionalInterface
public interface Predicate<T>{
    boolean test(T t);
    // ...
}

Predicate<Integer> result = x -> x > 10;

result.test(20); // true
```
