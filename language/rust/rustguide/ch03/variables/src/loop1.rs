fn main() {
    let mut counter = 0;

    let x = loop {
        counter += 1;
        println!("The counter is {}", counter);

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The value of x is: {}", x);
}