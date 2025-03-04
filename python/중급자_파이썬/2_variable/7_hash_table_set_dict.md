# 2.7 Hash Table, Set, Dict

## Hash Table

Hash Table은 key, value로 데이터를 저장하는 자료구조이다. 빠르게 검색을 할 수 있기 때문에 많이 사용된다.
각 key에 hash 함수를 적용하여 고유한 index를 생성하고, index를 활용하여 값을 저장하기 때문에 빠른 검색이 가능하다.
조회 시간 복잡도는 O(1)이다.

### Hash Collision

key의 개수 k개, 테이블의 크기를 n이라고 할때 적재율을 k/n이라고 한다. 적재율이 넘어갈 경우 탐색과 삭제 연산이 추가되어 O(k)만큼의 시간 복잡도가 생긴다.
또한 메모리는 무한하게 존재하지 않기 때문에 hash collision이 발생할 수 있다.
이를 해결하기 위해 개방 주소법(open addressing)과 분리 연결볍(chaining) 등이 있다.

* 개방 주소법(open addressing)
    * 충돌이 발생하면 다음 index를 탐색하여 저장한다.
    * 탐색을 위해서는 선형 탐색(linear probing), 제곱 탐색(quadratic probing), 이중 해싱(double hashing) 등을 사용한다.

* 분리 연결법(chaining)
    * 충돌이 발생하면 linked list를 사용하여 저장한다.
    * linked list를 사용하기 때문에 메모리를 더 많이 사용한다.
  
## Tuple vs List

tuple 또한 dict와 마찬가지로 hash table을 사용하여 저장된다. tuple은 immutable하기 때문에 hash table을 사용할 수 있다.

### Dictionary

기본적으로 `dict[key] = value` 형태로 사용된다. key는 immutable한 자료형만 사용할 수 있다.

```python
def count_letters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter
count_letters("apple")
#> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```
* setdefault: 해당 키가 없다면 default 값을 설정하고, 있다면 해당 키의 값을 반환한다.
```python
def count_letters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter
count_letters("apple")
#> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```

* get: 
key가 dict에 있으면 value를 반환하고, 없으면 default or None을 반환한다.
```python
def count_letters(word):
    counter = {}
    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1
    return counter
count_letters("apple")
#> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```

* update:
update는 key, value를 수정할 때 사용한다. value를 추가 할 수 도 있다.
```python
x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x.update(a=10)
print(x)

x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x.update({'a': 10, 'b': 20, 'e': 30})
print(x)
```

#### MappingProxyType
```python
from types import MappingProxyType
writable_data = {'a': 1, 'b': 2, 'c': 3}
read_only_data = MappingProxyType(writable_data)
print(read_only_data['a'])
read_only_data['a'] = 10
#> TypeError: 'mappingproxy' object does not support item assignment
```
`read_only_data`는 `writable_data`를 참조하는 read-only dict이다. 수정을 하기 위해서는 원래의 writable_data를 수정해야 한다.

## Set
set은 collection이면서 순서와 중복이 없다. 중복을 허용하지 않는 집합이다.
```python
s = set("Hello")
print(s)
#> {'H', 'e', 'l', 'o'}
```
set은 unordered이기 때문에 인덱싱을 통해 요소값을 얻을 수 없다. set자료형에 저장된 값을 인덱싱으로 접근하기 위해서는 리스트나 튜플로 변환한 후에 가능하다.

### operations
set은 집합의 성격을 가지고 있기 때문에 교집합, 합집합, 차집합 등의 연산을 지원한다.
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
```
### frozenset
frozenset은 immutable한 set이다. hash table을 사용하기 때문에 dict의 key로 사용할 수 있다.
```python
s1 = frozenset({"Apple", "Banana", "Cherry"})
s2 = set({"Apple", "Banana", "Cherry"})
s1.add("Orange")
#> AttributeError: 'frozenset' object has no attribute 'add'
s2.add("Orange")
print(s1)
print(s2)
```