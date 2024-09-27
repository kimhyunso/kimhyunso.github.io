---
title:  "좌표변환 - 2부 (fastAPI)"
layout: single
categories:
  - sideproject
tags:
  - faseAPI
  - python
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

## fastAPI
데이터베이스와 connection이 잘 맺어지는지 테스트 하기위해서 fastAPI로 만들었다.

일단 기본적으로 python이기 때문에 가상환경을 설정하여 진행했다.

아래 해당 url을 참고했다.

**https://wikidocs.net/175967**

## python 가상환경 설정하기

```shell
$ python -m venv [가상환경이름]
$ cd [가상환경이름]/Scripts
# 가상환경 활성화
$ source activate
# 가상환경 비활성화
$ source deactivate
```

## python 라이브러리 install
```shell
# fastapi 라이브러리
$ pip install fastapi
# python ORM 라이브러리
$ pip install sqlalchemy
# model = dto 만드는 라이브러리
$ pip install pydantic
```

## requirements.txt
해당 라이브러리가 다른 환경에서 동작을 안할 수도 있기 때문에 쉽게 환경을 다른 컴퓨터에서도 적용할 수 있도록 라이브러리버전 명시한다.

```shell
$ pip freeze > requirements.txt
```

![프로젝트구조](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7bc4d43f-b97f-46d3-ac89-26f536899877)
{: .align-center}

## api만들기

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main() -> dict:
    return {'Hello' : 'World'}
```

## 실행 및 테스트해보기
해당 url http://127.0.0.1:8000에서 결과를 확인할 수도 있지만

테스트를 위해 swagger를 사용했다.

> http://127.0.0.1:8000/docs

```shell
# 실행 명령어
$ uvicorn main:app --reload
```

![fastAPIdocs테스트](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/c87e02e4-5733-4334-b168-4d92f8b07f5d)
{: .align-center}

## 쿼리스트링 파라미터 및 body 데이터 테스트해보기

### 쿼리스트링 테스트
```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello(name: str) -> dict:
	return {'name' : name}
```

![쿼리스트링테스트](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/00d600cd-1abb-4233-b497-33b41167fa92)
{: .align-center}

### body 데이터 테스트

```python
# model.py
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
	item_id: int
	item_content: Optional[str]

# main.py
from fastapi import FastAPI
from model import Item

app = FastAPI()

@app.post('/hello-body')
def hello(Item: Item):
	return Item
```

![fastAPIBody테스트1](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/bb8fa23c-d3d2-4914-b3a3-ed8ca3915d83)
{: .align-center}

![fastAPIBody테스트2](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/2992479e-25a0-42ef-b540-c951c4eaae04)
{: .align-center}


### file업로드 테스트 및 x좌표, y좌표 읽어들이기
file을 업로드하여 x좌표와 y좌료를 읽어드린다.

pandas를 사용했다. 

### 에러
처음에는 pandas로 읽은 x좌표와 y좌표를 바로 리턴하기 위해 `return {'x' : read_x, 'y' : read_y}`를 사용했었다.

하지만 다음과 같은 에러가 발생했다. 자세히 읽어보니 `serialize unknown type` 직렬화 타입 확인 불가라고 나와 있었다. 

문제는 `return`시 type이 `pandas.Series`였던 것이 문제였다.

![에러](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/399ce87a-6df1-40a3-9b49-59d2a6fb936e)
{: .align-center}

### 해결
x좌표와 y좌표를 리스트에 `append()`시켜서 `dict()`로 리턴을 하였다.

위의 함수를 바탕으로 하여 x좌표와 y좌표를 데이터베이스 쿼리를 조회하고 결과를 리턴하는 테스팅을 할 것이다.

### dbConnection 오류
![dbConnection오류](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/32efa5aa-8336-43b1-966b-cc3bd1979fe9)
{: .align-center}

### 해결
해당 패키지에 `psycopg2`가 포함되어 있어 인스톨을 진행했다.

```sh
$ pip install psycopg2-binary
```

### 파일 업로드 테스트
```python
from fastapi import FastAPI, File, UploadFile
import pandas as pd

@app.post('/file')
def file_upload(file: UploadFile) -> dict:
    read_csv = pd.read_csv(file.file, encoding='utf-8')
    read_x = read_csv.iloc[:,4]
    read_y = read_csv.iloc[:,5]

    result = {}
    x_coordinates = []
    y_coordinates = []

    for x, y in zip(read_x, read_y):
        x_coordinates.append(x)
        y_coordinates.append(y)
        result['x'] = x_coordinates
        result['y'] = y_coordinates

    return result
