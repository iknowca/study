package file;

import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.security.SecureRandom;

public class WriteRandomBinary {
    public static void main(String[] args) {
        int size = 1024 * 1024 * 20;
        byte[] buffer = new byte[size];
        SecureRandom random = new SecureRandom();
        random.nextBytes(buffer);

        try (FileOutputStream out = new FileOutputStream("random.bin")) {
            out.write(buffer);
            out.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
