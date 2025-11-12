package main.java.network;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;

public class ClientExample {
    public static void main(String[] args) throws IOException {
        Socket socket = null;
        try {
            socket = new Socket();
            System.out.println("Try connect");
            socket.connect(new InetSocketAddress("localhost", 5001));
            System.out.println("connected");

            byte[] bytes = null;
            String message = null;

            OutputStream os = socket.getOutputStream();
            message = "Hello Server";
            bytes = message.getBytes("UTF-8");
            os.write(bytes);
            os.flush();
            System.out.println("data transmitted");

            InputStream is = socket.getInputStream();
            bytes = new byte[100];
            int readByteCount = is.read(bytes);
            message = new String(bytes, 0, readByteCount, "UTF-8");
            System.out.println("data received: " + message);

            os.close();
            is.close();
        } catch (Exception e) { e.printStackTrace();}

        if(!socket.isClosed()) {
            socket.close();
        }
    }
}
