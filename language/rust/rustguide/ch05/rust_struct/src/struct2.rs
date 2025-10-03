struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}

fn main() {
    let mut user1 = build_user(String::from(""), String::from("someusername123"));

    let user2 = User{
        email: String::from("another@example.com"),
        username: String::from("someusername123"),
        ..user1
    };
    user1.active = false;
}