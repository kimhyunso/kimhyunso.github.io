---
title:  "JAVA 함수형 프로그래밍 - 일급함수, 일급컬렉션, 고차함수"
layout: single
categories:
  - java
tags:
  - o'reilly
  - 함수형 프로그래밍
  - 일급함수
  - 일급컬렉션
---

## JShell 실행 방법
**JDK 14버전 이상만 지원**
```shell
$ jshell -v
```

## 선언형과 명령형 프로그래밍
### 선언형 (Declarative)
- WHAT

```java
public String replaceSpace(String name) {
    return name.replaceAll(" ", "");
}

String result = replaceSpace("Hello World !!"); // HelloWorld!!
```

### 명령형 (Imperative)
- 절차지형적
- HOW

```java
public String replaceSpace(String name) {
    String result = "";
    for (int i = 0; i < name.length(); i++){
        char word = name.charAt(i);
        if (!(word == ' ')){
            result += word;
        }
    }
    return result;
}
String result = replaceSpace("Hello World !!"); // HelloWorld!!
```

## 순수함수와 불순함수
순수함수와 불순함수라고 하여 순수함수가 기능적으로 더 우수하다는 뜻은 아님

## 순수함수
1. **동일한 입력에 항상 동일한 출력**
2. 어떤 사이드 이펙트 없이 자기 충족적 성질을 가짐


```java
public String toLowerName(String name) {
    return name.toLowerCase();
}
```

## 불순함수
순수함수의 두가지 조건 중 하나라도 위반시, 불순함수로 간주
```java
public String isTest(String name) {
    if (name.eqauls("test")){
        return "O"
    }
    return "X"
}
```

## 불변성
setter를 사용하지 않는 것

```java
public class Person {
    private int age;
    private String name;

    public Person(int age) {
        this.age = age;
    }

    public Person(String name) {
        this.name = name;
    }

    public Person(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public Person setName(String name) {
        return new Person(name);
    }

    public Person setAge(int age) {
        return new Person(age);
    }

    public Person setPerson(int age, String name) {
        return new Person(age, name);
    }
}
```

## 일급함수
**함수를 다른 인수로 전달 및 반환값으로 사용**할 수 있으며 **변수에 할당할 수 있는 함수**

```java
Function<String, String> sayHello = input -> input;
Function<String, String> greeting = input -> input + " World!";

sayHello.andThen(greeting)
        .apply("Hello"); // Hello World!

greeting.compose(sayHello)
        .apply("Hello"); // Hello World!
```

## 일급컬렉션
****



## 고차 함수
일급 함수의 특성을 바탕으로 **함수를 인수로 받거나**, **반환하거나 또는 두가지 모드 가능**하게 해야함

```java
// BinaryOperator를 사용하여 두 수를 더하는 일급함수를 정의
BinaryOperator<BinaryOperator<Integer>> higherOrderFunction = (operation) -> (a, b) -> operation.apply(a, b);
```
