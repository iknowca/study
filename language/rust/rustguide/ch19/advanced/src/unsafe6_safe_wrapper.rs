use std::slice;

// This function doesn't compile: can't create two mutable references from the same slice.
// fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
//     let len = values.len();
//     assert!(mid<=len);
//
//     (&mut values[..mid], &mut values[mid..])
// }

fn split_at_mut2(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = values.len();
    let ptr = values.as_mut_ptr();
    assert!(mid<=len);

    unsafe {
        (
            slice::from_raw_parts_mut(ptr, mid),
            slice::from_raw_parts_mut(ptr.add(mid), len-mid),
        )
    }
}

fn main() {
    let mut v = vec![1, 2, 3, 4, 5];
    let (a, b) = split_at_mut2(&mut v, 3);
    println!("a = {:?}", a);
    println!("b = {:?}", b);

    let address = 0x01234usize;
    let r = address as *mut i32;
    let values: &[i32] = unsafe { slice::from_raw_parts(r, 10) };
    println!("{:?}", values);
}