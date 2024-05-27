---
title:  "함수형 기초"
layout: single
# categories:
#     - functional
---

# 들어가기 앞서
자바는 함수형 프로그래밍이 아닌 객체 지향 프로그래밍을 따르고 있기 때문에 자바는 적합하지 않을 수 있다.

일부 적합하지 않은 곳은 자바가 아닌 언어를 사용 할 수 있다.


# 선언형과 명령형 프로그래밍
## 선언형 (Declarative)
- WHAT
```java
public String replaceSpace(String name){
    return name.replaceAll(" ", "");
}

String result = replaceSpace("Hello World !!"); // HelloWorld!!
```

## 명령형 (Imperative)
- 절차지형적
- HOW
```java
public String replaceSpace(String name){
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


# 순수함수와 불순함수
순수함수와 불순함수라고 하여 순수함수가 기능적으로 더 우수하다는 뜻은 아님
## 순수함수
1. 동일한 입력에 항상 동일한 출력
2. 어떤 사이드 이펙트 없이 자기 충족적 성질을 가짐
```java
public String toLowerName(String name){
    return name.toLowerCase();
}
```

## 불순함수
순수함수의 두가지 조건 중 하나라도 위반시, 불순함수로 간주
```java
public String isTest(String name){
    if (name.eqauls("test")){
        return "O"
    }
    return "X"
}
```

## 불변성
setter를 사용하지 않는 것
```java
public class Person{
    private int age;
    private String name;

    public Person(int age){
        this.age = age;
    }

    public Person(String name){
        this.name = name;
    }

    public Person(int age, String name){
        this.age = age;
        this.name = name;
    }

    public Person setName(String name){
        return new Person(name);
    }

    public Person setAge(int age){
        return new Person(age);
    }

    public Person setNameAndAge(int age, String name){
        return new Person(age, name);
    }
}
```

## 일급함수
함수를 다른 인수로 전달 및 반환값으로 사용할 수 있으며 변수에 할당할 수 있는 함수 (자바에선 불가능)

```javascript
function sayHello() {
  return "Hello ";
}
function greeting(helloMessage, name) {
  console.log(helloMessage() + name);
}

greeting(sayHello, "World!"); // Hello World!
```

## 고차 함수
일급 함수의 틍성을 바탕으로 함수를 인수로 받거나, 반환하거나 또는 두가지 모드 가능하게 해야함
```javascript
const arr1 = [1, 2, 3];

const arr2 = arr1.map(function(item) {
  return item * 2;
});

console.log(arr2); // 2, 4, 6
```
