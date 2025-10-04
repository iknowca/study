mod rust_string_utf8;
mod hash_map;

fn main() {
    println!("Hello, world!");

    let v: Vec<i32> = Vec::new();
    let v = vec![1, 2, 3];

    let mut v = Vec::new();
    v.push(5);
    v.push(6);
    v.push(7);

    let v = vec![1, 2, 3, 4, 5];
    let third: &i32 = &v[2];
    println!("The third element is {}", third);

    // let seventh: &i32 = &v[6];
    // println!("The seventh element is {}", seventh);
    // error: seventh element is not valid

    let third: Option<&i32> = v.get(7);
    match third {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element."),
    }

    let mut v = vec![1, 2, 3, 4, 5];
    let first = &v[0];
    println!("first: {}, ", first);
    v.push(6);
    println!("first: {:#?}, ", v);

    let v = vec![100, 32, 57];
    for i in &v {
        println!("{i}");
    }

    let mut v= vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
    }
    println!("v: {:?}", v);

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Int(5),
    ];

    rust_string_utf8::utf8::f1();
    rust_string_utf8::utf8::f2();
    rust_string_utf8::utf8::f3();

    hash_map::hash_map::f1();
    hash_map::hash_map::f2();
    hash_map::hash_map::f3();
    hash_map::hash_map::f4();
    hash_map::hash_map::f5();
    println!("end of main");
}

enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}