# Meta Class

파이썬에서는 모든 변수가 객체이다. 그렇다면 클래스도 객체이다. 그렇다면 클래스를 만드는 또 다른 클래스가 있어야 한다. 이것을 메타클래스라고 한다. 또한 메타프로그래밍이란 프로그램을 동적으로 생성 및 컨트롤 하는 기술을 의미한다.

## type
```python
class Sample:
    a = 1
    def custom_sum(self, b, c):
        return b + c

m = Sample()
print(m.custom_sum(1, 2)) # 3
```

이 클래스를 type으로도 표현 할 수 있다.
```python
m = type("MetaSample", (object,), {'a': 1, 'custom_sum': lambda self, b, c: b + c})
print(m.custom_sum(1, 2)) # 3
```