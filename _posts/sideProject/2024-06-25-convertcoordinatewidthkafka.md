---
title:  "좌표변환 - 3부 (kafka)"
layout: single
categories:
  - sideproject
tags:
  - kafka
  - nodejs
  - consumer
  - producer
---

## 하고자 하는 목표
간단한 x좌표와 y좌표가 있는 csv파일을 업로드 시키면 알아서 좌표로 변환 후 엑셀파일로 변환시켜주는 자동화 작업을 하고 싶음

사실상 대규모의 트래픽을 감당하고 있지 않기 때문에 (대략 20000~3000건의 데이터 처리) 카프카를 사용할 이유는 없다.

> 환경 : docker
>
> 사용 프레임워크 : Nodejs, Kafka, fastAPI
>
> 데이터베이스 : postgresql/postgis

## kafka
> 사용이유 : 데이터가 많지는 않지만 엑셀 자동화 작업을 위해 시트 마다 토픽을 부여하여 consumer가 처리한 결과물을 `merge`하면 될 것이라 생각했기 때문에 사용하게 되었다.

![카프카구조](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6c69b3f6-49f8-46e3-9534-74698219e841)
{: .align-center}

### broker
데이터 저장소

### zookeeper
상태관리 하는 역활

### producer
티켓을 발행하는 자

### consumer
구독을 한 토픽에 대한 데이터를 처리하는 자

데이터 consumse을 하게되면 `commit`을 통해 current offset을 +1 증가시킨다.

#### current-offset
해당 컨슈머가 처리해야 하는 데이터 순번

#### log-end-offset
데이터가 쌓여있는 순번

#### lag
> log-end-offset - current-offset

![lag확인](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/f603fb06-e517-4667-a71c-df4d3b5eb0ae)
{: .align-center}

### consumer group
특정 토픽을 구독한 consumer들의 집합

### topic
produer가 발행한 티켓

### partition
하나의 topic을 여러개의 파티션으로 나눔으로써 하나의 컨슈머가 담당하여 데이터를 처리하는 것이 아닌 여러 컨슈머가 데이터를 각자 처리할 수 있도록 분산시키는 것

![partition](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/fcbdfe90-b20a-45db-88e6-8b9dc7fd2395)
{: .align-center}


## producer
nodejs를 사용했다.







## consumer
전의 포스팅에서 fastAPI를 사용하여 테스팅해본 것을 fastAPI를 제거하고 consumer로써 사용했다.









































