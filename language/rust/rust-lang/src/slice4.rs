fn main() {
    let s_temp:&str;
    {
        let s = String::from("hello");
        let first2:&str = get_first_two(&s);
        s_temp = first2;
    }
    println!("{}", s_temp);
}

fn get_first_two(s: &str) -> &str {
    if s.len() < 2 {
        panic!("insufficient data");
    }
    return &s[0..2];
}