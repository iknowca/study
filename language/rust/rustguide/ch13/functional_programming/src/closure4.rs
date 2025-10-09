use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("{:?}", list);
    thread::spawn(move || {
        println!("{:?}", list);
    }).join().unwrap();
}