package chapter12;

public class SumThread extends Thread{
    private long sum;

    public long getSum() {
        return sum;
    }

    public void setSum(long sum) {
        this.sum = sum;
    }

    public void run() {
        for(long i=0; i<1000; i++) {
            sum += i;
        }
    }
}
