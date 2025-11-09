package main.java.io;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class BufferedInputStreamExample {
    public static void main(String[] args) throws IOException {
        long start = 0;
        long end = 0;
        String filename = "../../../../../deeplearning/deeplearning_from_scratch/vol1/ch03/asset/img/SQL 개발자 과외노트.pdf";


        FileInputStream fis2 = new FileInputStream(filename);
        BufferedInputStream bis = new BufferedInputStream(fis2);
        start = System.currentTimeMillis();
        while (bis.read() != -1) {}
        end = System.currentTimeMillis();

        System.out.println("File Input Stream: " + (end - start) + "ms");
        bis.close();
        fis2.close();

        FileInputStream fis1 = new FileInputStream(filename);
        start = System.currentTimeMillis();
        while (fis1.read() != -1) {}
        end = System.currentTimeMillis();
        System.out.println("File Input Stream: " + (end - start) + "ms");
        fis1.close();
    }
}
