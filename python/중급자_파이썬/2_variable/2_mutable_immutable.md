# mutable vs immutable

python에서는 immutable 타입과 mutable 타입이 있다.

| immutable | mutable |
|-----------|---------|
| immutable Var | int, float, str, tuple |
| mutable Var | list, dict, set |

## immutable

```python
a = 100
b = 100
c = 100
d = 100

if id(a) == id(b) == id(c) == id(d):
    print("a, b, c, d는 같은 메모리 주소를 가리킨다.")
else:
    print("a, b, c, d는 다른 메모리 주소를 가리킨다.")

print(id(a), id(b), id(c), id(d))
```

보통 C언어에서는 int형식의 변수는 각각 4 or 8바이트 메모리 공간을 차지하지만 파이썬에서는 100이라는 값을 담고 있는 메모리 주소를 가리킨다.

immutable 변수들은 같은 주소를 가리키고, python memory manager는 객체마다 힙에 값을 할당하는 것이 아니라 하나의 값만 힙에 할당하고, 여러 변수들이 그 값을 가리키게 한다.

## mutable

```python

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]
d = [1, 2, 3]

if id(a) == id(b) == id(c) == id(d):
    print("a, b, c, d는 같은 메모리 주소를 가리킨다.")
else:
    print("a, b, c, d는 다른 메모리 주소를 가리킨다.")
```

list타입의 경우 list의 값이 일치하더라도 참조하는 주소가 다르다. 즉, mutable 타입은 각각의 변수가 각각의 메모리 주소를 가리킨다.

> tuple은 immutable이기 때문에 값을 변경하는 경우 메모리에 새로운 주소를 allocation하기 때문에, 변경하는 경우 비싼 time consumption이 발생한다. 하지만, tuple은 해싱을 지원하기 때문에 조회 속도가 빠르다.
