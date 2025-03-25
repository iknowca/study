# Abstract Class(abc)

추상클래스는 클래스 내부에 구현되지 않은 method를 갖고 있는 클래스를 의미한다. 구현되지 않은 method는 자식 클래스에서 반드시 구현해야 한다.

```python
from abc import *

class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        ...
```

```python
from abc import *

class  Animal(metaclass=ABCMeta):
    @abstractmethod
    def  bark(self):
        print('animal : bark')

    @abstractmethod
    def  walk(self):
        pass

    def  sleep(self):
        print('animal : sleep')

class  Human(Animal):
    def  thinking(self):
        print('human : thinking') 

class  Dog(Animal):
    def  walk(self):
        print('Dog : walk')

    def  bark(self):
        print('Dog : bark')

# animal = Animal() # error
# human = Human() # error
dog = Dog()
dog.walk()
dog.bark()
dog.sleep()
```