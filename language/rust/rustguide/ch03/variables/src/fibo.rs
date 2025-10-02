fn fibo(n: i32) -> i64 {
    if n == 0 { 0 }
    else if n == 1 { 1

    } else { fibo(n - 1) + fibo(n - 2) }
}

fn main() {
    println!("{}", fibo(10));
}