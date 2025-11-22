package file;

import java.io.IOException;
import java.nio.file.FileStore;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class FileExample {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("src/file/FileExample.java");
        System.out.println("is directory? " + Files.isDirectory(path));
        System.out.println("is file? " + Files.isRegularFile(path));
        System.out.println("last edit time? " + Files.getLastModifiedTime(path));
        System.out.println("file size? " + Files.size(path));
        System.out.println("owner? " + Files.getOwner(path).getName());
        System.out.println("is hidden? " + Files.isHidden(path));
        System.out.println("is readable? " + Files.isReadable(path));
        System.out.println("is writable? " + Files.isWritable(path));
    }
}
