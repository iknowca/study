# 멀티스레드

멀티 스레드 애플리케이션에서는 실행중인 스레드가 존재한다면, 프로세스는 종료되지 않으며, 메인스레드가 작업스레드보다 먼저 종료되더라도, 작업 스레드들이 종료될때까지, 프로세스가 종료되지 않는다.

## `Thread`클래스로 스레드 생성
`java.lang.Thread`클래스로 작업 스레드 객체를 직접 생성하기 위해서는 Runnable을 매개값으로 갖는 생성자를 호출해야 한다.
```java
Thread thread = new Thread(target);
```

## `Thread` 하위 클래스로 생성
```java
public class WorkerThread extends Thread {
    @Override
    public void run() {
        //running...
    }
}
```

## 우선순위

자바에서 스레드 스케줄링은 Priority 방식과 Round-Robin방식을 사용한다.
우선순위 방식은 스레드 객체에 우선순위 번호를 부여할 수 있기 때문에 코드로 제어할 수 있지만, 라운드로빈방식은 JVM에 의해 정해지기 때문에 코드로 제어할 수 없다.

우선순위를 변경하기 위해서는 `setPriority()`메소드를 이용한다.

## 동기화 메소드와 동기화 블록

멀티 스레드 프로그램에서 단 하나의 스레드만 실행할 수 있는 코드 영역을 critical section이라고 하며, 자바에서는 critical section을 지정하기 위해 synchronized 메소드와
동기화 블록을 제공한다.

## 스레드 상태

실행 상태: Running
일시 정지 상태: WAITING, TIME_WAITING, BLOCKED

## 스레드 상태 제어
|메소드 | 설명                                                                                              |
|---|-------------------------------------------------------------------------------------------------|
|`interrupt()` | 일시 정지 산태의 스레드에 `InterruptedException`예외를 발생시킨다.                                                 |
|`notify()`, `notifyAll()` | `wait()`메서드에 의해 일시 정지 상태에 있는 스레드를 실행 대기 상태로 만든다.                                                |
|`resume()` | (Deprecated)`suspend()`메서드에 의해 일시 정지 상태에 있는 스레드를 실행 대기 상태로 만든다.                                 |
|`sleep(long ms)`, `sleep(long ms, int ns)` | 주어진 시간동안 일시 정지 상태로 만든다. 주어진 시간이 지나면 자동으로 실행 대기 상태가 된다                                           |
| `join()`, `join(long ms)`, `join(long ms, int ns)` | `join()` 메소드를 호출하면 일시 정지 상태가 된다. 스레드가 종료되거나, 주어진 시간이 지나야 실행 대기 상태가 된다.`                         |
| `wait()`, `wait(long ms)`, `wait(long ms, int ns)` | synchronized 블록 내에서 일시 정지 상태로 만든다, 주어진 시간이 지나거나, `notify()`, `notifyAll()`에 의해 실행 대기상태로 갈 수 있다. |
| `suspend()` | (Deprecated) 스레드를 일시 정지 상태로 만든다. `resume()`으로 실행 되기 상태가 될 수 있다.                                 |
| `yield()` | 실행중 우선순위가 동일한 다른 스레드에게 실행을 양보하고 실행 대기 상태가 된다.                                                   |
| `stop()` | (Deprecated)스레드를 즉시 종료시킨다.                                                                      |