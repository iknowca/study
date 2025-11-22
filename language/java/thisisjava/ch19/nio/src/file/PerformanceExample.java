package file;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.EnumSet;

public class PerformanceExample {
    public static void main(String[] args) throws IOException {
        Path from = Paths.get("random.bin");
        Path to1 = Paths.get("output1.bin");
        Path to2 = Paths.get("output2.bin");

        long size = Files.size(from);

        FileChannel fileChannelFrom = FileChannel.open(from);
        FileChannel fileChannelTo1 = FileChannel.open(to1, EnumSet.of(StandardOpenOption.CREATE, StandardOpenOption.WRITE));
        FileChannel fileChannelTo2 = FileChannel.open(to2, EnumSet.of(StandardOpenOption.CREATE, StandardOpenOption.WRITE));

        ByteBuffer nonDirectBuffer = ByteBuffer.allocate((int) size);
        ByteBuffer directBuffer = ByteBuffer.allocateDirect((int) size);

        long start, end;
        start = System.nanoTime();
        for(int i=0; i<100; i++) {
            fileChannelFrom.read(nonDirectBuffer);
            nonDirectBuffer.flip();
            fileChannelTo1.write(nonDirectBuffer);
            nonDirectBuffer.clear();
        }
        end = System.nanoTime();
        System.out.println("non direct:\t" + (end - start)/1000 + " ms");

        start = System.nanoTime();
        for(int i=0; i<100; i++) {
            fileChannelFrom.read(directBuffer);
            directBuffer.flip();
            fileChannelTo2.write(directBuffer);
            directBuffer.clear();
        }
        end = System.nanoTime();
        System.out.println("direct:\t\t" + (end - start)/1000 + " ms");
    }
}
