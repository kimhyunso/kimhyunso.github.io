---
title: "싱글톤 패턴 (Singleton Pattern)"
layout: single
categories:
  - designpattern
tags:
  - Singleton
  - DesignPattern
  - 디자인 패턴
  - 싱글톤
---

## 디자인 패턴
반복적으로 일어나는 문제들을 어떻게 해결해 나갈 것인지에 대한 해결방안 :: 정답이 아님

어떻게 바뀔지 모르는 상황에서 수정을 많이 하지 않고 어떻게 대처할 것인지에 대한 방안 모음

## 싱글톤 패턴
메모리 상에 하나의 인스턴스를 생성하여 인스턴스를 공유하는 것

- keyword : `private` 생성자

```java
public class MyClass {
    private static MyClass instance;

    private MyClass() {}

    public static MyClass getInstance() {
        if (instance == null) {
            instance = new MyClass();
        }

        return instance;
    }
}

MyClass firstClass = MyClass.getInstance();
MyClass secondClass = MyClass.getInstance();

if (firstClass == secondClass) {
    System.out.println(true);
}
```
















