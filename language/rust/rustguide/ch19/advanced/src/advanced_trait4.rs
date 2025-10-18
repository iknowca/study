trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("Pilot: I'm flying!");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Wizard: I'm flying!");
    }
}

impl Human {
    fn fly(&self) {
        println!("Human: I'm flying!");
    }
}

fn main() {
    let human = Human;
    human.fly();
    Wizard::fly(&human);
    Pilot::fly(&human);
}