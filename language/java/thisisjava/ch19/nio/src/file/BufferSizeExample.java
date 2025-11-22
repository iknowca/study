package file;

import java.nio.ByteBuffer;

public class BufferSizeExample {
    public static void main(String[] args) {
        ByteBuffer directBuffer = ByteBuffer.allocateDirect(200 * 1024 * 1024);
        System.out.println("direct buffer created");

        ByteBuffer nonDirectBuffer = ByteBuffer.allocate(200 * 1024 * 1024);
        System.out.println("non direct buffer created");
    }
}
