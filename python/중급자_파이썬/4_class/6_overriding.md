# Overriding

오버라이딩은 부모 클래스에 있는 method를 동일한 이름으로 자식 클래스에서 재정의하는 것이다.

```python
class Parent(object):
    def __init__(self):
        self.value = 10
        print("init: value: ", self.value)
    
    def get_value(self):
        return self.value

class Child(Parent):

    def get_value(self):
        return self.value * 2
```

## 연산자 오버라이딩

파이썬에서는 연산자 오버라이딩을 통해 이미 정의된 magic method를 재정의하여 연산자를 사용할 수 있다.

```python
class SampleOverloading:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return SampleOverloading(self.value + other.value)

    def __sub__(self, other):
        return SampleOverloading(self.value - other.value)

    def __mul__(self, other):
        return SampleOverloading(self.value * other.value)

    def __truediv__(self, other):
        return SampleOverloading(self.value / other.value)

    def __str__(self):
        return str(self.value)
```

다만 타입에 따른 오버로딩을 지원하지 않기 때문에 하나의 연산자에 하나의 연산 방식만 지원한다.

## 다형성

다형성이란 하나의 인터페이스가 여러 형태를 가질 수 있는 것을 의미한다.

```python
import datetime

class Logger(object):
    def log(self, msg):
        print(msg)
    
class TimestampLogger(Logger):
    def log(self, msg):
        message = f"{datetime.datetime.now()}, {msg}"
        super(TimestampLogger, self).log(message)

class DateLogger(Logger):
    def log(self, msg):
        message = f"{datetime.datetime.now().date()}, {msg}"
        super(DateLogger, self).log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()
l.log("Hello")
t.log("Hello")
d.log("Hello")
```