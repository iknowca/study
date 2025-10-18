
fn main() {
    type Kilometers = i32;

    let x: i32 = 5;
    let y: Kilometers = 5;

    println!("x = {}, y = {}", x, y);

    let f: Box<dyn Fn() + Send + 'static> = Box::new(|| println!("hi"));
    fn takes_long_type(_f: Box<dyn Fn() + Send + 'static>) { }
    fn returns_long_type() -> Box<dyn Fn() + Send + 'static> { Box::new(|| println!("hi")) }

    type Thunk = Box<dyn Fn() + Send + 'static>;
    let f: Thunk = Box::new(|| println!("hi"));
    fn takes_long_type2(f: Thunk) { }
    fn returns_long_type2() -> Thunk { Box::new(|| println!("hi")) }
}