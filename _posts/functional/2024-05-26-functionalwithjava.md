---
title:  "함수형 자바"
layout: single
# categories:
#     - functional
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

## 람다 변수 캡쳐
스코프에 있는 변수를 획득하는 것

불필요한 캡쳐 사용을 피하는 것이 좋음

캡쳐를 당하는 변수가 Effectively final이여야 한다는 필요성
```java
void capture(){
    int answer = 42;

    Runnable printAnswer = () -> System.out.println("정답 : " + answer);

    run(printAnswer);
}

void run(Runnable runnable){
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
인터페이스를 구현체에 상속시키지 않고 `new`연산자를 통해 override 시켜 사용하는 것
```java
@FunctionalInterface
public interface HelloWorld<T>{
    T sayHello(String name);
}

// 익명 클래스
HelloWorld<String> helloWorld = new HelloWorld(){
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
