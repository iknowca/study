package chapter12;

public class ThreadNameExample {
    public static void main(String[] args) {
        Thread mainThread = Thread.currentThread();
        System.out.println("프로그램 시작 스레드 이름: " + mainThread.getName());

        ThreadA threadA = new ThreadA();
        System.out.println("작업 스레드 이름: " + threadA.getName());
        threadA.start();

        ThreadB threadB = new ThreadB();
        System.out.println("작업 스레드 이름: " + threadB.getName());
        threadB.start();
    }
}

class ThreadA extends Thread {
    public ThreadA() {
        setName("ThreadA");
    }

    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(getName() + "가 출력한 내용");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}

class ThreadB extends Thread {
    public ThreadB() {
        setName("ThreadB");
    }

    public void run() {
        for (int i = 0; i < 2; i++) {
            System.out.println(getName() + "가 출력한 내용");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
