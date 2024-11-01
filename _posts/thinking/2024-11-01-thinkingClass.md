---
title:  "클래스에 대해 생각해보기"
layout: single
categories:
  - thinking
tags:
  - 생각정리
  - 클래스
---

## 클래스
흔히 클래스는 속성(property), 행동(method)로써 구분된다.

그런데 인터페이스와 추상 클래스라는 개념이 존재한다.

인터페이스와 추상 클래스의 차이점은 무엇일까?

편히 자바 언어를 사용하여 표현하도록 하겠다.

## 인터페이스
클래스간 공통된 메소드 추상화라고 생각된다.

인터페이스를 상속 받는다면 추상화 메소드를 무조건 상속 받아야한다.

```java
public interface Move {
    void move();
}

public class Bike implements Move {
    @Ovrride
    public void move() {
        // ... 기능 정의
    }
}

public class Main {
    public static void main(String[] args) {
        Move moveObject = new Bike();
        moveObject.move();
    }
}
```

## 추상클래스
클래스간 공통적으로 사용할 수 있는 메소드 정의도 가능하고, 

메소드 추상화도 가능하며 속성도 정의가 가능하다.

```java
public abstract class Vehicle {
    protected int speed;

    abstract void move();
}


public class Bike extends Vehicle {
    @Ovrride
    public void move() {
        // ... 기능 정의
    }
}

public class Main {
    public static void main(String[] args) {
        Move moveObject = new Bike();
        moveObject.move();
    }
}
```




