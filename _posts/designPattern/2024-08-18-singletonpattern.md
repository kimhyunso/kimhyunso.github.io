---
title: "싱글톤 패턴 (Singleton Pattern)"
layout: single
categories:
  - designpattern
tags:
  - Singleton
  - DesignPattern
  - 디자인 패턴
  - 싱글톤패턴
---

## 디자인 패턴
변경되는 요구사항들에 문제를 어떻게 해결해 나갈 것인지에 대한 해결방안 모음들 :: **정답이 아님**

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
















