package file;

import java.io.IOException;
import java.nio.file.FileStore;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Path;

public class FileSystemExample {
    public static void main(String[] args) throws IOException {
        FileSystem fileSystem = FileSystems.getDefault();
        for(FileStore store: fileSystem.getFileStores()) {
            System.out.println("[driver name] " + store.name());
            System.out.println("[file system] " + store.type());
            System.out.println("[total system] " + store.getTotalSpace()/1024/1024/1024 + "giga bytes");
            System.out.println("[available system] " + store.getUsableSpace()/1024/1024/1024 + "giga bytes");
            System.out.println("[used system] " + store.getUnallocatedSpace()/1024/1024/1024 + "giga bytes");
            System.out.println();
        }

        System.out.println("[file separator] " + fileSystem.getSeparator());
        System.out.println();

        for(Path path: fileSystem.getRootDirectories()) {
            System.out.println(path.toString());
        }
    }
}
