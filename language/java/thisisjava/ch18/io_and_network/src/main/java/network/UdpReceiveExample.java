package main.java.network;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class UdpReceiveExample {
    public static void main(String[] args) throws SocketException, InterruptedException {
        DatagramSocket datagramSocket = new DatagramSocket(5001);

        Thread thread = new Thread() {
            @Override
            public void run() {
                System.out.println("start recevied");
                try {
                    while(true) {
                        DatagramPacket packet = new DatagramPacket(new byte[100], 100);
                        datagramSocket.receive(packet);

                        String data = new String(packet.getData(), 0, packet.getLength(), "UTF-8");
                        System.out.println("message: " + packet.getSocketAddress() + ": " + data);
                    }
                } catch (IOException e) {
                    System.out.println("end");
                }
            }
        };

        thread.start();

        Thread.sleep(10000);
        datagramSocket.close();
    }
}
