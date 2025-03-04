# Deep copy vs Shallow copy

## Shallow copy

얕은 복사는 "=", copy함수, [:]를 사용하여, 구현할 수 있다.
```python
arr_1 = [1, 2, 3]
arr_2 = arr_1

print(f'arr_1: {arr_1}')
print(f'arr_2: {arr_2}')

print(f'arr_1 id: {id(arr_1)}')
print(f'arr_2 id: {id(arr_2)}')

arr_2.append(4)
print(f'arr_1: {arr_1}')
print(f'arr_2: {arr_2}')

print(f'arr-1 id: {id(arr_1)}')
print(f'arr-2 id: {id(arr_2)}')
```

mutalble 객체는 얕은 복사한 객체의 값을 수정하면 같은 주소를 바라보기 때문에 원본의 값또한 수정된다.

```python
a = 1
b = a

print(f'a: {a}')
print(f'b: {b}')

print(f'a id: {id(a)}')
print(f'b id: {id(b)}')

b += 1

print(f'a: {a}')
print(f'b: {b}')

print(f'a id: {id(a)}')
print(f'b id: {id(b)}')
```

immutable 객체는 얕은 복사한 객체의 값을 수정하면 원본은 수정되지 않고 다른 주소를 참조한다.

slice와 copy는 동일한 경향을 갖는다.

```python
import copy

arr_1 = [1, 2, 3, [4, 5, 6]]
arr_2 = arr_1[:]
arr_3 = copy.copy(arr_1)

print(f'arr_1: {arr_1}')
print(f'arr_2: {arr_2}')
print(f'arr_3: {arr_3}')
```

각각의 mutalble객체가 독립된 주소를 갖지만,

```python
print(f'arr_1 id: {id(arr_1[3])}')
print(f'arr_2 id: {id(arr_2[3])}')
print(f'arr_3 id: {id(arr_3[3])}')
```

내부의 mutalble 객체는 같은 주소를 참조한다.

## Deep copy

깊은 복사는 list of list, list of dict 등의 모든 객체가 원본과 동일한 주소를 참조하지 않도록 복사하는 방법이다.

```python
import copy

arr_1 = [1, 2, 3, [4, 5, 6]]
arr_2 = copy.deepcopy(arr_1)

print(f'arr_1 id: {id(arr_1)}')
print(f'arr_2 id: {id(arr_2)}')

print(f'arr_1[3] id: {id(arr_1[3])}')
print(f'arr_2[3] id: {id(arr_2[3])}')

arr_2[3].append(7)
print(f'arr_1: {arr_1}')
print(f'arr_2: {arr_2}')
```

## `==` and `is`

`==`는 값이 같은지 비교하고, `is`는 주소가 같은지 비교한다.

```python
a = [1, 2, 3]
b = a
b is a
b == a
```



