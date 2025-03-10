# Generator

제너레이터는 이터레이터를 생성하는 함수로, `yield`와 함께 사용된다. lazy evaluation방식으로 필요한 시점까지 연산을 늦춰서 불필요한 연산을 최소화 한다.

python에서는 iterable 타입으로 collections, text file, list, dict, set, tuple, unpacking, *args등이 있는데, 코루틴과도 사용되며 해당 타입들에서는 기본적으로 iter method를 사용할 수 있다.

```python
t = [1, 2, 3, 4, 5]
print(dir(t))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
for x in t:
    print(x)
# 1
# 2
# 3
# 4
# 5
```

## Yield

yield를 선언하면 해당 라인에서 정지하고, 다음 호출까지 기다리게 된다.
```python
def generator_ex():
    print("start")
    yield "start point"
    print("continue")
    yield "continue point"
    print("end")
    yield "end point"

g = iter(generator_ex())
print(next(g))
# start
# start point
print(next(g))
# continue
# continue point
print(next(g))
# end
# end point
```

함수에 yield가 선언되면 해당 함수는 generator가 된다. generator는 이터레이터를 생성하는 함수로, `yield`와 함께 사용된다. `yield`는 함수를 일시 중지하고 값을 반환하며, 다음 호출 시에는 이전 상태에서 계속 실행된다. 이를 통해 메모리 사용을 줄이고 성능을 향상시킬 수 있다.

### '\_\_next\_\_'

이터레이터는 `__next__` 메서드를 사용하여 다음 값을 가져온다. 이 메서드는 이터레이터 객체에서 호출되며, 다음 값을 반환한다. 만약 더 이상 반환할 값이 없으면 `StopIteration` 예외를 발생시킨다.

```python

class  Spliter():
    def  __init__(self, text):
        self._text = text.split(" ")
    def  __iter__(self):
        for word in  self._text:
            yield word

spliter = Spliter("Hello I am Python")
spliter_iter = iter(spliter)

print(next(spliter_iter))
# Hello
print(next(spliter_iter))
# I
print(next(spliter_iter))
# am
print(next(spliter_iter))
# Python
print(next(spliter_iter))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration