# Overloading

## Inheritance

파이썬에서는 다음과 같이 상속을 구현할 수 있다.
```python
class parent:
    # 부모 클래스

class child(parent):
    # 자식 클래스
    def __init__(self):
        super(child, self).__init__()
        #do something
```

자식 클래스는 부모 클래스의 속성을 상속받아 사용할 수 있다.
자식 클래스의 생성자를 만들면 부모 클래스 생성자가 별도로 호출되지 않기 때문에 명시적으로 호출해야해 한다.

## Overloading

파이썬에서는 오버로딩이 직접 지원되지는 않는다.

### packing
파라미터의 개수를 정할수 없을때 packing으로 해결한다.
```python
class SampleA:
    def add(self, *args):
        result = 0
        for i in args:
            result += i
        return result

a = SampleA()
print(a.add(1, 2, 3)) # 6
print(a.add(1, 2, 3, 4, 5)) # 15
```
### datatype
파라미터의 타입을 정할수 없을때 datatype으로 해결한다.
```python
class SampleB:
    def add(self, a, b):
        if type(a) == int and type(b) == int:
            return a + b
        elif type(a) == str and type(b) == str:
            return a + b
        else:
            raise TypeError("Invalid argument types")
a = SampleB()
print(a.add(1, 2)) # 3
print(a.add("1", "2")) # 12
print(a.add(1, "2")) # TypeError: Invalid argument types
```

### dispatch
`multipledispatch`를 사용하여 오버로딩을 구현할 수 있다.
```bash
pip install multipledispatch
```
먼저 `multipledispatch`를 설치해야 한다.

```python
from multipledispatch import dispatch

class SampleC:
    @dispatch(int,  int)
    def  multiple(x, y):
        return x*y

    @dispatch(int,  int,  int)
    def  multiple(x, y, z):
        return x * y * z

    @dispatch(float,  float,  float)
    def  multiple(x, y, z):
        return x * y * z

c = SampleC()
print(c.multiple(5,  6))
print(c.multiple(5,  6,  5))
print(c.multiple(5.0,  6.0,  12.0))
```