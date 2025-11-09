package io;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FileOutputStreamExample {
    public static void main(String[] args) throws IOException {
        String originaFilename = "./src/main/java/io/FileOutputStreamExample.java";

        FileInputStream fis = new FileInputStream(originaFilename);

        int readByteNo;
        byte[] readBytes = new byte[100];
        List<Integer> readByteNumList = new ArrayList<>();
        List<byte[]> readByteList = new ArrayList<>();
        while((readByteNo = fis.read(readBytes)) != -1) {
//            fos.write(readBytes, 0, readByteNo);
            readByteList.add(readBytes);
            readByteNumList.add(readByteNo);
            readBytes = new byte[100];
        }
        fis.close();

        String copyFilename = "./src/main/java/io/FileOutputStreamExample.java";
        FileOutputStream fos = new FileOutputStream(copyFilename, false);

        for(int i=0; i<readByteNumList.size(); i++) {
            fos.write(readByteList.get(i), 0, readByteNumList.get(i));
        }

        fos.flush();
        fos.close();
        System.out.println("copy done.");
    }
}
