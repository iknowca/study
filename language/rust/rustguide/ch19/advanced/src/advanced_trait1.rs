pub struct Counter {
    count: u32,
    name: String,
}

pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}

impl Iterator for Counter {
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item> {
        Some(self.count+1)
    }
}

pub trait GenericIterator<T> {
    fn next(&mut self) -> Option<T>;
}

