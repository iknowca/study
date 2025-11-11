package main.java.io;

import java.io.*;

public class PrintStreamExample {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("./file1.txt");
        PrintStream ps = new PrintStream(fos);

        ps.println("[프린터 보조 스트림]");
        ps.print("마치 ");
        ps.println("프린트가 출력하는 것처럼");
        ps.println("데이터를 출력한다.");

        ps.flush();
        ps.close();
        fos.close();
    }
}
