fn main() {
    let a:[i32; 5] = [1, 2, 3, 4, 5];

    println!("{:?}", &a[0..2]);
    println!("{:?}", &a[1..4]);
    println!("{:?}", &a[..4]);
    println!("{:?}", &a[1..]);
    println!("{:?}", &a[..]);
}