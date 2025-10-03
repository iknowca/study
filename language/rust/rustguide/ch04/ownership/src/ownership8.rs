fn main() {
    let my_string = String::from("hello world");

    let word = first_word(&my_string);
    let word = first_word(&my_string[0..6]);

    let my_string_literal = "hello world";

}

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[0..]
}