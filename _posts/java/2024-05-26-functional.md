---
title:  "JAVA 함수형 프로그래밍 - SAM"
layout: single
categories:
  - java
tags:
  - o'reilly
  - 함수형 프로그래밍
---

## SAM (Single Abstract Method)
하나의 추상 메소드만 존재하는 것

추상 메소드 이외의 다른 메소드 사용 가능

```java
@FunctinoalInterface
public interface Predicate<T> {
    boolean test(T t);

    default Predicate<T> and(Predicate<? super T> other) {
        // ...
    }

    static <T> Predicate<T> isEqual(Object targetRef) {
        // ...
    }
    // ...
}
```

## SAM (Single Abstract Method)
1. `Function<T, R>`
2. `Consumer<T>`
3. `Supplier<T>`
4. `Predicate<T>`

## `Funcional<T, R>`
하나의 매개변수에 대해 하나의 결과를 반환

> T : 매개변수 타입
>
> R : 반환타입

```java
@FunctionalInterface
public interface Function<T, R> {
    R apply(T t);
    // ...
}

Function<Integer, Integer> result = x -> x * 2;
result.apply(10); // 20
```

## `Consumer<T>`
매개변수는 있으며 반환은 `Void`

> T : 매개변수 타입

```java
@FunctionalInterface
public interface Consumer<T> {
    void accept(T t);
    // ...
}

Consumer<String> result = name -> System.out.println(name);
result.accept("hongildong"); // hongildong
```

## `Supplier<T>`
매개변수 X 반환 O

> T : 반환타입

```java
@FunctionalInterface
public interface Supplier<T> {
    T get();
    // ...
}

Supplier<String> result = () -> "Hello World!";
result.get(); // Hello World!
```

## `Predicate<T>`

> T : 매개변수 타입
>
> `boolean` : 반환값

```java
@FunctionalInterface
public interface Predicate<T> {
    boolean test(T t);
    // ...
}

Predicate<Integer> result = x -> x > 10;
result.test(20); // true
```

## 합성함수

> `andThen()`
> 
> `compose()`

```java
Function<String, String> hello = input -> input;
Function<String, String> world = input -> input + " World!";

hello.andThen(world)
    .apply("Hello"); // Hello World!

world.compose(hello)
    .apply("Hi"); // Hi World!
```
