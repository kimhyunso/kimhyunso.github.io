---
title:  "함수형 자바"
layout: single
categories:
    - functional
tags:
    - o REILLY
    - 함수형 프로그래밍 With 자바
    - A Functional Approach to Java
---

## 람다 문법
`(<parameter>) -> {<body>}`


## SAM (Single Abstract Method)
하나의 추상 메소드만 존재하는 것

추상 메소드 이외의 다른 메소드 사용 가능
```java
@FunctinoalInterface
public interface Predicate<T>{
    boolean test(T t);

    default Predicate<T> and(Predicate<? super T> other){
        // ...
    }

    static <T> Predicate<T> isEqual(Object targetRef){
        // ...
    }
    // ...
}
```