fn main() {
    let s = "010-1234-5678";
    println!("{:?}", get_number(s));
}

fn get_number(s: &str) -> Vec<u32> {
    s.chars().into_iter().filter_map(|c| c.to_digit(10)).collect::<Vec<u32>>()
}