import copy


def insertion_sort(A: list):
    A_ = copy.deepcopy(A)
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
    print(insertion_sort(A))
