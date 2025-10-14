use gui::{Button, Draw, Screen};

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        println!("SelectBox");
    }
}

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec! [
                    String::from("Option 1"),
                    String::from("Option 2"),
                    String::from("Option 3"),
                ]
            }),
            Box::new(Button {
                width: 100,
                height: 50,
                label: String::from("OK"),
            }),
        ]
    };

    screen.run();
}