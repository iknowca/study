# Lambda

람다는 익명함수로 코드가 간결해지지만, 무분별한 사용은 가독성을 떨어뜨릴 수 있다. 람다 함수는 주로 일회성으로 사용되며, 간단한 연산을 수행하는 데 적합하다.

힙 영역에서 사용되며, 사용 완료시 힙영역에서 제외된다.

## Map

map() 함수는 iterable한 객체의 각 요소에 대해 주어진 함수를 적용하여 새로운 iterable 객체를 반환한다. 주로 리스트, 튜플, 세트 등과 함께 사용된다.

```python
# only using map
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```
```python
# using lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```
```python
# using closure
numbers = [1, 2, 3, 4, 5]
def func(nums):
    def double_squre(x):
        return x ** 2
    return map(double_squre, nums)

squared_numbers = list(func(numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

map은 lazy evaluation을 지원하여, 필요한 시점까지 연산을 늦춰 불필요한 연산을 최소화한다.
iterable 객체를 순회하면서 함수를 적용하고, 결과를 새로운 iterable 객체로 반환한다. 하지만, 실제로 변환된 결과값들이 생성되는 방식이 아니라 필요할 때마다 계산되는 방식이다. 따라서, 메모리 사용량이 적고 성능이 향상된다.

## Filter

filter() 함수는 iterable한 객체의 각 요소에 대해 주어진 조건을 만족하는 요소만을 필터링하여 새로운 iterable 객체를 반환한다. 주로 리스트, 튜플, 세트 등과 함께 사용된다.

```python
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)  # [2, 4]
```
```python
numbers = [1, 2, 3, 4, 5]

def func(numbers):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, numbers)
result = list(func(numbers))
print(result)  # [2, 4]
```

## Reduce
reduce() 함수는 iterable한 객체의 각 요소에 대해 주어진 함수를 누적적으로 적용하여 단일 값을 반환한다. 주로 리스트, 튜플, 세트 등과 함께 사용된다.

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # 15
```
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def func(numbers):
    def add(x, y):
        return x + y
    return reduce(add, numbers)

result = func(numbers)
print(result)  # 15
```
