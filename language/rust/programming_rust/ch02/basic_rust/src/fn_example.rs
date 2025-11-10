fn gcd(mut n:u64, mut m: u64) -> u64 {
    while m != 0 {
        println!("{} vs {}", n, m);
        if m < n {
            let t = m;
            m = n;
            n = t;
        }
        m = m % n;
    }

    n
}

fn main() {
    println!("{:?}", gcd(42, 58));
}

#[cfg(test)]
fn test_gcd() {
    assert_eq!(gcd(42, 58), 6);
    assert_eq!(gcd(2* 3 * 5 * 11 * 17, 3 * 7 * 11 * 13 * 19), 3 * 11)
}