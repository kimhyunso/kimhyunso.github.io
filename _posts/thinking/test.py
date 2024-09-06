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






