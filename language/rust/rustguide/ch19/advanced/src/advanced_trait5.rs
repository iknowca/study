trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("Poppy")
    }
}

fn main() {
    println!("Dog's baby name: {}", <Dog as Animal>::baby_name());
}