fn main() {
    let mut address = 0x012345usize;
    let r = address as *const i32;
    address = address + 1;
    println!("{:p}", r);
    println!("{:p}", address as *const i32);
}