# Classmethod, Staticmethod

## Classmethod & Staticmethod
객체가 아닌 클래스에 연산을 수행하는 메서드이다.

- classmethod는 클래스 자체를 첫번째 매개변수로 받는다.
- staticmethod는 클래스를 첫번째 매개변수로 받지 않는다.

```python
class Demo:
    @classmethod
    def class_example_function(*args):
        return args

    @staticmethod
    def static_example_function(*args):
        return args
print(Demo.class_example_function(1, 2, 3))  # (<class '__main__.Demo'>, 1, 2, 3)
print(Demo.static_example_function(1, 2, 3))  # (1, 2, 3)
```
