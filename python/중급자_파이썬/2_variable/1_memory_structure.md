# memory structure

## 메모리 구조

컴퓨터 언어로 프로그램을 구현하고 실행하면, 프로그램은 컴퓨터의 메모리에 저장되어 실행된다. 이때, 프로그램에서 사용하는 변수들은 메모리에 저장되어 사용된다. 이번 장에서는 파이썬에서 변수가 메모리에 저장되는 방식을 알아보자.

메인 메모리는 크게 code region, data region, heap region, stack region으로 나뉜다.

* code region:
    * 프로그램의 코드가 저장되는 영역
    * CPU가 저장된 코드를 읽어 실행한다.
    * 기계어로 변환된 코드가 저장된다.
* data region:
    * 전역변수 (global)
    * 정적변수 (static)
    * 프로그램 종료시 소멸
* heap region:
    * 동적할당된 메모리가 저장되는 영역
    * Runtime에 할당되고 소멸된다.
    * 메모리를 해제하지 않으면 메모리 누수가 발생한다.
    * FIFO 방식으로 메모리를 할당한다.
* stack region:
    * 지역변수 (local)
    * 매개변수 (parameter)
    * 함수 호출시 생성되고 함수 종료시 소멸
    * LIFO 방식으로 메모리를 할당한다.
    * Compile time에 할당되고 소멸된다.

## 메모리 할당

보통 힙의 크기가 크고 동적으로 사용할 수 있으므로, 동적할당으로 힙 영역을 사용하는 것이 좋다.

C 계열에서는 malloc, new를 사용하면 직접 메모리에 할당할 수 있지만, python에서는 이러한 작업을 python memory manager가 대신한다.

python에서는 모든 변수가 객체기 때문에 python memory manager가 모든 객체들을 힙에 할당하고, 해제한다.

```python
def foo(k):
    k += 10
    return k

def poo(y):
    y *= 10
    p = foo(y)
    return p

def main():
    x = 10
    z = poo(x)
```
1. 먼저 x변수에 10이라는 데이터가 저장되었다. 여기서 x는 python에서는 int class의 객체이고 stack에는 x의 주소(pointer)가 저장, value는 해당 주소(포인터가 가리키키는 주소)에 저장된다.
   
2. poo는 function이므로 stack영역에 해당 function의 시작점의 주소가 저장된다.
   
3. 계산결과(10*10)에 의해 poo 함수에서 새로 생성된 변수y는 100을 저장한 heap의 주소를 stack에 저장한다.
   
4. foo를 만나 stack영역에 foo 함수의 주소가 push back되고 여기서 변수 k가 생성되며 heap의 110을 가리키는 주소를 stack에 저장한다.
   
5. stack에 저장된 foo가 먼저 완료되고 메모리 해제가 필요한 객체가 있다면 해제를 시도하고(여기서는 해당사항이 없음) 객체 p가 객체 k가 가리키던 110을 가리키게 된다.
   
6. stack에 저장된 poo가 해제 될때 객체y가 가리키는 100이 heap에서 해제된다.(GC에 의해 python memory manager가 해제)
   
7. main의 z객체가 p객체가 가리키던 110을 가리키게 된다.
