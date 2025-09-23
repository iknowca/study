package chapter12;

import java.awt.*;

public class BeepPrintExample1 {
    public static void main(String[] args) {
        Toolkit tk = Toolkit.getDefaultToolkit();
        for(int i=0; i<5; i++) {
            tk.beep();
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
        for(int i=0; i<5; i++) {
            System.out.println("띵");
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
