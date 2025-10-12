use std::sync::Mutex;
use std::rc::Rc;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));

    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        // error: Rc cannot be sent between threads safely
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}