fn main() {
    let s1 = String::from("hello");
    let s2 = s1;

    let len = calculate_length(&s2);
    println!("{}", len);
    println!("{}", s2);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}