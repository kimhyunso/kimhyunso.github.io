---
title:  "JAVA 함수형 프로그래밍 - 람다"
layout: single
categories:
  - java
tags:
  - o'reilly
  - 함수형 프로그래밍
  - 람다
---

## 람다 익명함수 (anonymous method)
인터페이스는 `new`연산자 사용 시, 구현체가 없기 때문에 함수를 `Override`해야 한다.

```java
@FunctionalInterface
public interface Lambda {
    public int sum(int x, int y);
}

Lambda lambda = new Lambda() {
    @Override
    public int sum(int x, int y){
        return x + y;
    }
}

int result = lambda.sum(10, 20);
System.out.println(result); // 30
```

## 람다 문법
`(<parameter>) -> {<body>}`

## 람다 변수 캡쳐
스코프에 있는 변수를 획득하는 것

불필요한 캡쳐 사용을 피하는 것이 좋음

캡쳐를 당하는 변수가 Effectively final이여야 한다는 필요성

```java
void capture() {
    int answer = 42;

    Runnable printAnswer = () -> System.out.println("정답 : " + answer);

    run(printAnswer);
}

void run(Runnable runnable) {
    runnable.run();
}

capture(); // 정답 : 42
```

## Effectively final
초기화 된 이후 값이 한 번도 변경되지 않는 것

변수를 `final`로 선언하면 됨

```java
final List<String> fruitList = new ArrayList<>();

Runnable addItem = () -> wordList.add("apple");
addItem.run(); // fruitList : [apple]
```

## 익명 클래스
인터페이스를 구현체에 상속시키지 않고 `new`연산자를 통해 override 시켜 구현하는 것

```java
@FunctionalInterface
public interface HelloWorld<T> {
    T sayHello(String name);
}

// 익명 클래스
HelloWorld<String> helloWorld = new HelloWorld() {
    @Override
    public String sayHello(String name){
        return "Hello " + name + " World!";
    }
};

helloWorld.sayHello("gildong");

// 람다
HelloWorld<String> helloWorld = name -> "Hello " + name + " World!";
helloWorld.sayHello("poodle");
```
