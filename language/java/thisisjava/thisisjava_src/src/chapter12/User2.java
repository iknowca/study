package chapter12;

public class User2 extends Thread{
    private Calculator calculator;

    public void setCalculator(Calculator calculator) {
        this.calculator = calculator;
    }

    public void run() {
        calculator.setMemory(50);
    }
}
