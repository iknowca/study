package chapter12;

public class User1 extends Thread{
    private Calculator calculator;

    public void setCalculator(Calculator calculator) {
        this.calculator = calculator;
    }

    public void run() {
        calculator.setMemory(100);
    }
}
