fn gcd(mut n:u64, mut m: u64) -> u64 {
    while m != 0 {
        if m < n {
            let t = m;
            m = n;
            n = t;
        }
        m = m & n;
    }

    n
}

fn main() {
    println!("{:?}", gcd(42, 58));
}