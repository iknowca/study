use std::fs;
use std::env;
fn main() -> std::io::Result<()> {
    let path = env::args().nth(1).unwrap_or_else(|| ".".to_string());
    let entries = fs::read_dir(path)?;
    for entry in entries {
        let entry = entry?;
        println!("{}", entry.file_name().to_string_lossy());
    }

    Ok(())
}
