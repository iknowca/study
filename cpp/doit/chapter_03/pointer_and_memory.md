# 포인터와 메모리

메모리는 연속된 공강으로 구성되었으며, 각 공간은 고유한 주소로 구별된다. 또한 CPU는 주소를 통해 특정 메모리 공간에 접근한다.
일반적으로 64bit 운영체제에서 char, int, double 타입은 각각, 1byte, 4byte, 8byte의 크기를 가진다.
변수를 선언하면 자료형의 크기에 맞게 공간을 확보한 후 해당 곤간에 데이터를 기록한다.
단, 확보한 실제 공간의 주소는 메모리 상황에 따라 매번 달라질 수 있다.

> 메모리 주소는 물리적 위치에 해당하는 고유 식별자지만, 실제 위치는 운영체제에 의해 런타임중에 변경될 수 있다.

## 포인터와 연산자

포인터는 메모리 주소를 저장하는 변수이다.

```c++
#include <iostream>

int main() {
    char char_value = 'A';
    int int_value = 10;
    double double_value = 3.14;

    char* char_pointer_value = &char_value;
    int* int_pointer_value = &int_value;
    double* double_pointer_value = &double_value;

    return 0;
}
```

### 포인터 변수의 크기

포인터 변수의 크기는 데이터 타입과는 관련이 없다. 모든 포인터 변수의 크기는 동일하다. 포인터 변수는 메모리 주소를 저장하는데 사용되고, 주소의 크기는 시스템 아키텍져에 의해 결정된다.
그래도 포인터 변수를 선언할 때, 데이터 형식을 지정하는 이유는 해당 포인터가 가리키는 데이터의 형식을 명시하기 위해서이다.

### 포인터 변수가 가리키는 데이터에 접근하기

포인터 변수에 저장된 주소를 이용해 데이터에 접근하는 방법은 간접 참조 연산자(*)를 사용하는 것이다.

[pointer.cpp](./src/pointer/pointer.cpp)

포인터 변수 앞에 역참조 연산자 *를 붙이면 해당 포인터가 가리키는 메모리 공간에 접근할 수 있다.

### 다중 포인터

포인터 변수는 다른 포인터 변수를 가리킬 수 있다. 이러한 포인터를 다중 포인터라고 한다.

```c++
#include <iostream>

int main()
{
    int int_value = 123;
    int* int_pointer = &int_value;
    int** int_pointer_pointer = &int_pointer;
    int*** int_pointer_pointer_pointer = &int_pointer_pointer;

    return 0;
}
```

삼중 포인터 변수는 역참조 연산자 *를 세 번 사용해야 해당 포인터가 가리키는 메모리 공간에 접근할 수 있다.

### 배열과 포인터

배열은 변수가 여러개 모인 것으로, 같은 자료형의 변수를 연속으로 늘어놓은 형태다.
배열을 선언하면, `array[index]`같은 형태로 해당 인덱스의 원소에 접근 할 수 있다.

### 배열 선언과 원소 접근

고정 배열은 컴파일 타임에 길이를 알고 있는 배열이다.

[array.cpp](./src/array/array.cpp)