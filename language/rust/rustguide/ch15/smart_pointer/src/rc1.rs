use std::rc::Rc;
enum List {
    Cons(i32, Box<List>),
    Nil,
}

enum RcList {
    Cons(i32, Rc<RcList>),
    Nil
}

fn main() {
    let a = List::Cons(5, Box::new(List::Cons(10, Box::new(List::Nil))));
    let b = List::Cons(3, Box::new(a));
    // let c = Cons(4, Box::new(b));

    let a = Rc::new(RcList::Cons(5, Rc::new(RcList::Cons(10, Rc::new(RcList::Nil)))));
    {
        println!("count after creating a: {}", Rc::strong_count(&a));
        let b = RcList::Cons(3, Rc::clone(&a));
        println!("count after creating b: {}", Rc::strong_count(&a));
        let c = RcList::Cons(4, Rc::clone(&a));
        println!("count after creating c: {}", Rc::strong_count(&a));
    }
    println!("count after a goes out of scope: {}", Rc::strong_count(&a));
}