---
title:  "나의 생각 말해보기 1일차"
layout: single
categories:
  - thinking
tags:
  - 생각정리
  - 회고
---

## 왜 규칙을 따라야하는가?
코딩이라는 것은 너무나 자유롭기 때문에 사람들과 규칙을 정해 다같이 만들어가는 것이라고 생각이 된다.

가령, 아래의 예시를 보자

아래의 예시를 보면 하나는 snake_case와 다른 하나는 CamelCase로 되어있다는 것을 알 수 있다.

```python
user_count = 3
userCount = 3
```

그러나 누가 이것이 표준이라고 하겠는가? :: 절대 정답이 아니다.

또한 아래의 예시를 하나 더 보자

```python
a = 3
b = 4
n = a + b
```

a와 b를 더해서 n이라는 변수에 담고 있다. 누구도 저런 코드를 좋아하지 않는다.

왜 우리는 항상 변수명은 신중하게 각 언어특성에 맞는 표기법을 따라야하는가?

나만의 생각은 서로 협력해나가면서 정해진 규격이 없다면 다른 사람이 읽을 수 없고,

그렇다면 한 사람이 작성한 코드들은 그 사람만이 **유일하게** 읽을 수 밖에 없다.

이것이 왜 문제가 될까? 내가 코딩해서 나만이 읽어서 내가 스스로 고쳐나가면 되지 않을까?

이렇게 생각한다면 회사를 다니는 의미가 없다고 생각한다.

**한사람에게 의존되기 때문이다.** 

회사 입장에서 생각해보아도 실력은 없지만 그 사람이 작성한 코드를 누구도 읽을 수 없다는 이유로 짜를 수 없다.

그렇기 때문에 결과적으로는 다른 사람들이 보편적으로 사용하고 있는 표준은 지켜야 한다고 생각된다.

물론 나의 생각이 정답은 아니다. 누구나 다른 생각과 다른 가치관을 지닌다.

어느 책에서 본 내용인데, 사람이란 같은 진리하나를 배워도 받아들이는 관점의 차이가 생긴다고 한다.

우리의 눈이나 환경 등이 영향을 끼칠 수 있다고 한다. 그렇기 때문에 세상에 정답이란 없다.

## 왜 코드리뷰를 받아야하는가?
현재 회사를 다니며 느끼는 생각이지만, 선임은 없어도 되지만, 회사에 코드리뷰는 필수라는 생각이 든다. (현재 코드리뷰를 받고 있지는 않는다.)

코드리뷰는 현재 내가 짠 함수에 대한 다른사람이 보았을 때 문제점을 찾을 수 있다. 나만의 생각뿐 아니라 다른 사람들의 생각을 피드백 받는 것이 중요하다고 생각된다. **(객관화)**

만약, 코드리뷰를 받지 못 한다면 현재 년차에서 더 이상 성장할 수 없다는 생각이 든다. 이것은 어디까지나 나만의 생각이다.

평가라는 것도 내가 하는 것이 아닌 다른 사람에 의해서 어떤 방식으로든 당하게 되는 것처럼 코드 리뷰도 비슷하다고 생각이 된다.


## 디자인 패턴 및 방법론들이 왜필요하는가?
코딩은 사실상 변수, 조건문(=`if`), 반복문(=`for`, `while`)이 전부이다.

그런데도 디자인 패턴이라는 것이 존재한다.

왜 필요할까?

나의 개인적인 생각이지만 변수, 조건문, 반복문만 사용하여 코딩한다는 것은 자국어를 응, 그래, 아니밖에 하지 않는 것이라고 생각한다.

생각해보자 우리는 일상생활 속에서 다른 사람들과 대화를 어떻게 하는가?

나의 감정, 현재 상태, 환경 등등 다양한 조건속에서 대화를 이루어 나가지 않는가?

그런데 왜 코딩은 변수선언, 조건문, 반복문이 전부일 것이라고 속단하는가

코딩도 마찬가지라고 생각이든다. 

수많은 방법론들이 있지만, 각자의 방법론들은 각자의 언어와 생각들이 집약되어 있다.

우리는 응, 그래, 아니만 사용하기 위해서 코딩하는 것이 아닌 다른 사람들과 일상에서 대화를 하듯이 코딩하는 것이라고 생각이 된다.

아래 예시를 보자

```python
from domain import Cat, Dog

animal_type = 'cat'

def createAnimal(animal_type):
    if animal_type == 'cat':
        return Cat()
    elif animal_type == 'dog':
        return Dog()

createAnimal(animal_type)
```

위의 코드를 보고 무언가 잘못된 점을 찾지 못하였다면 좀더 공부를 하기를 바란다.

세상에 동물이 강아지와 고양이 밖에 없을 수가 있을까?

누군가 '저는 토끼를 좋아해서 토끼도 생성할 수 있도록 해주세요.' 라고 요청이 들어왔다면 어떻게 할까?

다음 두가지 예시를 보고 어떻게 하는 것이 좀 더 유연한지 판단하기를 바란다.

첫번째 예시는 `if`문 뒤에 계속 추가를 하는 것이다.

```python
from domain import Cat, Dog, Rabbit

animal_type = 'rabbit'

def createAnimal(animal_type):
    if animal_type == 'cat':
        return Cat()
    elif animal_type == 'dog':
        return Dog()
    elif animal_type == 'rabbit':
        return Rabbit()

createAnimal(animal_type)
```

두번째 예시는 디자인 패턴 중 팩토리패턴 사용하여 타입에 따른 인스턴스들을 생성한다.

```python
from abc import abstractmethod

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Factory:
    @abstractmethod
    def create_animal(self):
        pass

class CatFactory(Factory):
    def create_animal(self):
        return Cat()

class DogFactory(Factory):
    def create_animal(self):
        return Dog()
    
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Factory:
    @abstractmethod
    def create_animal(self):
        pass

class CatFactory(Factory):
    def create_animal(self):
        return Cat()

class DogFactory(Factory):
    def create_animal(self):
        return Dog()

cat_factory = CatFactory()
aniaml = cat_factory.create_animal()
```

토끼가 생성된다면 아래와 같이 rabbit클래스, rabbitFactory를 추가하면된다.

```python
# ...

class Rabbit(Animal):
    pass

class Rabbit(Factory):
    def create_animal(self):
        return Rabbit()
```

불편해보이는가? 클래스가 너무 많이 생성되는 것 같은가? 필요성을 느끼지 못하겠는가? 그렇다면 10개의 동물을 정의하고 `if`문을 사용하여 인스턴스를 생성하고 완료가 되었다면 수정사항으로 2개의 동물이 더 추가되었다고 가정하고 작성해보길 바란다.


## 결론
결국 혼자서 할 수 있는 것은 아무것도 없다.

다른 사람들과 무엇인가를 만들어보고 싶다면, 다른 사람들이 보편적으로 사용하는 규칙을 따르고 나의 코드가 변경되었을 때를 가정하여 코딩을 해나가야 한다고 생각한다.

다른 사람들과 코딩을 하다보면 서로 의견, 생각, 가치관이 다를 것이다.

하지만 세상에는 선택만이 존재할 뿐 정답은 존재하지 않는 것이라 생각된다.

긴 글 읽어주어서 감사하다.

