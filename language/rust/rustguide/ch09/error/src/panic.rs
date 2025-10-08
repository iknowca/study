pub mod panic {
    pub fn f1() {
        println!("panic::f1");

        panic!("crash and burn");
    }
}
