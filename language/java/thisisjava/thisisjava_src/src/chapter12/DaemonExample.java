package chapter12;

public class DaemonExample {
    public static void main(String[] args) {
        AutoSaveThread autoSaveThread = new AutoSaveThread();
        autoSaveThread.setDaemon(true);
        autoSaveThread.start();

        try { Thread.sleep(3000); } catch (InterruptedException e) {return;}
        System.out.println("main thread quit");
    }
}
