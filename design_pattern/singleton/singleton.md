# Singleton

싱글톤 패턴은 디자인 패턴중 하나로, 특정 클래스의 인스턴스를 오직 하나만 생성하고, 그 인스턴스에 전역적으로 접근할 수 있도록 하는 방식이다.

* 자원공유: 시스템 전체에서 공통적으로 사용되는 객체를 하나만 생성해서 관리함으로써 메모리 사용을 최적화 할 수 있다.
* 전역 상태관리: 여러 객체가 하나의 인스턴스를 참조하게 되어 일관성을 유지할 수 있다.
* 제어와 동기화: 멀티스레드 환경에서 한 인스턴스만 존재하도록 동기화 할수 있다.

## 구현 방식
1. 생성자 은닉: 클래스의 생성자를 `private` 또는 내부적으로 접근할 수 없게 하여, 외부에서 새로운 인스턴스를 생성하지 못하도록 한다.
2. 정적 인스턴스 변수: 클래스 내부에 유일한 인스턴스를 저장할 정적 변수를 선언한다.
3. 전역 접근 메소드: 해당 인스턴스를 반환하는 정적 메소드를 제공하여, 필요할 때마다 인스턴스를 가져올 수 있도록 한다.

### C++

```cpp
class Singleton {
private:
    static Singleton* instance;

    // 생성자
    Singleton() {}
public:
    // 인스턴스를 반환하는 정적 메소드
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }
};
Singleton* Singleton::instance = nullptr;
```

### Java

```java
public class Singleton {
    private static Singleton instance;

    private Singleton() {
        // 생성자
    }

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```
### Python

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```

## 고려 사항

* 테스트: 전역 상태를 갖기 때문에 단위 테스트나 모킹이 복잡해질수 있다.
* 병렬처리: 멀티 스레슫 환경에서는 인스턴스 생성시 동기화를 통해 여러 스레드가 동시에 생성하지 않도록 주의해야 한다.
* 유연성 제한: 확장성이 떨어질 수 있으므로, 정말 필요한 경우에만 사용해야 한다.