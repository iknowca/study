use std::thread;
use std::time::Duration;

fn main() {
    let time = Duration::from_secs(1);
    let expensive_closure = |num: u32| -> u32 {
        println!("Calculating slowly...");
        thread::sleep(time);
        num
    };
    let result = expensive_closure(5);
    println!("The result is: {}", result);
}