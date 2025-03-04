# Weak Reference

### 메모리 관리
python은 c의 malloc/free 같은 메모리 관리 기능을 제공하지 않는다. python memory manager가 자동으로 메모리를 관리한다. python memory manager는 counting을 사용하여 메모리를 관리한다. 객체를 참조하면 reference count가 증가하고, 참조가 사라지면 reference count가 감소한다. reference count가 0이 되면 메모리가 해제된다.
> 엄밀하게 말하자면, reference count가 0이 되면 메모리가 해제되는 것이 아니라, reference count가 0이 되면 메모리를 해제할 수 있는 상태가 된다. python은 reference count가 0이 된 객체를 garbage collection을 통해 메모리를 해제한다.

## Weak Reference

counting은 비교적 안전하지만, 순환 참조 가 발생하면, memory leak을 발생시킬 수 있다.

```python
import gc
import weakref

def Weakreference:
    def __init__(self, name):
        self.name = name
        self.f = None
    
    def __del__(self):
        self.f = None
        print(f"{self.name}, {id(self)} is deleted")

x = Weakreference("foo")
y = Weakreference("bar")
gc.enable()

x.f = weakref.ref(y)
y.f = weakref.ref(x)

del x
del y
# foo,135842218676416 is destroyed 
# poo,135842218681648 is destroyed
```
만약 위 코드에서 `x.f = y, y.f = x`로 사용하면, 순환 참조가 발생하여, 메모리 leak이 발생한다. 하지만 `weakref`를 사용하면, 순환 참조가 발생하지 않는다.

weakreaf는 순환 참조를 피하는 목적으로도 사용되지만, 캐시를 위해서도 사용될 수 있다. 만드는데 비싼 객체를 참조하는 경우 계속 유지하는 것이 부담이 될 수 있다. 이런 경우 약한 참조를 사용한다면, 메모리 압력이 높은 시점에 캐시를 파괴하고, 필요한 경우 다시 생성하는 식으로 사용할 수 있다.

```python
# strong reference
class MyClass:
    def __del__(self):
        print("MyClass instance is being deleted")

obj = MyClass()
strong_ref = obj

print("Before deleting obj:")
print(f"obj: {obj}")
print(f"strong_ref: {strong_ref}")

print("After deleting obj:")
print(f"strong_ref: {strong_ref}")
# Before deleting obj:
# obj: <__main__.MyClass object at 0x...>
# strong_ref: <__main__.MyClass object at 0x...>
# After deleting obj:
# strong_ref: <__main__.MyClass object at 0x...>
# MyClass instance is being deleted
```
```python
# weak reference

import weakref
class MyClass:
    def __del__(self):
        print("MyClass instance is being deleted")

obj = MyClass()
weak_ref = weakref.ref(obj)

print("Before deleting obj:")
print(f"obj: {obj}")
print(f"weak_ref: {weak_ref()}")
print(f"weak_ref(): {weak_ref()}")

print("After deleting obj:")
print(f"weak_ref: {weak_ref()}")
print(f"weak_ref(): {weak_ref()}")
# Before deleting obj:
# obj: <__main__.MyClass object at 0x...>
# weak_ref: <weakref at 0x...; to 'MyClass' at 0x...>
# weak_ref(): <__main__.MyClass object at 0x...>
# MyClass instance is being deleted
# After deleting obj:
# weak_ref: <weakref at 0x...; dead>
# weak_ref(): None
```

강한 참조에서는 obj를 삭제해도, strong_ref가 남아있기 때문에, MyClass instance는 삭제되지 않는다. 하지만 약한 참조에서는 obj를 삭제하면, weak_ref도 None이 된다.

이렇게 약한 참조를 사용하면 객체를 필요 이상으로 메모리에 오래 유지하는 것을 피할 수 있기 때문에 리소스를 효율적으로 캐싱하고 관리하는 데 유용할 수 있다.