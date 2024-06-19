---
title:  "좌표변환 - 2부 (kafka 공부)"
layout: single
categories:
  - network
tags:
  - "kafka"
---

## 하고자 하는 목표
간단한 x좌표와 y좌표가 있는 csv파일을 업로드 시키면 알아서 좌표로 변환 후 엑셀파일로 변환시켜주는 자동화 작업을 하고 싶음

사실상 대규모의 트래픽을 감당하고 있지 않기 때문에 (대략 20000~3000건의 데이터 처리) 카프카를 사용할 이유는 없다.

> 환경 : docker
>
> 사용 프레임워크 : Nodejs, Kafka, fastAPI
>
> 데이터베이스 : postgresql/postgis

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

테스트를 위해 http://127.0.0.1:8000/docs를 활용했다.

swagger같은 RESTAPI 명세서

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

```python
from fastapi import FastAPI, File, UploadFile
import pandas as pd

@app.post('/file-upload')
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

![파일업로드테스트](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6e0110c8-abe4-43b4-9ccb-df5b5968face)
{: .align-center}

### 에러
처음에는 pandas로 읽은 x좌표와 y좌표를 바로 리턴하기 위해 `return {'x' : read_x, 'y' : read_y}`를 사용했었다.

하지만 다음과 같은 에러가 발생했다. 자세히 읽어보니 `serialize unknown type` 직렬화 타입 확인 불가라고 나와 있었다. 

문제는 `return`시 type이 `pandas.Series`였던 것이 문제였다.

![에러](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/399ce87a-6df1-40a3-9b49-59d2a6fb936e)
{: .align-center}

### 해결
x좌표와 y좌표를 리스트에 `append()`시켜서 `dict()`로 리턴을 하였다.


위의 함수를 바탕으로 하여 x좌표와 y좌표를 데이터베이스 테이블에 





 
















