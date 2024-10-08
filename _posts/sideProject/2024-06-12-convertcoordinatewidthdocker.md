---
title:  "좌표변환 - 1부 (Dokcer 및 postgis)"
layout: single
categories:
  - sideproject
tags:
  - docker-compose
  - docker
  - postgis
  - postgres
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

## docker 사용이유
로컬에 다운받아 사용할 수 있지만 컨테이너로 묶어서 한 번에 관리를 편리하게 하기 위해서 사용했다.

## docker-compose
컨테이너를 만들어서 알아서 묶어준다.

```shell
$ docker-compose -f docker-compose-kafka.yml up
```

### postgresql/postgis
docker-compse 명령어를 통해 서버를 구축한다. 해당 이미지는 아래 링크를 통해 버전을 설정했다.

https://registry.hub.docker.com/r/postgis/postgis/

postgresql 기본 포트는 5432이며 DB명은 gis, user명과 password는 postgres로 통일했다.

```yml
version: '3.9'
volumes:
  postgis-data:
services:
  db:
    image: postgis/postgis:14-3.4
    volumes:
      - postgis-data:/var/lib/postgresql
      - dbbackups:/backups
    environment:
      - POSTGRES_DB=gis             # db명
      - POSTGRES_USER=postgres      # user명
      - POSTGRES_PASSWORD=postgres  # password
      - ALLOW_IP_RANGE=0.0.0.0/0    # 허용 범위 : 누구나 허용
      - POSTGRES_MULTIPLE_EXTENSIONS=postgis,hstore,postgis_topology,postgis_raster,pgrouting
      - RUN_AS_ROOT=true
    ports:
      - "5432:5432"                 # 포트
    restart: on-failure
    healthcheck:
      test: "PGPASSWORD=docker pg_isready -h 127.0.0.1 -U docker -d gis"
```

![postgresql](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/168b3f5c-cbac-4967-a8f9-267dc5eef96a)
{: .align-center}

## 아래의 내용은 db테이블 및 데이터에 대해서 도와주신 분이 계셨다.

### DBeaver 설치
SQL 관리 도구로서 DBeaver를 설치했다.

https://dbeaver.io/download/


### DB Connection

> create -> connection
>
> database는 postgresql을 선택한다.
>
> db명과 username, password를 docker-compose를 통해 설정한 것과 동일하게 설정한다.

![dbeaver](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/f301e1e0-aaeb-43e3-ae01-1c7e940c3416)
{: .align-center}


![database선택](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/88c1f88c-c5b4-4491-9729-029fd4a5a04a)
{: .align-center}


![host설정](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/9cbd772a-59ca-4673-9244-abc8e53409ab)
{: .align-center}

아래 명령어를 통해 postgis가 잘 설치되었는지 확인한다.

```sql
select * from postgis_full_version();
```

![postgisversion확인](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/c833516d-e11d-4b48-9e4c-625dc67352b9)
{: .align-center}

### 대한민국 데이터

아래 링크를 통해 shp 데이터를 다운받는다.

http://www.gisdeveloper.co.kr/?p=2332

postgis에 데이터를 밀어넣기 위해서 `shp2pgsql`라는 명령어를 사용했다.

docker terminal로 접속을 한다.

![터미널접속](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/70db2239-9f4f-49f5-9212-232131e4ec69)
{: .align-center}

아래 명령어를 통해 터미널에서 postgres에 접속이 가능한지 확인한다.

```shell
$ su - postgres
$ psql
```

### 로컬 파일을 컨테이너 안으로 복사하기
> docker ps를 통해 docker contanier ID를 확인한다.
>
> docker cp [현재파일 or 디렉토리] conianierID:[이동경로] 명령어를 통해 파일을 이동시킨다.

![dockerContainerID](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/aab17f2a-0619-438e-bb54-5d170d74906d)
{: .align-center}

```shell
$ docker ps

$ docker cp MAP 99803ecc322f:/var/lib/postgresql/MAP
```

### shp2pgsql 설치하기
처음 shp2pgsql명령어가 안되서 설치방법을 찾고 다녔다.

아래 명령어를 통해 설치할 수 있었다.

```shell
$ apt-get update # 저장소 업데이트
$ apt-get install -y postgis postgresql-11-postgis-3 # shp2pgsql 안에 포함되어 있음
```

### 데이터 밀어넣기
아래 명령어를 사용하면 해당 파일들이 gis데이터베이스에 저장된다.

```shell
$ shp2pgsql -s 5179 -W cp949 ./ctprvn.shp |PGPASSWORD='postgres' psql -U postgres -d gis -q
$ shp2pgsql -s 5179 -W cp949 ./emd.shp |PGPASSWORD='postgres' psql -U postgres -d gis -q
$ shp2pgsql -s 5179 -W cp949 ./sig.shp |PGPASSWORD='postgres' psql -U postgres -d gis -q
$ shp2pgsql -s 5179 -W cp949 ./li.shp |PGPASSWORD='postgres' psql -U postgres -d gis -q
```
저자는 테이블명을 아래와 같이 리네임하였다.

> 시, 도 -> korea_1st
> 
> 구 -> korea_2nd
>
> 동 -> korea_3rd
>
> 리 -> korea_4th

![테이블리스트](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/2cc93df7-23da-43d5-9780-109d140fa726)
{: .align-center}


### 좌표계 변환
아래 URL에 좌표계 정리를 잘 해주셨다.

https://yganalyst.github.io/spatial_analysis/spatial_analysis_3/

아래 명령어를 통해 5179 좌표계를 4326좌표계로 변환한다.

```sql
alter table public."korea_1st"
 alter column geom type geometry(multipolygon, 4326) using st_transform(st_setsrid(geom, 5179), 4326);

alter table public."korea_2nd"
 alter column geom type geometry(multipolygon, 4326) using st_transform(st_setsrid(geom, 5179), 4326);

alter table public."korea_3rd"
 alter column geom type geometry(multipolygon, 4326) using st_transform(st_setsrid(geom, 5179), 4326);

alter table public."korea_4th"
 alter column geom type geometry(multipolygon, 4326) using st_transform(st_setsrid(geom, 5179), 4326);
```


2부에서는 fastAPI를 활용하여 좌표변환 및 카프카 활용에 대해서 포스팅을 할 예정이다.



















