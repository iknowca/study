use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf:&[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;
    
    fn write_all(&mut self, buf:&[u8]) -> Result<(), Error>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<(), Error>;
}

type Reuslt<T> = std::result::Result<T, Error>;
pub trait Write2 {
    fn write(&mut self, buf:&[u8]) -> Reuslt<usize>;
    fn flush(&mut self) -> Reuslt<()>;
    
    fn write_all(&mut self, buf:&[u8]) -> Reuslt<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Reuslt<()>;
}