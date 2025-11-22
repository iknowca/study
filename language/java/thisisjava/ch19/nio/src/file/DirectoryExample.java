package file;

import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class DirectoryExample {
    public static void main(String[] args) throws IOException {
        Path p1 = Paths.get("src/file");
        Path p2 = Paths.get("directory_exmaple_file.txt");

        if(Files.notExists(p1)) {
            Files.createDirectories(p1);
        }

        if(Files.notExists(p2)) {
            Files.createFile(p2);
        }

        Path p3 = Paths.get("src");
        DirectoryStream<Path> ds = Files.newDirectoryStream(p3);
        for (Path p: ds) {
            if(Files.isDirectory(p)) {
                System.out.println("[dir]"+p.getFileName());
            } else {
                System.out.println("[file]"+p.getFileName());
            }
        }
    }
}
