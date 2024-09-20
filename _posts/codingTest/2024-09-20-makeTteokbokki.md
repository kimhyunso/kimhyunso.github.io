---
title:  "이것이 코딩테스트다 - 13일차"
layout: single
categories:
  - codingtest
tags:
  - TIL
---

## 주제
binary search

## 문제
여행 가신 부모님을 대신해 떡집에서 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.

떡볶이의 떡은 길이기 일정하지 않다. 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라 맞춘다.

절단기 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.

손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

## 예시
19, 14, 10, 17cm인 떡이 나란히 있다면 절단기 높이를 15cm로 지정한 뒤 자른 뒤의 떡 높이는 15, 14, 10, 15cm가 될 것이다.

잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼을 가져가게 된다.

## 조건
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000) (1 <= M <= 2,000,000,000)

둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상 이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.

높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

## 최초 시도
처음에는 해당 문제를 보고 떡길이의 총합 / H 를 해서 나머지가 6이 된다면 해당 몫이 정답인 줄 알았다.

예시대로 한다면 61 / H 나머지 = 6로 되는 것이 정답인 줄 알았는데 아니였다. 예시대로 한다면 61 / 15 나머지는 1이 되게된다.

다른 방법을 한참을 고민하다 결국 내가 모르는 문제라는 것을 인정한 뒤 풀이방법을 보고 말았다.

풀이에 대한 힌트는 떡의 개수만큼 떡을 세로로 배치한 뒤 중간`(떡의 시작점=0 + 떡의 끝점=19 // 2)`을 잘라보고 잘려진 나머지들의 합이 고객이 요구하는 것과 같은지 판별 한 뒤

아니라면 다시 중간 + 1에서 떡의 시작점(10)과 떡의 끝점(19)의 중간점을 찾아 나머지들의 합이 고객이 요구하는 것과 같은지 판별하는 것을 반복하는 작업이였다.

다음 그림을 보자 이해가 더 쉬울 것이다.

![첫번째loop](https://github.com/user-attachments/assets/35f4aa5d-b6b7-426e-b647-5e4b67f447e9)
{: .align-center}

![두번째loop](https://github.com/user-attachments/assets/19ee7cb6-dfb2-4744-8c37-f3d85156a1e1)
{: .align-center}

![세번째loop](https://github.com/user-attachments/assets/9b728ea6-c6ed-4f1e-9c83-ae7dbab37018)
{: .align-center}

![네번째loop](https://github.com/user-attachments/assets/dfce753e-62d6-462b-9a43-8f03c591ce6a)
{: .align-center}

![다섯번째loop](https://github.com/user-attachments/assets/a3b57e50-f3da-4c2a-9215-cb4cb8390ea2)
{: .align-center}

![종료](https://github.com/user-attachments/assets/087d8d1d-14a4-4df1-904b-0c8c46cf4533)
{: .align-center}


## 풀이 방법
1. 떡의 개수, 고객이 요청한 떡의 길이, 떡의 개별 높이 배열을 입력받는다.
2. 시작점과 끝점을 구한다. 끝점은 떡의 개별 높이 배열 중 가장 큰 요소이다.
3. binary search를 이용한다.
4. 떡의 나머지 총합을 구하는 로직을 사용하여 자른 뒤 나머지의 총합을 구한다.
5. 자른 뒤 나머지 총합과 고객이 요구한 떡의 길이를 비교하여
6. 자른 뒤 나머지 총합 < 고객이 요구한 떡의 길이 : 끝점을 중앙 -1 만큼 이동시킨다.
7. 자른 뒤 나머지 총합 >= 고객이 요구한 떡의 길이 : 중앙값을 결과에 담고, 시작점을 중앙 + 1 만큼 이동시킨다.
8. 결과를 출력한다.

```python
n, m = map(int, input().split(' '))
rice_cakes = list(map(int, input().split(' ')))

start = 0
end = max(rice_cakes)

result = 0
while (start <= end):
    remain_total = 0 # 떡의 나머지 총합
    mid = (start + end) // 2

    for rice_cake in rice_cakes: # 떡의 나머지 총합을 구하는 로직
        if rice_cake > mid:
            remain_total += rice_cake - mid

    if remain_total < m: # 자른 뒤 나머지의 총합이 요구한 떡의 길이보다 작을 경우
        end = mid - 1
    else: # 자른 뒤 나머지의 총합이 요구한 떡의 길이보다 크거나 같을 경우
        result = mid
        start = mid + 1

print(result)
```












