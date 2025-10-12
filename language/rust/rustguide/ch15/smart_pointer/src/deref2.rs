use std::ops::Deref;
pub struct MyBox2<T>(T);

impl<T> MyBox2<T> {
    pub fn new(x: T) -> MyBox2<T> {
        MyBox2(x)
    }
}

impl<T> Deref for MyBox2<T> {
    type Target = T;
    fn deref(&self) -> &T {
        &self.0
    }
}

fn hello(neme: &str) {
    println!("Hello, {}!", neme);
}

fn main() {
    let m = MyBox2::new(String::from("Rust"));
    hello(&m);
}