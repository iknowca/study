package file;

import java.io.*;
import java.nio.file.*;
import java.nio.file.WatchEvent.Kind;
import java.util.List;

public class WatchServiceExample {
    static class WatchServiceThread extends Thread {
        @Override
        public void run() {
            try {
                WatchService ws = FileSystems.getDefault().newWatchService();
                Path path = Paths.get("src/file");
                path.register(ws, StandardWatchEventKinds.ENTRY_CREATE, StandardWatchEventKinds.ENTRY_DELETE, StandardWatchEventKinds.ENTRY_MODIFY);
                while (true) {
                    WatchKey watchKey = ws.take();
                    List<WatchEvent<?>> list = watchKey.pollEvents();

                    for (WatchEvent event: list) {
                        Kind kind = event.kind();
                        Path p = (Path) event.context();
                        if(kind == StandardWatchEventKinds.ENTRY_CREATE) {
                            System.out.println("file created: " + p.getFileName());
                        } else if (kind == StandardWatchEventKinds.ENTRY_MODIFY) {
                            System.out.println("file modified: " + p.getFileName());
                        } else if (kind == StandardWatchEventKinds.ENTRY_DELETE) {
                            System.out.println("file deleted: " + p.getFileName());
                        }
                    }
                    if(!watchKey.reset()) { break;}
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        WatchServiceThread wst = new WatchServiceThread();
        wst.start();
        Thread.sleep(1000);
        File file = new File("src/file/watch_test_file");
        FileOutputStream fos = new FileOutputStream(file);

        Thread.sleep(1000);
        fos.write("hello, world".getBytes());
        fos.flush();
        fos.close();

        Thread.sleep(1000);
//        file.delete();
    }
}
