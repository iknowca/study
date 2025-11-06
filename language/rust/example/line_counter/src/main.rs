use std::fs::File;
use std::io::{BufReader, BufRead};
fn main()  {
    let count = count();
    println!("count: {}", count);
}

fn count() -> usize {
    let file = File::open("./src/main.rs");
    println!("file: {:?}", file);
    let reader = BufReader::new(file.unwrap());

    let mut count = 0;
    for line in reader.split(b'\n') {
        let line = line.unwrap();
        if line.iter().any(|&b| !b.is_ascii_whitespace()) {
            count += 1;
        }
    }

    count
}