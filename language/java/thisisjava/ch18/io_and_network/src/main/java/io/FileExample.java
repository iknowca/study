package io;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URISyntaxException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FileExample {
    public static void main(String[] args) throws URISyntaxException, IOException {
        File dir = new File("./");
        File file1 = new File(dir, "file1.txt");
        FileWriter fw = new FileWriter(file1);
        if (!dir.exists()) {dir.mkdirs();}
        if (!file1.exists()) file1.createNewFile();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd    a    HH:mm");
        File[] contents = dir.listFiles();

        System.out.println("date, time, type, size, name");
        System.out.println("----------------------------");
        for (File file: contents) {
            System.out.println(sdf.format(new Date(file.lastModified())));
            fw.write(file.getName() + "\n");
            if (file.isDirectory()) System.out.println("\t<DIR>\t\t\t" + file.getName());
            else System.out.println("\t" + file.length() + "\t\t" + file.getName());
        }
        fw.close();

    }
}
