package chapter12;

import java.util.Map;
import java.util.Set;

public class ThreadInfoExample {
    public static void main(String[] args) {
        AutoSaveThread autoSaveThread = new AutoSaveThread();
        autoSaveThread.setName("AutoSaveThread");
        autoSaveThread.setDaemon(true);
        autoSaveThread.start();

        Map<Thread, StackTraceElement[]> map = Thread.getAllStackTraces();
        Set<Thread> threads = map.keySet();
        for(Thread thread: threads) {
            System.out.println("Name: " + thread.getName() + ((thread.isDaemon())?"(Daemon)":"(no Daemon)"));
            System.out.println("\tgroup: " + thread.getThreadGroup().getName());
            System.out.println();
        }
    }
}
