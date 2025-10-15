struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x: a, y: b } = p;
    println!("The value of a is: {}", a);
    println!("The value of b is: {}", b);

    let Point { x, y } = p;
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);

    match p {
        Point { x: 0, y: 0 } => println!("Origin"),
        Point { x, y: 0 } => println!("On the x-axis with an x value of {}", x),
        Point { x: 0, y } => println!("On the y-axis with a y value of {}", y),
        Point { x, y } => println!("The value of x is: {}, and y is: {}", x, y),
    }
}