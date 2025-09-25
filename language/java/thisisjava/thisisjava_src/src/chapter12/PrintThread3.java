package chapter12;

public class PrintThread3 extends Thread{
    public void run() {
        while(true) {
            System.out.println( "PrintThread3");
            if (Thread.interrupted()) {
                break;
            }
        }
        System.out.println("Stop");
    }
}
