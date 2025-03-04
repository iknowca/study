# Variable Scope

## Local Variable

기본적으로 local 변수의 scope는 함수내에서 global은 파일 전체에서 사용할 수 있다.
```python
a = 10
def fooo():
    a = 5
    print(a)
foo()
```

## Global Variable
```python
a = 10
def foo():
    print(a)
```
> 코드가 복잡하고 긴 경우 전역변수 사용은 많은 문제를 야기시킬 수 있기 때문에 전역 변수 사용은 안하는걸 권장한다.

## Non-local

non-local은 클로저에서 사용하는 예약어이다.

```python
def closure_ex():
    total = 0
    def cum_sum(c, n):
        nonlocal total
        for i in range(n):
            total += c
        return total
    return cum_sum

cl = closure_ex()
cl(10, 10)
```
