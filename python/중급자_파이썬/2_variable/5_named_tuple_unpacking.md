# Named Tuple, Unpacking

# Named Tuple

tuple은 immutable 변수로 아래와 같이 사용할 수 있다.
```python
from math import sqrt
import math

pt1 = (1.2, 11.2)
pt2 = (2.21, 1.9)

distance = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
print(math.ceil(distance))
```

name tuple은 tuple이지만, key-value로 사용할 수 있다.
```python
from collections import namedtuple

Point = namedtuple('Point', 'x y')
pt1 = Point(1.2, 11.2)
pt2 = Point(2.21, 1.9)
print(pt1[0])
print(pt3.x)
print(pt3)

# 1.2 
# 1.2 
# point_pair(x=1.2, y=11.2)
```
namedtuple은 namedtuple("Name", "KEY1 KEY2")로 선언할 수 있으며,
value에 접근하기 위해서는 list처럼 인덱스로 접근할 수도 있고, key로 접근할 수도 있다.
> 선언할 때, `namedtuple("Name", "KEY1 KEY2")`, `namedtuple("Name", "KEY1, KEY2"), `namedtuple("Name", ["KEY1", "KEY2"])` 모두 가능하다.

## method
method를 사용하면 간편하게 named tuple을 사용할 수 있다.

### _make

_make를 사용하면 iterable한 객체를 적절하게 unpacking 해준다.
```python
Point_pair_1 = namedtuple("point_pair",  "x y")
Point_pair_2 = namedtuple("point_pair",  "x, y")
Point_pair_3 = namedtuple("point_pair",  ["x", "y"])

sample_points= [10,  100]
p1 = Point_pair_1 ._make(sample_points)
p2 = Point_pair_2 ._make(sample_points)
print(p1)
print(p2)

sample_points_list= [[1,2],[3,4],[5,6]]
p_list = [Point_pair_3 ._make(x)  for x in sample_points_list]
print(p_list)
# point_pair(x=10, y=100) 
# point_pair(x=10, y=100) 
# [point_pair(x=1, y=2), point_pair(x=3, y=4), point_pair(x=5, y=6)]
```
### _fields
_fields를 사용하면 key값을 확인할 수 있다.
```python
Point_pair_1 = namedtuple("point_pair",  "x y")
sample_points= [10,  100]
p1 = Point_pair_1 ._make(sample_points)
print(Point_pair_1._fields)
print(p1._fields)
# ('x', 'y')
# ('x', 'y')
```

### _asdict
_asdict를 사용하면 named tuple을 dictionary로 변환할 수 있다.
```python
Point_pair_1 = namedtuple("point_pair",  "x y")
sample_points= [10,  100]
p1 = Point_pair_1 ._make(sample_points)
print(p1._asdict())  

sample_points_list= [[1,2],[3,4],[5,6]]
p_list = [Point_pair_1 ._make(x)  for x in sample_points_list]
p_dict_list = [p._asdict()  for p in p_list]
print(p_dict_list)
# {'x': 10, 'y': 100} 
# [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]
```

## unpacking
** operator는 딕셔너리 타입을 *operator는 리스트, 튜플 타입을 unpacking할 수 있다.
```python
Point_pair_1 = namedtuple("point_pair",  "x y")
sample_points = [10,  100]
p1 = Point_pair_1 ._make(sample_points)

x, y = p1
print(x ,"and", y)

point_pair_dict = {"x":  10,  "y":  100}
p2 = Point_pair_1(**point_pair_dict )

x, y = p2
print(x ,"and", y)

# 10 and 100
# 10 and 100
```

```python
x, y, *rest = range(5)
print(x,",",y,",",rest)

x, y, *rest = "a","b","c","d","e"
print(x,",",y,",",rest)

x, y, *rest = 1,  2
print(x,",",y,",",rest)
# 0 , 1 , [2, 3, 4] 
# a , b , ['c', 'd', 'e'] 
# 1 , 2 , []
```
