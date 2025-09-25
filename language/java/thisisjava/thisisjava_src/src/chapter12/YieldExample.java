package chapter12;

public class YieldExample {
    public static void main(String[] args) {
        ThreadA2 threadA = new ThreadA2();
        ThreadB2 threadB = new ThreadB2();

        threadA.start();
        threadB.start();

        try { Thread.sleep(3000); } catch (InterruptedException e) {}
        threadA.work = false;

        try { Thread.sleep(3000); } catch (InterruptedException e) {}
        threadA.stop = true;

        try { Thread.sleep(3000); } catch (InterruptedException e) {}
        threadA.stop = true;
        threadB.stop = true;
    }
}

class ThreadA2 extends Thread {
    public volatile boolean work = true;
    public volatile boolean stop = false;

    public void run() {
        while(!stop) {
            if(work) {
                System.out.println("ThreadA work");
            } else {
                System.out.println("ThreadA yield");
                Thread.yield();
            }
        }
        System.out.println("ThreadA stop");
    }
}

class ThreadB2 extends Thread {
    public volatile boolean work = true;
    public volatile boolean stop = false;

    public void run() {
        while(!stop) {
            if(work) {
                System.out.println("ThreadB work");
            } else {
                System.out.println("ThreadB yield");
                Thread.yield();
            }
        }
        System.out.println("ThreadB stop");
    }
}
