package io;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileInputStreamExample {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("./src/main/java/io/FileInputStreamExample.java");
            int data;

            while((data = fis.read()) != -1) {
                System.out.print((char)data);
            }
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
