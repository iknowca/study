# Class

객체는 데이터를 뜻하고, 객체의 상태와 행동을 구체화 하는 프로그래밍 패러다임을 OOP라고 한다.
또한 객체의 설계도를 클래스라고 한다.

클래스는 설계도를 뜻하고, 객체를 해당 클래스 타입으로 선언 했을때 선언된 객체를 인스턴스라고 한다.

```python
unit_attac_dict = {
    "테란": 10,
    "저그": 12,
    "프로토스": 15
}

class Unit(Object):
    total_unit_count = 0
    def __init__(self, name):
        self.name = name
        Unit.total_unit_count += 1
    def attack(self):
        return unit_attac_dict.get(self.name, None)
    def __del__(self):
        Unit.total_unit_count -= 1
```

