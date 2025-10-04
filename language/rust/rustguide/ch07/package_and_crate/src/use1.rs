use std::collections::HashMap;
use std::collections;
fn main() {
    // this is reasonable
    let mut map = HashMap::new();
    map.insert(1, 2);

    // this is not reasonable
    let mut map = collections::HashMap::new();
}