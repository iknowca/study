enum Color {
    Rgb( i32, i32, i32),
    Hsv( i32, i32, i32),
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(Color),
}

fn main() {
    let msg = Message::ChangeColor(Color::Rgb(255, 0, 0));

    match msg {
        Message::ChangeColor(Color::Rgb(r, g, b)) => println!("The color is red, green, and blue: {}, {}, {}", r, g, b),
        Message::ChangeColor(Color::Hsv(h, s, v)) => println!("The color is hue, saturation, and value: {}, {}, {}", h, s, v),
        _ => (),
    }
}