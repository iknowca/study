struct Point<T> {
    x: T,
    y: T,
}

struct Point2<T, U> {
    x: T,
    y: U,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };

    let integer = Point2 { x: 5, y: 10.4 };
    let float = Point2 { x: 1.0, y: 4.0};
}