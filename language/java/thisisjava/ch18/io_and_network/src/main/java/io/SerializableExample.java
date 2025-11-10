package main.java.io;

import java.io.*;

public class SerializableExample {
    static class ClassA implements Serializable {
        int field1;
        ClassB field2 = new ClassB();
        static int field3;
        transient int field4;
    }

    static class ClassB implements Serializable{
        int field1;
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
//        write();
        read();
    }

    private static void write() throws IOException {
        FileOutputStream fos = new FileOutputStream("./SerializableExample.dat");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        ClassA ca = new ClassA();
        ca.field1 = 1;
        ca.field2.field1 = 2;
        ca.field3 = 3;
        ca.field4 = 4;
        oos.writeObject(ca);
        oos.flush();oos.close();fos.close();
    }

    private static void read() throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream("./SerializableExample.dat");
        ObjectInputStream ois = new ObjectInputStream(fis);
        ClassA ca = (ClassA) ois.readObject();
        System.out.println("field1: " + ca.field1);
        System.out.println("field2.field1: " + ca.field2.field1);
        System.out.println("field3: " + ca.field3);
        System.out.println("field4: " + ca.field4);
    }
}
