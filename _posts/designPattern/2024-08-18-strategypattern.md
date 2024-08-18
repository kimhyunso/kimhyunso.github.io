---
title: "전략 패턴 (Strategy Pattern)"
layout: single
categories:
  - designpattern
tags:
  - Strategy
  - DesignPattern
  - 디자인 패턴
  - 전략패턴
---

## 디자인 패턴
반복적으로 일어나는 문제들을 어떻게 해결해 나갈 것인지에 대한 해결방안 :: 정답이 아님

어떻게 바뀔지 모르는 상황에서 수정을 많이 하지 않고 어떻게 대처할 것인지에 대한 방안 모음

## 전략 패턴
행위 분류하여 미리 만들어 놓고 상황에 따라 알맞게 선택해서 사용하는 패턴

만약, 변경사항이 생기더라도 새로운 행위를 만들면 됨

- keyword : 많은 수정사항

```java
public interface Vehicle {
    public void run();
}

public class Subway implements Vehicle {
    @Override
    public void run() {
        System.out.println("선로 위를 달린다.");
    }
}

public class Bus implements Vehicle {
    @Override
    public void run() {
        System.out.println("도로 위를 달린다.");
    }
}
```

위와 같이 설계를 진행했다면 무슨 문제가 발생할까?

만약, 버스(`Bus`)가 물 위를 달릴 수 있게 발명되었다고 한다면 어떻게 될까?

버스의 문구를 수정해야 할 것이다.

```java
// 수정
@Override
public void run() {
    System.out.println("도로 위를 달린다.");
}
```

한 번만 수정하니 편리한 듯하다.

그런데 도로 위를 달리던 교통수단들이 물 위를 달릴 수 있게 된다면 어떻게 될까?

모든 교통수단들의 문구들을 일일이 수정해야 할 것이다.

그렇다면 얼마나 바뀌어야 하는가? 교통수단들 만큼 바뀌어야 모든 것을 해결 할 수 있지 않은가?

얼마나 비효율적인가 따라서 상황에 맞게 변경되는 것들을 미리 만들어 전략에 따라 바꿀 수 있도록 해야할 것이다.

아래의 코드들을 보자

### 행위들의 모음

```java 
public interface Way {
    public void run();
}

public class WaterWay implements Way {
    @Override
    public void run() {
        System.out.println("물 위를 달린다.");
    }
}

public class TrackWay implements Way {
    @Override
    public void run() {
        System.out.println("선로 위를 달린다.");
    }
}

public class RoadWay implements Way {
    @Override
    public void run() {
        System.out.println("도로 위를 달린다.");
    }
}
```


### 실제 구현 클래스들

```java
public abstract class Transportation {
    protected Way way;

    public void performRun() {
        way.run();
    }

    public void stop() {
        System.out.println("멈춤");
    }

    public void setWay(Way way) {
        this.way = way;
    }
}

public class Subway extends Transportation {
    public Subway(Way way) {
        this.way = way;
    }
}

public class Bus extends Transportation {
    public Bus(Way way) {
        this.way = way;
    }
}

public class Taxi extends Transportation {
    public Taxi(Way way) {
        this.way = way;
    }
}

// 변경 전
Subway subway = new Subway(new TrackWay());
subway.performRun(); // 선로 위를 달린다.

Bus bus = new Bus(new RoadWay());
bus.performRun(); // 도로 위를 달린다.

Taxi taxi = new Taxi(new RoadWay());
taxi.performRun(); // 도로 위를 달린다.

// 변경 후
subway.setWay(new WaterWay());
subway.performRun(); // 물 위를 달린다.

bus.setWay(new WaterWay());
bus.performRun(); // 물 위를 달린다.

taxi.setWay(new WaterWay());
taxi.performRun(); // 물 위를 달린다.
```

만약, 교통수단들이 갑자기 하늘을 날 수 있게 바뀐다면 행동 클래스를 추가하면 된다.

```java
public class FlyWay implements Way {
    @Override
    public void run() {
        System.out.println("하늘 위를 달린다.");
    }
}
```






















작은 프로그램임에도 불구하고 3건 이상의 변경사항이 생겼다.









































