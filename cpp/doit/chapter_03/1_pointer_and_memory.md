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

### 포인터 연산으로 배열의 원소 접근

[array_pointer_1.cpp](./src/array_pointer_1/array_pointer_1.cpp)

배열의 인덱스로 각 원소에 접근하는 것처럼, 포인터 연산을 통해 배열의 원소에 접근할 수 있다.

배열의 첫번째 원소의 주소는 배열의 이름과 동일하다. 따라서 배열의 이름은 배열의 첫번째 원소의 주소를 가리키는 포인터로 취급된다.

포인터 연산에서 덧셈은 자료형의 크기를 곱한 만큼 덧센을 수행한다.

배열이 int 자료형이라면 덧셈한 숫자에 4byte 크기가 곱해진다.

이는 포인터의 사칙 연산과 증감 연산에서도 동일하다.


배열 변수가 가리키는 주소는 배열의 첫번째 원소의 주소이기도 하고, 배열 인덱스의 포인터 연산이 같아서 배열과 포인터가 같다고 생각할 수도 있지만,
배열과 포인터는 엄연히 다르다.

```c++
#include <iostream>

using namespace std;

int main()
{
    int array[5] = {1, 2, 3, 4, 5};
    int* pointer_array = array;

    cout << "Array: " << array << endl;
    cout << "Pointer array: " << pointer_array << endl;

    cout << "sizeof(array): " << sizeof(array) << endl;
    cout << "sizeof(pointer_array): " << sizeof(pointer_array) << endl;

    return 0;
}
```
```
Array: 0x16b1ff220
Pointer array: 0x16b1ff220
sizeof(array): 20
sizeof(pointer_array): 8
```

위의 코드를 확인해보면 array와 pointer_array가 가리키는 주소가 동일하다. 하지만 sizeof(array)와 sizeof(pointer_array)의 값은 다르다.
array는 int[5] 타입이고, pointer_array는 int* 타입이기 때문이다.
array의 sizeof는 4byte * 5가 출력되고, pointer_array의 sizeof는 8byte가 출력된다.

단 배열과 포인터 관계에서, 배열의 원소에 접근할 때, 포인터 연산으로도 가능하다는 것이 중요하다.

[pointer_array_3.cpp](./src/array_pointer_3/array_pointer_3.cpp)

### 동적 메모리 할당

#### 동적 메모리 할당과 해제

dynamic memory allocation은 프로그램 실행중에 필요한 크기의 메모리를 운영체제에 요청하여 사용하는 방법이다.

```c++
type *var_name = new type;
```

`new`로 할당된 메모리는 필요 없는 시점에 `delete`로 해제해야 한다.

```c++
delete var_name;
```

[new_and_delete.cpp](./src/new_and_delete/new_and_delete.cpp)

#### 배열의 동적 메모리 할당과 해제

```c++
type *var_name = new type[size];
```

[new_delete_array.cpp](./src/new_delete_array/new_delete_array.cpp)

#### 동적 할당 메모리를 해제하는 이유

일반 변수와 달리 동적으로 할당한 메모리를 해제해야 하는 이유는 사용하는 메모리의 영역이 다르기 때문이다.

함수의 매개변수나 지역변수처럼 대부분의 일반 변수는 스택에 할당되고, 스택영역은 함수의 호출과 함께 할당되며 함수가 반환되면 자동으로 소멸한다.
반면 동적으로 할당된 변수는 힙에 존재한다. 힙은 스택보다 큰 메모리 풀이기 때문에 크기가 큰 배열도 충분히 할당할 수 있다. 하지만 힙에 할당된 메모리는 명시적으로 해제하기 전에는 계속 유지된다. 메모리를 해제하지 않으면 프로그램이 동작하면서 조금씩 메모리 누수가 누적되고, 메모리를 과다하게 사용하는 문제로 발전하게 된다.

#### 포인터와 동적 메모리 할당

[dynamic_memory.cpp](./src/dynamic_memory/dynamic_memory.cpp)

#### 포인터를 다룰때 주의할 점
포인터는 강력하지만 쉽지 않다. 포인터를 다룰 때는 주의해야 할 점이 있다.

1. 포인터를 역참조 하기전에 포인터가 유효한 메모리를 가리키는지 확인해야한다.
2. 할당된 메모리의 범위를 벗어나는 포인터 연산은 피해야 한다.
3. 할당 해제된 메모리를 역참조 하지 말아야 한다.