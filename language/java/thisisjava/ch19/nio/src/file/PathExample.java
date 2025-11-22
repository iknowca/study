package file;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Iterator;

public class PathExample {
    public static void main(String[] args) {
        Path path = Paths.get("src/file/PathExample.java");
        System.out.println("[filename] " + path.getFileName());
        System.out.println("[parent dir name] " + path.getParent().getFileName());
        System.out.println("[depth] " + path.getNameCount());

        System.out.println();
        for(int i=0; i<path.getNameCount(); i++) {
            System.out.println(path.getName(i));
        }
        System.out.println();

        Iterator<Path> it = path.iterator();
        while(it.hasNext()) {
            Path p = it.next();
            System.out.println(p.getFileName());
        }
    }
}
