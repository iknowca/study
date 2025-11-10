package main;

import java.io.*;

public class WriteReadObjectMethodExample {
    static class Parent {
        public String field1;
    }

    static class Child extends Parent implements Serializable {
        public String field2;

        private void writeObject(ObjectOutputStream out) throws IOException {
            out.writeUTF(field1);
            out.defaultWriteObject();
        }

        private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
            field1 = in.readUTF();
            in.defaultReadObject();
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        FileOutputStream fos = new FileOutputStream("./write_read_object_method_example.dat");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        Child child = new Child();
        child.field1 = "aaa";
        child.field2 = "bbb";
        oos.writeObject(child);
        oos.flush(); oos.close(); fos.close();

        FileInputStream fis = new FileInputStream("./write_read_object_method_example.dat");
        ObjectInputStream ois = new ObjectInputStream(fis);
        Child c = (Child) ois.readObject();
        System.out.println("field1: " + c.field1);
        System.out.println("field2: " + c.field2);
        ois.close(); fis.close();
    }
}
