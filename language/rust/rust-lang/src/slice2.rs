fn main() {
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    let first2 = get_first_two(&numbers);
    println!("{:?}", first2);
}

fn get_first_two(numbers: &[i32]) -> &[i32] {
    if numbers.len() < 2 {
        panic!("insufficient data");
    }
    &numbers[0..2]
}