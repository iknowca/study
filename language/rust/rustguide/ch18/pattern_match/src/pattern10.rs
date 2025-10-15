fn main() {
    let mut setting_value = Some(5);
    let new_setting_value = Some(10);

    match (setting_value, new_setting_value) {
        (Some(_), Some(10)) => {
            println!("Both are Some and 3");
        }
        (Some(_), Some(_)) => {
            println!("Both are Some");
        },
        _ => {
            setting_value = new_setting_value;
            println!("At least one of them is None");
        }
    }
    println!("At the end: setting_value = {:?}", setting_value);
}