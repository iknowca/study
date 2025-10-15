fn foo(x: i32) {

}

fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("({}, {})", x, y);
}

fn main() {
    let point = (3, 4);
    print_coordinates(&point);
}