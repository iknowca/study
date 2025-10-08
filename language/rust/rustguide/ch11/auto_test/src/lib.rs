#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2+2, 4);
    }

    // #[test]
    // fn another() {
    //     panic!("Make this test fail");
    // }

    use super::*;
    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle { width: 8, height: 7 };
        let smaller = Rectangle { width: 5, height: 1 };
        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle { width: 8, height: 7 };
        let smaller = Rectangle { width: 5, height: 1 };
        assert!(!smaller.can_hold(&larger));
    }
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 {
            panic!("Guess value must be greater than or equal to 1, got {}.", value);
        } else if value > 100 {
            panic!("Guess value must be less than or equal to 100, got {}.", value);
        }
        Guess { value }
    }
}

#[cfg(test)]
mod tests_guess {
    use super::Guess;
    #[test]
    #[should_panic(expected = "less")]
    fn greater_than_100() {
        Guess::new(101);
    }

    #[test]
    #[should_panic(expected = "greater")]
    fn less_than_1() {
        Guess::new(0);
    }
}

#[cfg(test)]
mod test_result {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err("2 + 2 != 4".to_string())
        }
    }
}