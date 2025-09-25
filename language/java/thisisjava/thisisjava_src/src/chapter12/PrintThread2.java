package chapter12;

public class PrintThread2 extends Thread{
    public void run() {
        try {
            while (true) {
                System.out.println("running");
                Thread.sleep(1);
            }
        } catch (InterruptedException e) {
            System.out.println("Interrupted");
        }

        System.out.println("Stop");
    }
}
