unsafe trait Foo {
    fn add_one(&self) -> i32;
}

unsafe impl Foo for i32 {
    fn add_one(&self) -> i32 {
        *self + 1
    }
}

fn main() {
    let x = 10;
    x.add_one();
}