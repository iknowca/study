fn main() {
    let x = Some(5);
    let y = 10;
    match x {
        Some(50) => println!("Got 50"),
        Some(n) if n == y => println!("Matched, n = {:?}", n),
        Some(n) if n != y => println!("Not matched, n = {:?}", n),
        None => println!("Matched some value"),
        // 반드시 필요! 컴파일러가 철저성검사에서 guard를 무시하기 때문에
        _ => println!("Default case, x = {:?}", x),
    }

    println!("At the end: x = {:?}, y = {:?}", x, y);
}