```

![파일업로드테스트](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/5190de6c-e10f-4124-8827-58127548bd82)
{: .align-center}



## 데이터베이스 쿼리 조회 및 결과 리턴
해당 쿼리는 기존에 도와주시던 분께서 너무 감사하게도 sql쿼리를 짜주셨다.

원래는 해당 테이블을 파악하고 그에 따른 sql쿼리를 짜야하지만 있는 sql쿼리문을 ORM으로 적용해봐야겠다는 생각이 들었다.

### 기존 SQL 쿼리문
쿼리문이 두 개인 이유는 하나는 도시군구동읍면리 중 도시군구동읍면만 있는 주소 체계가 있기때문에 두 개의 쿼리를 생성해주셨다.

```sql
-- 도시군구동읍면리
select D.ctp_kor_nm, C.sig_kor_nm, B.emd_kor_nm, A.li_kor_nm
  from
   (select li_cd, substring(li_cd, 1, 8) as up_cd, li_kor_nm
      from public."Korea_4th"
     where geometry_within (st_setsrid(st_geomfromtext('POINT(127.135 37.0612)'), 4326), geom) limit 1) as A,
   (select emd_cd, substring(emd_cd, 1, 5) as up_cd, emd_kor_nm
      from public."Korea_3rd") as B,
   (select sig_cd, substring(sig_cd, 1, 2) as up_cd, sig_kor_nm
      from public."Korea_2nd") as C,
   (select ctprvn_cd, ctp_kor_nm
      from public."Korea_1st") as D
 where A.up_cd = B.emd_cd
   and B.up_cd = C.sig_cd
   and C.up_cd = D.ctprvn_cd
 ;

-- 도시군구동읍면
select D.ctp_kor_nm, C.sig_kor_nm, B.emd_kor_nm
  from
   (select emd_cd, substring(emd_cd, 1, 5) as up_cd, emd_kor_nm
      from public."Korea_3rd"
     where geometry_within (st_setsrid(st_geomfromtext('POINT(127.048 37.3007)'), 4326), geom) limit 1) as B,
   (select sig_cd, substring(sig_cd, 1, 2) as up_cd, sig_kor_nm
      from public."Korea_2nd") as C,
   (select ctprvn_cd, ctp_kor_nm
      from public."Korea_1st") as D
 where B.up_cd = C.sig_cd
   and C.up_cd = D.ctprvn_cd
 ;
```

### 기존 SQL ORM 변경
python ORM인 `sqlalchemy`을 사용했다.

위의 쿼리를 ORM으로 변경한 것이다.

```python
from db.model import Korea_1st, Korea_2nd, Korea_3rd, Korea_4th
from sqlalchemy import select, func

dong = (select(Korea_3rd.emd_cd, func.substring(Korea_3rd.emd_cd, 1, 5).label('up_cd'), Korea_3rd.emd_kor_nm)).alias('dong')
gu = (select(Korea_2nd.sig_cd, func.substring(Korea_2nd.sig_cd, 1, 2).label('up_cd'), Korea_2nd.sig_kor_nm)).alias('gu')
si = (select(Korea_1st.ctprvn_cd, Korea_1st.ctp_kor_nm)).alias('si')

def si_gu_dong(x, y):
    dong = (
        select(Korea_3rd.emd_cd, func.substring(Korea_3rd.emd_cd, 1, 5).label('up_cd'), Korea_3rd.emd_kor_nm)
        .where(func.ST_Within(func.ST_SetSRID(func.ST_GeomFromText(f'POINT({x} {y})'), 4326), Korea_3rd.geom))
        .limit(1)
    ).alias('dong')
    
    result = (
        select(si.c.ctp_kor_nm, gu.c.sig_kor_nm, dong.c.emd_kor_nm)
        .select_from(dong)
        .join(gu, dong.c.up_cd == gu.c.sig_cd)
        .join(si, gu.c.up_cd == si.c.ctprvn_cd)
    )
    
    return result


def si_gu_dong_ri(x, y):
    ri = (
         select(Korea_4th.li_cd, func.substring(Korea_4th.li_cd, 1, 8).label('up_cd'), Korea_4th.li_kor_nm)
        .where(func.ST_Within(func.ST_SetSRID(func.ST_GeomFromText(f'POINT({x} {y})'), 4326), Korea_4th.geom))
        .limit(1)
    ).alias('ri')

    result = (
        select(si.c.ctp_kor_nm, gu.c.sig_kor_nm, dong.c.emd_kor_nm, ri.c.li_kor_nm)
        .select_from(ri)
        .join(dong, ri.c.up_cd == dong.c.emd_cd)
        .join(gu, dong.c.up_cd == gu.c.sig_cd)
        .join(si, gu.c.up_cd == si.c.ctprvn_cd)
    )

    return result
```

### api와 접목해보기
```python
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from db.query import si_gu_dong_ri, si_gu_dong
from db.database import SessionLocal

db = SessionLocal()

# main.py
@app.post('/file-convert')
def file_upload(file: UploadFile) -> list:
    read_csv = pd.read_csv(file.file, encoding='utf-8')
    read_x = read_csv.iloc[:,4]
    read_y = read_csv.iloc[:,5]

    result = [db.execute(si_gu_dong_ri(x, y)).fetchone() for x, y in zip(read_x, read_y)]

    if not result:
        result = [db.execute(si_gu_dong(x, y)).fetchone() for x, y in zip(read_x, read_y)]

    return result
```


3부에서는 카프카 활용에 대해서 포스팅을 할 예정이다.




 
















