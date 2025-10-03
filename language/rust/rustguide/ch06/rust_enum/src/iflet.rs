fn main() {
    let config_max = Some(3u8);
    match config_max {
        Some(max) => println!("Max is {}", max),
        None => (),
    }

    let config_max = Some(3u8);
    if let Some(max) = config_max {
        println!("Max is {}", max);
    }

    let config_max: Option<u8> = None;
    if let Some(max) = config_max {
        println!("Max is {}", max);
    }
}