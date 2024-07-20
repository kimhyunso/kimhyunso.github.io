---
title:  "스프링 부트 - batch"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
    - 스프링 배치
---

## 개요
들어가기 앞서, 회사에서 우연치 않게 간단한 배치작업을 개발해야하는 상황이 발생하여 내가 배운 내용들을 글로 남기고자 한다.

## 공식문서
https://docs.spring.io/spring-batch/reference/index.html

## 배치작업
대량의 작업을 한 번에 `일괄처리` 할 수 있도록 도와주는 작업

## 스케쥴링
어떠한 작업을 `특정 시간`에 작업을 실행하도록 도와주는 설정

## 배치 아키텍처
하나의 Job은 여러개의 Step을 가질 수 있으며 하나의 Step은 `ItemReader`, `ItemProcessor`, `ItemWriter`를 가질 수 있다.
![배치아키텍처](https://github.com/user-attachments/assets/c84c735c-9dfd-4c80-8905-a99b09a0163b)
{: .align-center}

## Job 구성
![job구성](https://github.com/user-attachments/assets/f44f250b-f162-4cbd-aa96-fbbab8cc2696)
{: .align-center}

## JobInstance

## JobParameters
`Job Instance`를 구분하기 위한 파라미터 

![jobParameters](https://github.com/user-attachments/assets/389615c3-46e2-4208-929a-3a2a0a5bce1d)
{: .align-center}

## JobExecution

## Step
1. Tasklet-based Step
2. Chunk-based Step

### Tasklet-based Step
중지 신호를 보낼때까지 반복해서 실행됨

### Chunk-based Step
데이터 원본의 데이터를 처리해야 하는 시나리오에서 사용됨

![step구성](https://github.com/user-attachments/assets/40f9b81f-dbd0-4992-a351-1163b97b8a70)
{: .align-center}




## StepExecution















