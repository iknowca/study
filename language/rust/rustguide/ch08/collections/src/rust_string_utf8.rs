pub mod utf8 {
    pub fn f1() {
        let mut s = String::new();
        println!("s: {}", s);
    }

    pub fn f2() {
        let data = "initial contents";
        println!("data: {}", data);
        let s = data.to_string();
        println!("s: {}", s);
        let s = "initial contents".to_string();
        println!("s: {}", s);
        let s = String::from("initial contents");
        println!("s: {}", s);

        let ss = s.as_str();
        println!("ss: {}", ss);
    }

    pub fn f3() {
        println!("f3");
        let mut s = String::from("foo");
        println!("s: {}", s);
        s.push_str("bar");
        println!("s: {}", s);
    }

    pub fn f4() {
        println!("f4");

        let s1 = String::from("tic");
        let s2 = String::from("tac");
        let s3 = String::from("toe");
        let mut s = format!("{}-{}-{}", s1, s2, s3);
        println!("s: {}", s);
        s.push_str("-");
        println!("s: {}", s);
    }
}