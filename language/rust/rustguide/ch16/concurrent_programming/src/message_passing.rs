use std::sync::mpsc;
use std::thread;
fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        tx.send(String::from("world")).unwrap();
    });



    let received = rx.recv().unwrap();
    println!("Got: {}", received);
    let received = rx.recv().unwrap();
    println!("Got: {}", received);
}