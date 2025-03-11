# Property

@property는 python의 표준 빌트인 데코레이터다.

```python
class PropertySample:
    def __init__(self):
        self.x = 0
        self._z = 0
        self.__y = 0

    def get_y(self):
        return self.__y
    def set_y(self, value):
        self.__y = value

sample = PropertySample()
sample.__y
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'PropertySample' object has no attribute '__y'
```

`__y`는 private 속성으로, 외부에서 접근할 수 없다. `get_y`와 `set_y` 메소드를 통해 접근할 수 있다.

> 단, python에서는 엄밀하게 private 속성을 지원하지 않는다. `__y`는 `_PropertySample__y`로 변경되어 접근할 수 있다. 하지만, 이는 권장되지 않는다.
> 또는 `sample.__y`와 같이 접근할 수 있다. 

```python
class PropertySample:
    def  __init__(self):
        self.x = 0
        self._z = 0
        self.__y = 0
    @property
    def  y(self):
        return  self.__y
    @y.setter
    def  y(self, value):
        self.__y = value
    @y.deleter
    def  y(self):
        del  self.__y
sample = PropertySample()
sample.y = 2
del sample.y
```