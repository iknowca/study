use crates::art::kinds::PrimaryColor;
use crates::art::utils::mix;
fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}
