fn main() {
    let num = Some(5);

    match num {
        Some(x) if x % 2 ==0 => println!("Even"),
        Some(x) => println!("Odd"),
        None => (),
    }
}