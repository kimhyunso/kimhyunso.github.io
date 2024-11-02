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

그렇다면 추상클래스가 인터페이스보다 더 범위가 넓은 것인가?

정답은 아니라고 생각된다.

여러 개의 클래스가 같은 행동을 하지만, 다른 행동을 하는 클래스들도 존재할 것이다.

동물을 예를 들어 다음 코드를 보자

```java
public abstract class Animal {
    abstract void sleep();
    abstract void eat();
    void poop() {
        System.out.println("똥을 싼다.");
    }
}

public interface Flyable {
    void fly();
}

public interface Swimable {
    void swimming();
}

public class Bear extends Animal {
    @Override
    public void sleep() {
        System.out.println("저녁에 잠을 잔다.");
    }

    @Override
    public void eat() {
        System.out.println("과일을 먹는다.");
    }
}

public class Bat extends Animal implements Flyable {
    @Override
    public void sleep() {
        System.out.println("아침에 잠을 잔다.");
    }

    @Override
    public void eat() {
        System.out.println("곤충을 먹는다.");
    }

    @Override
    public void fly() {
        System.out.println("하늘을 난다.");
    }
}

public class Dolphin extends Animal implements Swimable {
    @Override
    public void sleep() {
        System.out.println("좌뇌 우뇌를 번갈아 가며 잔다.");
    }

    @Override
    public void eat() {
        System.out.println("물고기를 먹는다.");
    }

    @Override
    public void swimming() {
        System.out.println("수영을 한다.");
    }
}
```

코드에서 보는 바와 같이 목적이 다르다.

`Animal`이라는 추상 클래스에는 공통적인 행동들이 정의되어 있다.

모든 동물들은 먹고, 싸고, 잔다.

하지만, 모든 동물들이 날거나 수영을 할 수 있는 것이 아니다.

이와 같이 `클래스에서 공통적인 것들(속성, 행동)`은 추상클래스에서 정의하는 것이 맞다고 생각된다.

하지만, `특정 클래스들만 할 수 있는 행동`을 정의한 것이 인터페이스라고 생각된다.

따라서, 추상클래스와 인터페이스의 차이점이라한다면 아래와 같다고 생각된다.

1. 추상클래스 - 전체적인 큰 구조를 잡는 것
2. 인터페이스 - 특정 클래스들만 할 수 있는 행동을 정의하는 것


