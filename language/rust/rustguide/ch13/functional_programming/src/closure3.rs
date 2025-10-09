fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before calling closure: {:?}", list);
    let mut only_mutates = || list.push(4);
    only_mutates();
    println!("After calling closure: {:?}", list);
}