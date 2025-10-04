use package_and_crate;
use package_and_crate::external_lib::Rng;
fn main() {
    package_and_crate::eat_at_restaurant();
    package_and_crate::eat_at_restaurant2();
    package_and_crate::eat_at_restaurant3();
    let secret_number = rand::thread_rng().gen_range(1..=100);
    println!("The secret number is: {}", secret_number);
}