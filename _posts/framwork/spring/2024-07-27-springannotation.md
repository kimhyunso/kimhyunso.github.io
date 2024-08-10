---
title:  "스프링 부트 - Annotation"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
    - 어노테이션
---

## 어노테이션이란
주석, 메타데이터이다. java가 컴파일할 때에 어노테이션에 맞는 형식으로 컴파일을 진행한다.

### 예시
```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component
public @interface Controller {
    @AliasFor(
        annotation = Component.class
    )
    String value() default "";
}

```

## `@Target`
해당 어노테이션을 부착가능한 **대상**

|value|설명|
|-|-|
|ANNOTATION_TYPE|어노테이션|
|CONSTRUCTOR|생성자|
|FIELD|필드 선언(enum 정수 포함)|
|LOCAL_VARIABLE|로컬변수|
|METHOD|메서드|
|PARAMETER|파라미터|
|PACKAGE|패키지|
|TYPE|클래스, 인터페이스 (어노테이션 포함), enum|

```java
public class MyController {
    @Controller  // 에러
    public MyController {}
}
```

## `@Retention(RetentionPolicy.RUNTIME)`
애노테이션의 라이프 사이클 : 애노테이션이 언제까지 살아 남아 있을 지를 정하는 것

![라이프사이클](https://github.com/user-attachments/assets/185da594-8592-4338-b556-85bd52447825)
{: .align-center}

|value|설명|
|-|-|
|SOURCE|소스코드까지 살아남는다|
|CLASS|클래스파일까지살아남는다(=바이트코드)|
|RUNTIME|런타임까지 살아남는다|



## `@Documented`
해당 어노테이션을 javadoc 파일에 추가시킬지 여부이다.














