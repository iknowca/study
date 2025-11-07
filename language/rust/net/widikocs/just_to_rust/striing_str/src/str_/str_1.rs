fn main() {
    let s = "Hello, world!";

    println!("{}", s);
    println!("s.len: {}", s.len());

    let s = "대한민국";
    println!("{}", s);
    println!("s.len: {}", s.len());
    println!("len s: {}", s.chars().count());
    println!("{}", &s[0..1]);
}