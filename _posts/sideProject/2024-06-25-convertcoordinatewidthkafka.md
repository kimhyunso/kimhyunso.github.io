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

- 환경 : docker, local(mac)
- 사용 언어 : python, javascript
- 사용 프레임워크 : Nodejs, Kafka
- 데이터베이스 : postgresql/postgis

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

## 카프카 만들기 docker-compose
```yml
version: '3'
 
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.0.0
    hostname: zookeeper
    container_name: zookeeper
    environment:
      ZOOKEEPER_SERVER_ID: 1 # 주키퍼를 식별하는 아이디로 유일한 값, 1개의 주키퍼를 사용할 예정이라 없어도 문제 없음
      ZOOKEEPER_CLIENT_PORT: 2181 # 주키퍼 포트, 기본 포트로 2181 사용
      ZOOKEEPER_TICK_TIME: 2000 # 클러스터를 구성할 때 동기화를 위한 기본 틱 타임
 
  broker:
    image: confluentinc/cp-kafka:7.0.0
    container_name: broker
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1 # 카프카의 브로커 아이디로 유일한 값, 1개의 브로커를 사용할 예정이라 없어도 문제 없음
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181' # 주키퍼에 연결하기 위한 대상 지정 [서비스이름:컨테이너내부포트]
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_INTERNAL:PLAINTEXT # 보안을 위한 프로토콜 매핑. PLAINTEXT는 암호화하지 않은 일반 평문
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092,PLAINTEXT_INTERNAL://broker:29092 # 외부 클라이언트에 알려주는 리스너 주소
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1 # 토픽 복제에 대한 설정 값
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1 # 트랜잭션 최소 ISR(InSyncReplicas 설정) 수
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1 # 트랜잭션 상태에서 복제 수
```

```sh
$ docker-compose -f {fileName.yml} up
```

## 도커 내부터미널 진입
![docker프로세스 확인](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/03e74613-6337-4bf2-af35-77a540b74aeb)
{: .align-center}

![docker터미널진입](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/c2dd08a6-e9eb-45b0-8dbb-ea5671715198)
{: .align-center}

```sh
$ docker ps
$ docker exec -it {containerID} /bin/bash
```


## 토픽 만들기
![토픽만들기](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/1e448b71-8ff2-4c8e-8848-e45671bd532e)
{: .align-center}

```sh
$ kafka-topics --bootstrap-server localhost:9092 --create --topic topic --partitions 3 --replication-factor 1
```

## 토픽 리스트 확인하기
![토픽리스트확인하기](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6c406dfb-2fb9-4a3a-9dd4-342b38f6c3af)
{: .align-center}

```sh
$ kafka-topics --list --bootstrap-server localhost:9092
```

## 토픽 삭제하기
```sh
$ kafka-topics --delete --bootstrap-server localhost:9092 --topic topic2
```

## lag 확인하기
```sh
$ kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group test-group1
```


이번 포스팅에서는 kafka 설정 및 토픽 생성 작업을 진행하였다. 다음 포스팅에서는 producer와 consumer에 대해서 포스팅할 예정이다.


































