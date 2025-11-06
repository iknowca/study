fn main() {
    let mut s = String::from("HELLO");
    print_data(&mut s);
    println!("{}", s);
}

fn print_data(s: &mut String) {
    s.push_str(", world");
    println!("{}", s);
}