package chapter12;

import java.awt.*;

public class BeepThread extends Thread{
    @Override
    public void run() {
        Toolkit tk = Toolkit.getDefaultToolkit();
        for(int i=0; i<5; i++) {
            tk.beep();
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
