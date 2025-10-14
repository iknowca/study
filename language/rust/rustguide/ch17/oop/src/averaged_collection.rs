pub struct AveragedCollection {
    list: Vec<f64>,
    average: f64,
}

impl AveragedCollection {
    pub fn add(&mut self, value: f64) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<f64> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    fn update_average(&mut self) {
        let total: f64 = self.list.iter().sum();
        self.average = total / self.list.len() as f64;
    }
}