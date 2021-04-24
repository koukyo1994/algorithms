import numpy as np

"""
def count_primes_lower_than(N: int):
    is_prime = np.ones(N - 1, dtype=bool)
    is_prime[0] = False
    cursor = 1
    while (cursor + 1) ** 2 <= N:
        if not is_prime[cursor]:
            cursor += 1
            continue
"""



def count_primes_lower_than(N: int):
    A = list(range(2, N + 1))
    p = []
    while A[0] ** 2 <= N:
        tmp = A[0]
        p.append(tmp)
        A = [e for e in A if e % tmp != 0]
    return len(p + A)


if __name__ == '__main__':
    while True:
        try:
            a = int(input())
        except EOFError:
            import sys
            sys.exit(0)
        if a == 1:
            print(0)
        else:
            print(count_primes_lower_than(a))
