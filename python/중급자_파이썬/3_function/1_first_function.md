# 3-1 First Function

## 일급 객체
일급객체는 아래의 조건을 만족하는 객체를 의미한다.
- 자료 구조로 저장할 수 있다.
- 함수의 인자로 전달할 수 있다.
- 함수의 반환값으로 사용할 수 있다.

## 일급 함수

파이썬에서는 함수 도 일급 객체이기 때문에 일급 함수라고 부른다.
- 함수를 변수에 할당할 수 있다.
- 함수를 인자로 전달할 수 있다.
- 함수를 반환값으로 사용할 수 있다.

### callable
```python
def callable_sample(a):
    return a+1

print(callable(str), callable(list), callable(callable_sample), callable(1))
# True True True False
```

### partial

partial은 인자 중 일부를 고정하여 새로운 함수를 만드는 함수이다.

```python
from functools import partial

def sum(a, b):
    return a + b

sum_five = partial(sum, 5)
sum_five_six = partial(sum, 6)

print(sum_five(10))
print(sum_five_six())
```

### reduce

reduce는 리스트의 모든 요소를 하나로 줄이는 함수이다.

```python
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x + y, data)
print(result)

num_list = [1,  2,  3,100,3,1,-1]
max_num = reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)
# 55 
# 55 
# 55 
# 100
```