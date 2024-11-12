---
title:  "typingGame 만들기 (도메인 구상)"
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
3. OOP(Object-Oriented Programming)에 대한 이해

## 도메인 구상
1. 스테이지(Stage) 클래스
	- 스테이지의 레벨
	- 스테이지의 백그라운드

```java
public class Stage {
	private final int stageLevel;
	private final BufferedImage backgroundImage;
	private final int score;

	public Stage(final int stageLevel, final BufferedImage backgroundImage, final int score) {
		this.stageLevel = stageLevel;
		this.backgroundImage = backgroundImage;
		this.score = score;
	}

	// toString(), equals()
}
```


2. Unit 슈퍼클래스
	- 공격력
	- 위치값 (x, y)
	- 죽었는지 살았는지
	- 이미지 (공격, 움직임, 뛰기)
	- 공격하기: 행동
	- 움직이기: 행동
	1. Soldier 클래스
		- 공격력 10
		- 위치값 (x, y)
		- 죽었는지 살았는지 상태값
		- 이미지 (공격, 움직임, 뛰기)
		- 공격하기: 행동
	2. Zombie 클래스
		- 공격력 2 ~ 5
		- 위치값 (x, y)
		- 죽었는지 살았는지 상태값
		- 라벨
		- 이미지 (공격, 움직임, 뛰기)
		- 공격하기: 행동
		- 움직이기: 행동

```java
public class Position {
	private int x;
	private int y;

	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}

	// toString(), equals()
}

public abstract class Unit {
	protected String name;
	protected int damage;
	protected Position position;
	protected List<BufferedImage> attackImages;
	protected List<BufferedImage> runImages;
	protected List<BufferedImage> moveImages;
	protected boolean isDead = false;
}

public interface SoldierAttackable {
	Soldier attack(Soldier soldier);
}

public interface ZombieAttackable {
	Zombie attack(Zombie target);
}

public class Soldier extends Unit implements ZombieAttackable {
	public Soldier(String name, Position position) {
		this.name = name;
		this.damage = 10;
		this.position = position;
	}

	@Override
	public Zombie attack(Zombie target) {

	}
}

public class Label {
	private String label;
}


public class Zombie extends Unit implements SoldierAttackable {
	private Label label;

	public Zombie(String name, Position position) {
		this.name = name;
		this.damage = Math.random(5) % 2 + 1;
		this.position = position;
	}

	@Override
	public Soldier attack(Soldier soldier) {
		
	}
}

```



