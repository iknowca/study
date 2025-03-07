# Decorator

데코레이터란 다른 함수를 인자로 받는 Callable 객체이다.

```python
def target():
    print("running")
t = decorate(target)
```

위의 함수를 데코레이터를 사용하면 아래와 같이 구현할 수 있다.

```python
@decorate
def target():
    print("running")
```

데코레이터를 코드의 간결성의 위한 구문으로 사용하기도 하지만, 주로 로깅, 권한 체크, 캐싱, 트랜잭션 처리와 같은 부가적인 기능을 추가하기 위해서도 사용된다.

```python

import time

def clock(func):
    def clocked(*args):
        start_time = time.time()
        result = func(*args)
        print(f"real sleep time: {time.time() - start_time}")
        print(f"function name: {func.__name__}")
        return result
    return clocked

def time_func(seconds):
    print(f'sleep time: {seconds}')
    time.sleep(seconds)
    return 'finish_time_func'

deco = clock(time_func)
deco(1.5)
```

위와 같은 코드를 데코레이터로는 다음과 같이 구현할 수 있다.

```python
import time

def  clock(func):
    def  clocked(*args):
        start_time = time.time()
        result = func(*args)
        print(f'real sleep time : {time.time() - start_time}')
        print(f'function name : {func.__name__}')
        return result
    return clocked

@clock
def  time_func(seconds):
    print(f'sleep time : {seconds}')
    time.sleep(seconds)
    return  "finish_time_func"

time_func(1.5)
```

## built in decorator

### functolls.lru_cache
LRU(Least Recently Used) 캐시를 구현하는 데코레이터이다. 메모리 사용량을 줄이기 위해서 가장 오래된 캐시를 삭제하는 방식으로 동작한다.

```python
import time
from functools import lru_cache

@lru_cache(maxsize=32)
def  my_fibo(n):
    if n == 0  :
        return  0
    elif n == 1  or n == 2:
        return  1
    else:
        return my_fibo(n-1) + my_fibo(n-2)

start_t = time.time()
print(my_fibo(10))
print("time : ", time.time()- start_t)
```
maxsize는 호출한 인수의 결과를 최대 32회까지 캐싱한다는 의미이다. 

## 매개변수가 있는 데코레이터

데코레이터에서 매개변수를 사용하고 싶다면, 함수를 하나 더 만들어야 한다.

```python
def  is_multiple(x):
    def  my_decorator(func):
        def  my_func(a, b):
            result = func(a, b)
            print(f'function name : {my_func.__name__}')
            if result %x == 0:
                print(f"{x}'s multiple number!")
            else:
                print(f"{x}'s non-multiple number!")
            return result 
        return my_func
    return my_decorator

@is_multiple(2)
def  add(a, b):
    sum = a+b
    print(f"sum : {sum}")
    return sum

print(add(2,  1))
print(add(10,  22))
```

디버깅을 할때, 함수의 원래 이름을 알고 싶다면, `functools.wraps`를 사용하면 된다.

```python
import functools

def  is_multiple(x):
    def  my_decorator(func):
        @functools.wraps(func)
        def  my_func(a, b):
            r = func(a, b)
            print(f'function name : {my_func.__name__}')
            if r%x == 0:
                print(f"{x}'s multiple number!")
            else:
                print(f"{x}'s non-multiple number!")
            return r
        return my_func
    return my_decorator

@is_multiple(3)
@is_multiple(7)
def  add(a, b):
    return a + b

add(10,  20)
```