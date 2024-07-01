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

> 환경 : docker
>
> 사용 프레임워크 : Nodejs, Kafka, fastAPI
>
> 데이터베이스 : postgresql/postgis


## producer
nodejs를 사용했다.

https://nodejs.org/en

프로듀서 부분만 포스팅을 하겠다. 나머지 부분은 아래 url에서 확인하길 바란다.

https://github.com/geosoft-mini/producer-nodejs


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

https://github.com/geosoft-mini/consumer-python





















