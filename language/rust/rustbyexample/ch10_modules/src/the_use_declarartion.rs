fn function() {
    println!("called `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("called `deeply::nested::function()`");
        }
    }
}

fn main() {
    function();
    deeply::nested::function();
    {
        use deeply::nested::function;
        function();
        println!("Leaving block");
    }
}