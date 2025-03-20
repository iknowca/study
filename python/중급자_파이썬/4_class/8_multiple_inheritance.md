# Multiple_Inheritance

다중상속을 여러개의 클래스를 상속하는 것을 말한다.

```python
class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A, B):
    ...
```

```python
class Animal:
    def bark(self):
        print("Animal: bark")
    
class Mammal:
    def feed(self):
        print("Mammal: feed")

class Dog(Animal, Mammal):
    def name(self):
        print("name: Dog")

dog = Dog()
dog.bark() # Animal: bark
dog.feed() # Mammal: feed
```

## diamond problem
다이아몬드 문제는 다중 상속을 사용할 때 발생하는 문제로, 두 개의 부모 클래스가 동일한 메소드를 가지고 있을 때 자식 클래스에서 어떤 부모 클래스의 메소드를 호출할지 결정할 수 없는 상황을 말한다.

```python
class A:
    def bark(self):
        print("A: bark")
class B(A):
    def bark(self):
        print("B: bark")
class C(A):
    def bark(self):
        print("C: bark")

class D(B, C):
    pass
d = D()
d.bark() # B: bark
```

B와 C는 A를 상속받고, D는 B와 C를 상속받는다.
ABC는 모두 bark() 메소드를 가지고 있다.
이때 D에서 bark() 메소드를 호출하면 B의 bark() 메소드가 호출된다.
하지만, D에서 어떤 메소드를 호출할지 결정할 수 없기 때문에 이런 상황을 ambiguous한 상황이라고 한다.

## MRO
MRO는 Method Resolution Order의 약자로, 메소드 호출 시 어떤 순서로 부모 클래스를 탐색할지를 결정하는 알고리즘이다.
`mro()` 메소드를 사용하여 MRO를 확인할 수 있다.

```python
D.mro()
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

MRO 메서드를 보면 D 클래스는 B 클래스를 먼저 탐색하고, 그 다음 C 클래스를 탐색한다.
D에는 bark메소드가 없기 때문에 B클래스의 bark메소드를 호출한다.

기본적으로 다중상속시 class D(B, C)일때, 클래스 목록중 왼쪽에서 오른쪽 순서로 메서드를 찾는다.
그러므로 같은 메서드가 있다면 B클래스의 메서드가 호출된다.
그러나 상속관계가 복잡하다면 MRO를 사용하여 메서드를 찾는다.