package chapter12;

public class DataBox {
    private String data;

    public synchronized String getData() {
        if(this.data == null) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }

        String returnValue = data;
        System.out.println("Data by Consumer Thread: " + returnValue);
        data = null;
        notify();
        return returnValue;
    }

    public synchronized void setData(String data) {
        if(this.data != null) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }

        this.data = data;
        System.out.println("Data by Producer Thread: " + data);
        notify();
    }
}
