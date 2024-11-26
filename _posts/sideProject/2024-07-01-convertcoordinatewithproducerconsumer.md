---
title:  "좌표변환 - 4부 (producer, consumer)"
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


## producer
nodejs를 사용했다.

https://nodejs.org/en

프로듀서 부분만 포스팅을 하겠다. 나머지 부분은 아래 url에서 확인하길 바란다.

producer URL : https://github.com/geosoft-mini/producer-nodejs


### npm kafkajs
https://www.npmjs.com/package/kafkajs


### npm express
https://www.npmjs.com/package/express

```js
// producer/producer.js
const { Kafka } = require('kafkajs')
const { Partitioners } = require('kafkajs')

const kafka = new Kafka({
	clientId: 'test-group',
	brokers: ['localhost:9092']
})

const producer = kafka.producer({
	maxRequestSize: 200000000,
	createPartitioner: Partitioners.LegacyPartitioner
})

const initKafka = async () => {
	await producer.connect()
}

initKafka()
module.exports = { producer }


// routers/readCsv/readCsv.js
const express = require('express')
const router = express.Router()
const multer = require('multer')
const { producer } = require('../../producer/producer')

const storage = multer.memoryStorage()
const upload = multer({ storage: storage })
const topic = 'overspeed-detail-address'


const sendProcuder = async (topic, result, partitionIndex) => {
	await producer.send({
		topic: topic,
		messages: [
			{ value: JSON.stringify(result), partition: partitionIndex % 3 },
		],
	})
}

router.post('/', upload.single('list.csv'), async (req, res, next) => {

	const files = req.file.buffer.toString('utf-8')
	const rows = files.split('\r\n')
	rows.shift()

	const splitNum = 100

	for (let i = 0; i < rows.length / splitNum; i++) {
		const result = []
		for (let j = splitNum * i; j < splitNum * (i + 1); j++){
			try { result.push(rows[j].split(',')) } catch (error) {}
		}	
		await sendProcuder(topic, result, i)
	}

	res.send('response ok')
})

module.exports = router;
```

### 경보
위의 코드를 실행하면 아래와 같은 경보창이 뜬다.

경보창 메시지에서 url을 클릭해서 들어가니 아래와 같은 문구가 있었다.

![경보](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/84817978-c690-4905-8eb4-d8d848a50b76)
{: .align-center}


### 경보해결
![경보해결](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7315712d-006f-48fc-8bd1-ecd5184df91d)
{: .align-center}

## consumer
전의 포스팅에서 fastAPI 부분을 제외하고 ORM사용 부분만 채택했다.

consumer URL : https://github.com/geosoft-mini/consumer-python

```python
# init/consumer.py
from kafka import KafkaConsumer
from json import loads

def init(client_id, group_id):
    return KafkaConsumer(
        client_id = client_id,
        bootstrap_servers = ['localhost:9092'], # 카프카 브로커 주소 리스트
        auto_offset_reset = 'latest', # 오프셋 위치(earliest:가장 처음, latest: 가장 최근)
        enable_auto_commit = True, # 오프셋 자동 커밋 여부
        group_id = group_id, # 컨슈머 그룹 식별자
        value_deserializer = lambda x: loads(x.decode('utf-8')), # 메시지의 값 역직렬화
        consumer_timeout_ms = 10000,
    )

# main.py
from db.database import SessionLocal
from db.query import si_gu_dong_ri, si_gu_dong
from init.consumer import init
from create.create_excel import CreateExcel

excel_title = '과속 상세내역'
excel_sheet_name = '과속 상세내역 주소변환'
result_file_name_path = './excel/result.xlsx'
excel = CreateExcel(excel_title, excel_sheet_name)

topic = 'overspeed-detail-address'
consumer = init(client_id='consumer1', group_id='test-group1')
consumer.subscribe(topic)

db = SessionLocal()

def __create_row(values: list, address: str) -> list:
    return [values[0], values[1], values[2], values[3], address, values[6], values[7]]

for messages in consumer:
    for values in messages.value:
        x = float(values[4])
        y = float(values[5])
    
        result = db.execute(si_gu_dong_ri(x, y)).fetchone()
        if not result:
            result = db.execute(si_gu_dong(x, y)).fetchone()
            
        address = excel.create_excel(result)
            
        row = __create_row(values, address)
        excel.ws.append(row)
        
excel.wb.save(result_file_name_path)
excel.wb.close()
```

## 결과
데이터는 회사와 관련된 데이터이기 때문에 공개를 하지는 않겠다.

대신 테스트 데이터를 사용하겠다.

```csv
회사코드,차량번호,차량ID,날짜,주소,,속도,발생시각
testse01, 울산123바12321, kmsa12c1212, 202404022, 127.371028, 36.964962, 81, 22-APR-24 10:43:00
... more 1101
```

## swagger를 사용하여 카프카로 데이터 전송하기
swagger를 통해 카프카에게 전달한다.

![카프카로데이터전송하기](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/979043e7-f2ef-4a6e-ac0d-d692bccef67e)
{: .align-center}

카프카 레그를 확인한다.

![카프카레그확인](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/e7e24350-07d4-4f6b-8a9a-b5421144d0b2)
{: .align-center}

컨슈머를 실행시킨다. 

![컨슈머실행결과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7e6e2549-ce90-4a1f-832a-b167b3b1393f)
{: .align-center}

## 만났던 문제점
처음에는 반복문을 잘 못 사용함으로 써, 데이터가 카프카에 많이 쌓이게 되는 문제를 발견하게 되었다.

처음에는 근본적인 문제의 원인을 파악하지 못함으로써 시간을 많이 허비했다.

아래와 같은 삽질(?)을 진행하고 반복문이 잘 못되어 데이터가 커져버리는 현상을 캐치하게 되었다.

## 에러
![오류](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/c5105163-4473-474d-bd3b-5be38a9b9604)
{: .align-center}

KafkaJSProtocolError: The request included a message larger than the max message size the server will accept


## 솔루션 1
kafka config 설정을 아래와 같이 바꾼다.

> message.max.bytes=200000000
> 
> max.request.size=200000000
> 
> max.partition.fetch.bytes=200000000

## 솔루션 2
```sh
$ kafka-topics --bootstrap-server localhost:9092 --create --topic large-message --partitions 3 --replication-factor 1
```

```js
const producer = kafka.producer({
    maxRequestSize: 200000000  
})
```

## commitFatiledException
https://mujilog.tistory.com/entry/리밸런싱이-자주-일어나는-경우-CommitFailedException에-대해



## 보안점
현재 프로젝트의 보안점은 xslx파일을 csv파일로 변경하고 변경된 csv파일을 카프카로 전송하여 consumer가 해당 데이터를 읽어 xlsx파일로 만들어주는 번거로움이 있다.

1. xslx파일을 변경하지 않고 카프카에 전송한다.
2. consumer를 수동으로 돌리지 않고 배치적으로 돌 수 있게 만든다.



















