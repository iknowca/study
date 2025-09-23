package chapter12;

import java.util.ArrayList;
import java.util.List;

public class PriorityExample {
    public static void main(String[] args) {
        List<Thread> threadList = new ArrayList<>();
        for(int i=0; i<=40; i++) {
            Thread thread = new CalcThread("thread" + i);
            if(i != 0) {
                thread.setPriority(Thread.MIN_PRIORITY);
            } else {
                thread.setPriority(Thread.MAX_PRIORITY);
            }
            threadList.add(thread);
        }
        for(Thread thread : threadList) {
            thread.start();
        }
    }
}
