package main.java.network;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.net.SocketException;

public class UdpSendExample {
    public static void main(String[] args) throws IOException {
        DatagramSocket datagramSocket = new DatagramSocket();
        System.out.println("start transmission");

        for (int i=0; i<3; i++) {
            String data = "message" + i;
            byte[] bytes = data.getBytes("UTF-8");
            DatagramPacket packet = new DatagramPacket(
                    bytes, bytes.length, new InetSocketAddress("localhost", 5001)
            );

            datagramSocket.send(packet);
            System.out.println("count byte: " + bytes.length + " bytes");
        }
        System.out.println("end of transmission");
        datagramSocket.close();
    }
}
