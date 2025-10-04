pub mod hash_map {
    use std::collections::HashMap;

    pub fn f1() {
        println!("hash_map::f1");

        let mut scores = HashMap::new();
        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Yellow"), 50);
    }

    pub fn f2() {
        println!("hash_map::f2");

        let mut scores = HashMap::new();
        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Yellow"), 50);

        let team_name = String::from("Blue");
        let score = scores.get(&team_name).copied().unwrap_or(0);
        println!("score: {:?}", score);
    }

    pub fn f3() {
        println!("hash_map::f3");

        let field_name = String::from("Favorite color");
        let field_value = String::from("Blue");

        let mut map = HashMap::new();
        map.insert(field_name, field_value);

        println!("map: {:?}", map);
        // error: field_name is not valid
        // println!("field_name: {:?}", field_name)
    }

    pub fn f4() {
        println!("hash_map::f4");

        let mut scores = HashMap::new();
        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Yellow"), 50);

        scores.entry(String::from("Red")).or_insert(0);
        scores.entry(String::from("Blue")).or_insert(0);

        println!("scores: {:?}", scores);
    }

    pub fn f5() {
        println!("hash_map::f5");

        let text = "hello world wonderfule world";

        let mut map = HashMap::new();
        for word in text.split_whitespace() {
            let count = map.entry(word).or_insert(0);
            *count += 1;
        }
        println!("map: {:?}", map);
    }
}