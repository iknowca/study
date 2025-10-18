static HELLO_WORLD: &str = "Hello, world!";
static mut COUNTER: u32 = 0;

fn add_to_count() {
    unsafe {
        COUNTER += 1;
    }
}
fn main() {
    println!("{}", HELLO_WORLD);

    add_to_count();
    unsafe {
        // println!("COUNTER: {}", COUNTER);
    }
}