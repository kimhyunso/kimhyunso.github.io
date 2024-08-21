---
title: "팩토리 패턴 (Factory Pattern)"
layout: single
categories:
  - designpattern
tags:
  - Factory
  - DesignPattern
  - 디자인 패턴
  - 팩토리패턴
---

## 디자인 패턴
변경되는 요구사항들에 문제를 어떻게 해결해 나갈 것인지에 대한 해결방안 모음들 :: **정답이 아님**

## 팩토리 패턴
인스턴스를 용도에 맞게 만드는 패턴

1. 팩토리 패턴
2. 팩토리 메소드 패턴


### 팩토리 패턴

### 구현클래스 
```java
public abstract class Animal {

    protected String name;
    protected int age;

    public void eat() {
        System.out.println(name + " 음식을 먹는다.");
    }

    public abstract void speek();

    public void info() {
        System.out.println("이름은 : " + name + " 나이는 : " + age + "살 입니다.");
    }
}

public class Dog extends Animal {

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public void speek() {
        System.out.println("멍멍");
    }
}

public class Cat extends Animal {

    public Cat(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public void speek() {
        System.out.println("야옹");
    }
}

public enum Type {
    CAT, DOG;

    public Animal isType(String name, int age) {
        if (this == CAT) {
            return new Cat(name, age);
        }
        return new Dog(name, age);
    }
}
```

### 팩토리 클래스

```java

public class AnimalFactory {
    private String name;
    private int age;

    public AnimalFactory(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public  Animal getAnimal(Type type) {
        return type.isType(name, age);
    }

    public AnimalFactory init(String name, int age) {
        this.name = name;
        this.age = age;
        return this;
    }
}

Animal animal = null;

AnimalFactory factory = new AnimalFactory("멍돌이", 5);
animal = factory.getAniaml(Type.DOG);
animal.info(); // 이름은 : 멍돌이 나이는 : 5살 입니다.
animal.speek(); // 멍멍

factory.init("로미냥", 3);
animal = factory.getAniaml(Type.CAT);
animal.info(); // 이름은 : 로미냥 나이는 : 3살 입니다.
animal.speek(); // 야옹
```

## 팩토리 메소드 패턴
만약, 요구 사항이 추가되어 갑자기 강아지에 책가방을 추가해야한다.

또한, 고양이는 사냥할 일이 없어져 발톱이 없어져버렸다.

어떻게 위의 코드에서 변경을 할 것인가?

`Dog` 클래스와 `Cat` 클래스에 추가를 하게될 것이다.

만약, 요구사항이 더 많아진다면 어떻게 해야할까?

`Dog` 클래스와 `Cat` 클래스에 많은 요구사항들을 집어넣어야한다.

`Dog` 팩토리와 `Cat` 팩토리를 나누어 그 안에서 요구사항들을 변경처리한다면 고유한 `domain`은 변하지 않고 유연하게 처리할 수 있을 것이다.

### 구현 클래스

```java
public abstract class Animal {

    protected String name;
    protected int age;

    public void eat() {
        System.out.println(name + " 음식을 먹는다.");
    }

    public abstract void speek();

    public void info() {
        System.out.println("이름은 : " + name + " 나이는 : " + age + "살 입니다.");
    }
}

public class Dog extends Animal {

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public void speek() {
        System.out.println("멍멍");
    }
}

public class Cat extends Animal {

    public Cat(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public void speek() {
        System.out.println("야옹");
    }
}
```

### 팩토리 메소드 패턴

```java
public abstract class AnimalFactory {
    protected String name;
    protected int age;
    
    public abstract Animal createAnimal();
}


public class DogFactory extends AnimalFactory {

    public DogFactory(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    @Override
    public Animal createAnimal() {
        return new Dog(name, age);
    }

    public Dog tieBag(Animal animal) {
        System.out.println("책가방을 맨다.");
        return (Dog) animal;
    }
}

public class CatFactory extends AnimalFactory {
    
    public CatFactory(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    @Override
    public Animal createAnimal() {
        return new Cat(name, age);
    }

    public Cat lostClaw(Animal animal) {
        System.out.println("발톱이 없어졌어요 ㅠㅠ");
        return (Cat) animal;
    }
}

Animal animal = null;
DogFactory dogFactory = new DogFactory("멍돌이", 5);
animal = dogFactory.createAnimal();
animal = dogFactory.tieBag(animal); // 책가방을 맨다.

CatFactory catFactory = new CatFactory("로미냥", 3);
animal = catFactory.createAnimal();
animal = catFactory.lostClaw(animal); // 발톱이 없어졌어요 ㅠㅠ
```



