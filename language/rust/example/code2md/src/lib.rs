use std::fs::{File, read_dir};
use std::io::{BufRead, BufReader, Write};

pub fn read_file(filename: &str) -> String {
    println!("Reading file: {}", filename);
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut lines = String::new();
    for line in reader.lines() {
        let line = line.unwrap();
        if line.len() > 0 {
            lines.push_str(&line);
            lines.push('\n');
        }
    }
    lines
}

pub fn get_dir(path: &str) -> Vec<String> {
    let mut files = Vec::new();
    for entry in read_dir(path).unwrap() {
        let entry = entry.unwrap();
        let path = entry.path();
        if path.is_file() {
            files.push(path.to_str().unwrap().to_string());
        }
    }
    files
}

pub fn write_md(path: &str, content: &str) {
    let prefix = "```rust";
    let suffix = "```";
    let mut file = File::create(path).unwrap();
    file.write_all(format!("{}\n{}\n{}\n", prefix, content, suffix).as_bytes()).unwrap();
}