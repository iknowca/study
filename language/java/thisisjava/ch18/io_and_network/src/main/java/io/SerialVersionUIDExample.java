package main.java.io;

import java.io.*;

public class SerialVersionUIDExample {
    static class ClassC implements Serializable {
        static final long serialVersionUID = 1908588509535355997L;
        int field1;
        int field2;
    }

    static void write() throws IOException {
        FileOutputStream fos = new FileOutputStream("./SerialVersionUIDExample.dat");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        ClassC cc = new ClassC();
        cc.field1 = 1;
        oos.writeObject(cc);
        oos.flush();oos.close();fos.close();
    }

    static void read() throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream("./SerialVersionUIDExample.dat");
        ObjectInputStream ois = new ObjectInputStream(fis);
        ClassC cc = (ClassC) ois.readObject();
        System.out.println("field1: " + cc.field1);
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
//        write();
        read();
    }
}
