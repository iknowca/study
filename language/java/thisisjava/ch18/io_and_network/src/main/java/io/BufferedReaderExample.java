package main.java.io;

import java.io.*;

public class BufferedReaderExample {
    public static void main(String[] args) throws IOException {
        InputStream is = System.in;
        Reader reader = new InputStreamReader(is);
        BufferedReader br = new BufferedReader(reader);

        System.out.println("input: ");
        String lineString = br.readLine();

        System.out.println("output: " + lineString);
    }
}
