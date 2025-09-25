package chapter12;

public class PrintThread1 extends Thread{
    private boolean stop;

    public void setStop(boolean stop) {
        this.stop = stop;
    }

    @Override
    public void run() {
        while(!stop) {
            System.out.println("PrintThread1");
        }
        System.out.println("PrintThread1 stop");
    }
}
