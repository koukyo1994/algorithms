fn main() {
    let mut x: Vec<u32> = vec![5, 2, 4, 6, 1, 3];
    insertion_sort(&mut x);
    println!("{:?}", x);
}

fn insertion_sort(x: &mut [u32]) {
    for j in 1..x.len() {
        let key = x[j];
        let mut i = j - 1;
        while x[i] > key {
            x[i + 1] = x[i];
            if i == 0 {
                break;
            } else {
                i -= 1;
            }
        }
        x[i] = key
    }
}
