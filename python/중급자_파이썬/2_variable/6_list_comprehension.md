# List Comprehension

리스트 컨프리헨션을 사용하는 이유는 코드를 간결하게 만들수 있고, 추가적인 장점이 존재한다.
1. CPython에서 list Comprehension에 대한 별도의 최적화된 구현이 존재하기 때문에 for loop보다 빠르다.
2. 단일 표현식으로 불필요한 변수 할당 및 temp 변수 생성등으로 인한 오버헤드가 줄어든다.
3. for loop 내부의 성격마다 다를 수 있지만, 최악의 경우 for loop에서 iteration마다 함수 호출이 발생할 수 있는 반면, list comprehension은 한번의 함수 호출로 처리가 가능하다.

```python
import time

end_number = 1000000
start_time = time.time()
number_list = [i for i in range(end_number)]
print('List Comprehension Time:', time.time() - start_time )
start_time = time.time()
numbers = []
for i in  range(end_number):
    numbers.append(i)
print('For loop Time:', time.time()-start_time)
# List Comprehension Time: 0.3237941265106201 
# For loop Time: 0.5245461463928223
```
