fn main() {
    let x: i32;
    x = 0;
    let mut s = String::from("hello");
    s.push_str(" World!");
    println!("{}", s);

    let s2 = s;
    println!("s2: {}", s2);
    // println!("s: {}", s);

}