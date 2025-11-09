package io;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class FileWriterExample {
    public static void main(String[] args) throws IOException {
        File file = new File("./src/main/java/io/FileWriterExample_testfile.java");
        FileWriter fw = new FileWriter(file, true);
        fw.write("");
        fw.write("test file");
        fw.close();
    }
}
