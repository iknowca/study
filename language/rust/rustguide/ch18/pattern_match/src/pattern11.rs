struct Point {
    x: i32,
    y: i32,
    z: i32,
}

fn main() {
    let p = Point { x: 0, y: 7, z: 3 };
    match p {
        Point { x, y, .. } => println!("The value of y is: {}", y),
    }
}