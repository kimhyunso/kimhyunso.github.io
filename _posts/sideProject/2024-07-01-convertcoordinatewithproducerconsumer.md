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
## 프로젝트 시작 계기
기존 API를 호출하여 주소변환 작업을 진행하고 있던 중 API를 수도 없이 호출하기 때문에 `connection faild`오류가 발생하게 되었다. 

주소를 변환 작업 도중 `connection faild` 오류가 발생하면 해당 작업이 끝난 시점부터 파일 안의 내용을 지우고 다시 시작해야된다는 단점이 있었고 Open API를 호출하다 보니 매크로가 아님을 방지하기 위해서 `sleep()`을 발생시켜 딜레이를 발생시켜야만 했다.

결과물이 나오는데 걸리는 시간이 3일이나 걸리고, 파일 데이터를 삭제하고 다시 돌리는 번거로움까지 추가되어 개발을 진행하게 되었다.

## 하고자 하는 목표
간단한 x좌표와 y좌표가 있는 csv파일을 업로드 시키면 알아서 좌표로 변환 후 엑셀파일로 변환시켜주는 자동화 작업을 하고 싶음

사실상 대규모의 트래픽을 감당하고 있지 않기 때문에 (대략 20000~3000건의 데이터 처리) 카프카를 사용할 이유는 없다.

> 환경 : docker
>
> 사용 프레임워크 : Nodejs, Kafka, fastAPI
>
> 데이터베이스 : postgresql/postgis


