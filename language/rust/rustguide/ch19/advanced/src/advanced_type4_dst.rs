fn main() {
    // let s1: str = "";
    let s1:&str = "";
}

fn generic<T>(t: T) {

}

fn generic2<T: Sized>(t: &T) {

}

fn generic3<T: ?Sized>(t: &T) {
    
}