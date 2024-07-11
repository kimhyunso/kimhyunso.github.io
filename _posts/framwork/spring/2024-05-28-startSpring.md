---
title:  "스프링 부트 시작하기"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
---

## 스프링 부트 시작
**https://start.spring.io**

## 스프링 부트 공식문서
**https://docs.spring.io/spring-boot/tutorial/index.html**

### Dependencies
필요 라이브러리 추가

### Group
> 도메인 명
>
> 예시 : naver.com
> 
> Groupid : com.naver
>
> 하위 Groupid : com.naver.map
>
> 하위 Groupid : com.naver.web

### Artifact
> 프로젝트의 이름 사용
>
> 이 이름으로 컴파일된  Jar 생성
>
> 소문자로만 작성/특수문자 사용 금지

### Name
> 물리적으로 생성되는 프로젝트명
>
> Artifact와 비슷하여 같은 이름을 쓰는 경우가 많음

## web과 was의 차이점
`web` : 정적파일 담당 (css, image 등...)

`was` : 동적 처리 담당

### 로직흐름
![로직흐름](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/796fd939-5e29-422c-8568-dceb9bc83bff)
{: .align-center}

### Web Context (=was) 구조
![webcontext](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/8eaef459-bc16-4d1b-8b7c-e93d9f8a9b17)
{: .align-center}


### Dispatcher Servelt 구조
![DispatcherServlet](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7fed0b80-eb95-4feb-a3bc-8550dd8fbc72)
{: .align-center}

### Spring Container

![스프링컨테이너](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/efd98fb4-f0ab-454e-b6de-ec7a6e3120e0)
{: .align-center}



![스프링컨테이너2](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/32df1b97-eb67-4568-8e49-0981b080bfe5)





![스크린샷 2024-05-31 오전 9 00 35](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/ce7d2768-8bbf-4bdb-983b-aa103b48b5d6)
{: .align-center}

![스크린샷 2024-05-31 오전 9 32 22](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/2b4c70a2-b675-4da3-a9f2-278e6a9ffb14)
{: .align-center}

## 뷰리졸버
> prefix : 물리적 위치
>
> suffix : 파일 확장자명

```properties
spring.mvc.view.prefix=/WEB-INF/views/
spring.mvc.view.suffix=.jsp
```





