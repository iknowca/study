#[derive(Debug)]
enum Message {
    Hello { id: i32 },
}

fn main() {
    let msg = Message::Hello { id: 11 };

    match msg {
        Message::Hello {
            id: id_var @ 3..=7,
        } => println!("Found an id in range: {}", id_var),
        Message::Hello {
            id: 10 | 11,
        } => {
            println!("Found an id: {:?}", msg);
            println!("Found a 10 or 11");
        },
        Message::Hello { id } => {
            println!("Found some other id: {}", id);
        }
    }
}