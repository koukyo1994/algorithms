# Sort Algorithms

## Insertion sort

挿入ソートと呼ばれるソート

* データ数が小さい時に高速なソート法
* 元の配列を書き換える形でソートする

```python
import copy


def insertion_sort(A: list, inplace: bool = False):
    A_ = copy.deepcopy(A)
    if inplace:
        A_ = A
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A_[i] > key:
            A_[i + 1] = A_[i]
            i -= 1
        A_[i + 1] = key
    return A_


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(A))  # => [1, 2, 3, 4, 5, 6]
    print(A)  # => [5, 2, 4, 6, 1, 3]

    print(insertion_sort(A, inplace=True))  # => [1, 2, 3, 4, 5, 6]
    print(A)  # => [1, 2, 3, 4, 5, 6]
```
