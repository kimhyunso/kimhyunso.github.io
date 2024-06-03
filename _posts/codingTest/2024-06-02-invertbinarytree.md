---
title:  "99클럽 코테 스터디 2일차 TIL - 트리순환문제"
layout: single
categories:
  - codingtest
tags:
  - 99클럽
  - 코딩테스트 준비
  - 개발자 취업
  - 항해99
  - TIL
---

# 오늘의 학습 키워드 
트리순환문제

# 오늘 공부한 내용
재귀함수 복습

# 오늘의 회고

처음 문제를 보고 어제 문제의 복습인 재귀함수를 사용하면 쉽게 풀 수 있을 것이라 생각했다.

하지만 뜻대로 되지는 않았다.

뜻대로 되지 않자 천천히 처음부터 복기하기 시작했다.

맨위의 노드가 들어오면 어떻게 되고, 그 다음 노드 차례가 되면 어떻게 되는지 차근차근 노트와 펜을 들고 생각해보니

결국 왼쪽 노드의 맨마지막 노드와 왼쪽 노드의 맨 마지막 오른쪽 노드를 교환하고

맨위의 노드 입장에서 오른쪽 맨마지막 왼쪽 노드와 오른쪽 맨마지막 오른쪽 노드를 교환하고 

중간 노드들이 저절로 바뀌니 해결되었을 것이라 생각했다.

그 결과 시간은 오래 걸렸지만 통과하였다!

다음 문제는 아는 것이라 자만하지말고 차근차근히 생각하는 습관을 들여야할 것 같다.

![통과](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/102b8cc1-4b62-4c9f-a012-4c22d859e6b8)
{: .align-center}

# 결과물
[결과물보러가기](https://github.com/kimhyunso/sail-99_withPython/tree/main/266.InvertBinaryTree)











