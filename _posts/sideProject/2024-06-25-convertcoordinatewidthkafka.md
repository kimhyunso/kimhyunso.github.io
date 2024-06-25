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

![Group 114](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/df6dc5e4-b390-4e87-a9d0-4db10d34d9da)
{: .align-center}

### server


### broker

### zookeeper


### producer
티켓을 발행하는 자


### consumer
구독을 한 토픽에 대한 데이터를 처리하는 자


### topic
일종의 티켓






















