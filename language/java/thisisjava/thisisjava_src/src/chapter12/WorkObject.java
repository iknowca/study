package chapter12;

public class WorkObject {
    public synchronized void methodA() {
        System.out.println("methodA()");
        notify();
        try {
            wait();
        } catch (InterruptedException e) {
        }
    }

    public synchronized void methodB() {
        System.out.println("methodB()");
        notify();
        try {
            wait();
        } catch (InterruptedException e) {
        }
    }
}
