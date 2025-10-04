use std::fmt;
use std::io;
use std::io::Result as IoResult;
// When multiple modules have functions with the same name,
// you must specify the module name to clarify which one to use.
// Or use 'as' to rename the function.
fn main() {

}

fn func1() -> fmt::Result {

}

fn func2() -> io::Result<()> {
}

fn func3() ->  IoResult<()>{
}