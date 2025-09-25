package chapter12;

public class WaitNotifyExample {
    public static void main(String[] args) {
        WorkObject workObject = new WorkObject();
        ThreadA3 threadA = new ThreadA3(workObject);
        ThreadB3 threadB = new ThreadB3(workObject);
        threadA.start();
        threadB.start();
    }
}

class ThreadA3 extends Thread {
    private WorkObject workObject;

    public ThreadA3(WorkObject workObject) {
        this.workObject = workObject;
    }

    @Override
    public void run() {
        for ( int i = 0; i < 10; i++) {
            workObject.methodA();
        }
    }
}

class ThreadB3 extends Thread {
    private WorkObject workObject;
    public ThreadB3(WorkObject workObject) {
        this.workObject = workObject;
    }
    @Override
    public void run() {
        for ( int i = 0; i < 10; i++) {
            workObject.methodB();
        }
    }
}