---
title:  "typingGame 만들기 (설계)"
layout: single
categories:
  - sideproject
tags:
  - java
  - game
  - thread
  - udp
  - tcp
---

## 프로젝트 목적
1. `thread`, `udp`, `tcp`를 활용해서 game을 만들고 이해하기
2. 디자인 패턴을 적용하여 만들어보기

## 설계
- 메인 화면
	- 싱글모드버튼: 게임시작
	- 멀티모드버튼: local 통신을 통해 상대방과 대전가능
	- 설정버튼: 설정을 통해 화면의 해상도, 소리 등을 조절할 수 있음
	- 명예의전당버튼: 순위를 비교하여 1등 부터 50등까지의 순위를 보여줌
	- 나가기버튼: 종료버튼

![game_view](https://github.com/user-attachments/assets/b9afd078-aab7-458e-aa92-b850af24260c)
{: .align-center}


- 싱글모드버튼 클릭시
	- 캐릭터 선택 기능
	1. davidthompson
	2. jamescarter
	3. johnmiller

![chois_character](https://github.com/user-attachments/assets/dd4362b3-4689-4861-badd-3f99d8d98c5a)
{: .align-center}

- 캐릭터 선택시
	- 게임시작
	- 필요한 요소들
	1. 체력
	2. 타수 속도
	3. 점수
	4. 좀비들
	5. 군인
	
![single_game_view_level1~2](https://github.com/user-attachments/assets/042ea500-d142-4967-801d-e432dd483e83)
{: .align-center}

-  설정 버튼 클릭시
	- 해상도 조절기능
	- 단어 추가 기능
	- 사운드 조절 기능

![setting](https://github.com/user-attachments/assets/7b74685f-8736-49cd-b864-a0068179646c)
{: .align-center}



