package io;

import java.io.IOException;
import java.io.InputStream;

public class SystemInExample1 {
    public static void main(String[] args) throws IOException {
        System.out.println("==Menu==");
        System.out.println("1. 예금 조회");
        System.out.println("2. 예금 출금");
        System.out.println("3. 예금 입금");
        System.out.println("5. 종료");
        System.out.print("select the menu");

        InputStream is = System.in;
        char inputChar = (char) is.read();
        switch (inputChar) {
            case '1' -> System.out.println("1.");
            case '2' -> System.out.println("2.");
            case '3' -> System.out.println("3.");
            case '4' -> System.out.println("4. ");
            default -> System.out.println("5.");
        }
    }
}
