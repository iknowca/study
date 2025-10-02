package chapter12;

public class ThreadGroupExample {
    public static void main(String[] args) {
        ThreadGroup myGroup = new ThreadGroup("myGroup");
        WorkThread workThread1 = new WorkThread(myGroup, "workThread1");
        WorkThread workThread2 = new WorkThread(myGroup, "workThread2");

        workThread1.start();
        workThread2.start();

        System.out.println("[main 스레드 그룹의 list() 메서드 출력 내용]");
        ThreadGroup mainGroup = Thread.currentThread().getThreadGroup();
        mainGroup.list();

        try {
            Thread.sleep(3000);
        } catch  (InterruptedException e) {}

        System.out.println("[ myGroup 스레드 그룹의 interrupt()메서드 호출 ]");
        myGroup.interrupt();
    }
}
