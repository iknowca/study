package main.java.io;

import java.io.*;

public class BufferedOutputStreamExample {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = null;
        FileOutputStream fos = null;
        BufferedInputStream bis = null;
        BufferedOutputStream bos = null;

        int data = -1;
        long start = 0;
        long end = 0;

        fis = new FileInputStream("./IMG_2145.JPG");
        bis = new BufferedInputStream(fis);
        fos = new FileOutputStream("./IMG_2145.JPG.COPY");
        bos = new BufferedOutputStream(fos);
        start = System.currentTimeMillis();
        while((data = bis.read()) != -1) {
            bos.write(data);
        }
        bos.flush();
        end = System.currentTimeMillis();
        bos.close();
        fos.close();
        bis.close();
        fis.close();
        System.out.println("buffered input, buffered output: " + (end-start) + "ms");

        fis = new FileInputStream("./IMG_2145.JPG");
        bis = new BufferedInputStream(fis);
        fos = new FileOutputStream("./IMG_2145.JPG.COPY");

        start = System.currentTimeMillis();
        while((data = bis.read()) != -1) {
            fos.write(data);
        }
        fos.flush();
        end = System.currentTimeMillis();
        fos.close();
        bis.close();
        fis.close();

        System.out.println("buffered input, non buffered output: " + (end-start) + "ms");

        fis = new FileInputStream("./IMG_2145.JPG");
        fos = new FileOutputStream("./IMG_2145.JPG.COPY");
        bos = new BufferedOutputStream(fos);
        start = System.currentTimeMillis();
        while((data = fis.read()) != -1) {
            bos.write(data);
        }
        bos.flush();
        end = System.currentTimeMillis();
        bos.close();
        fos.close();
        fis.close();
        System.out.println("non buffered input, buffered output: " + (end-start) + "ms");

        fis = new FileInputStream("./IMG_2145.JPG");
        fos = new FileOutputStream("./IMG_2145.JPG.COPY");

        start = System.currentTimeMillis();
        while((data = fis.read()) != -1) {
            fos.write(data);
        }
        fos.flush();
        end = System.currentTimeMillis();
        fos.close();
        fis.close();

        System.out.println("non buffered input, non buffered output: " + (end-start) + "ms");
    }
}
