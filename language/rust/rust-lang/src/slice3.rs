fn main() {
    let s: String = String::from("hello");
    let s1: &str = &s[1..4];
    let s2: &str = &s;

    println!("s1: {}, s2: {}", s1, s2);
}