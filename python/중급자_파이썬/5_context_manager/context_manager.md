# Context Manager
python에서 context manager는 with문을 사용하여 자원(resource)을 관리하는 방법입니다.
context manager는 자원을 자동으로 할당하고 해제하는 기능을 제공합니다. 예를 들어, 파일을 열고 작업을 수행한 후 자동으로 파일을 닫는 작업을 context manager가 처리합니다.
또한 리소스 관리 뿐만 아니라 특정 논리를 제공하기 위해 custom context manager를 만들 수 있다.

```python
file = open('test.txt', 'w')
try:
    file.write('Hello, World!')
finally:
    file.close()
```

위와 같은 코드에서 예외가 발생하거나 오류를 처리하기 위해서 filnally블록에 close()를 호출해야 한다.
하지만 context manager를 사용하면 with문을 사용하여 자원을 자동으로 관리할 수 있다.

```python
with open("text.txt", "w") as file:
    file.write("Hello, World!")
```

with 구문은 context manager로 구성되어 있으며, context manager는 `__enter__`와 `__exit__` 두개의 메서드로 구성되어 있다.
with 구문은 __enter__() 메서드를 호출하여 자원을 할당하고, with 블록이 끝나면 __exit__() 메서드를 호출하여 자원을 해제한다.
context manager 블록 내에서 예외 혹은 오류가 발생하는 경우에도 `__exit__`가 호출된다.

```python
class MyFileManager:
    def __init__(self, filename, method):
        self.file_pointer = open(file_name, method)
    
    def __enter__(self):
        return self.file_pointer
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Error: {exc_value, value, traceback}")
        self.file_pointer.close()

with MyFileManager("test.txt", "w") as file:
    file.write("Hello, World!")
```

위와 같이 custom context manager를 만들 수 있다.

```python
import time

class Timer:
    def __init__(self, msg):
        self.__msg = msg

    def __enter__(self):
        self.__start = time.time()
        return self.__start

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Error: {exc_value, value, traceback}")
        else:
            self.__end = time.time()
            print(f"{self.__msg}: {self.__end - self.__start:.2f} seconds")
        return true
with Timer("Execution time") as v:
    time.sleep(2)
```

## with decorator

contextlib 데코레이터를 활용하여 더 간단하게 context manager를 만들 수 있다.
```python
import contextlib
import time

@contextlib.contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    f = open(filename, mode)
    yield f
    file.close()

with file_manager("test.txt", "w") as file:
    file.write("Hello, World!")
```
contextlib.contextmanager 데코레이터를 사용하면 __enter__와 __exit__ 메서드를 구현하지 않고도 context manager를 만들 수 있다.
yield 키워드를 사용하여 자원을 할당하고, with 블록이 끝나면 자동으로 close() 메서드가 호출된다.

```python
import contextlib
import time

@contextlib.contextmanager
def Timer(msg):
    start_time = time.time()
    try:
        yield start_time
    except BaseException as e:
        print(f"{msg, e}")
        raise e
    finally:
        end_time = time.time()
        print(f"{msg}: {end_time - start_time:.2f} seconds")

with Timer("Execution time") as v:
    time.sleep(2)
```