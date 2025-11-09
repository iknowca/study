package io;

import java.util.Scanner;

public class ScannerExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("input string: ");
        String inputString = scanner.nextLine();
        System.out.println("input string: " + inputString);
        System.out.println();

        System.out.println("input integer: ");
        int inputInteger = scanner.nextInt();
        System.out.println("input integer: " + inputInteger);
        System.out.println();

        System.out.println("input double: ");
        double inputDouble = scanner.nextDouble();
        System.out.println("input double: " + inputDouble);
    }
}
