fn c2f(c: f32) -> f32 {
    c * 9.0 / 5.0 + 32.0
}

fn f2c(f: f32) -> f32 {
    (f - 32.0) * 5.0 / 9.0
}

fn main() {
    println!("섭씨 100도는 화씨 {}", c2f(100f32).to_string());
    println!("섭씨 0도는 화씨 {}", c2f(0f32).to_string());
    println!("화씨 100도는 섭씨 {}", f2c(100f32).to_string());
    println!("화씨 0도는 섭씨 {}", f2c(0f32).to_string());
}