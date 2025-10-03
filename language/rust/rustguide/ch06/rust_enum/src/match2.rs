fn main() {
    let dice_roll = 9;
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        _other => re_roll()
    }
}

fn move_player(num_spaces: i8) {
    println!("Moving player {} spaces", num_spaces);  
}
fn add_fancy_hat() {
    println!("Adding fancy hat");
}
fn remove_fancy_hat() {
    println!("Removing fancy hat");
}
fn re_roll() {
    println!("Re-rolling");
}