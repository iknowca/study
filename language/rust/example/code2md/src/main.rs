use code2md::{read_file, get_dir, write_md};
fn main() {
    println!("Hello, code2md!");
    let file_string = read_file("./src/main.rs");
    println!("{:?}",get_dir("./src"));
    write_md("./README.md", &file_string);
}


