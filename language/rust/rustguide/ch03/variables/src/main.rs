mod array;
mod function;
mod branches;
mod loop1;
mod loop2;
mod while1;
mod while2;
mod for1;
mod temp_converter;
mod fibo;

fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    let x = x + 1;
    println!("The value of x is: {x}");
    {
        let x = 7;
        println!("The value of x is: {x}");
    }
    println!("The value of x is: {x}");
}
