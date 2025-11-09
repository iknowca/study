package io;

import java.io.Console;

public class ConsoleExample {
    public static void main(String[] args) {
        Console console = System.console();

        System.out.println("Id: ");
        String id = console.readLine();

        System.out.println("Password: ");
        char[] password = console.readPassword();
        String passwordStr = new String(password);

        System.out.println("id: " + id + ", password: " + passwordStr);
    }
}
