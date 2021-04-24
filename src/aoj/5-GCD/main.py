def factorize(N: int):
    i = 2
    n = N
    ans = {}
    while i ** 2 <= N:
        while n % i == 0:
            n = n // i
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        i += 1
    if n != 1:
        ans[n] = 1
    return ans


def gcd(factor_a: dict, factor_b: dict):
    val = 1
    keys_a = set(list(factor_a.keys()))
    keys_b = set(list(factor_b.keys()))
    intersection = keys_a.intersection(keys_b)
    for key in intersection:
        power = min(factor_a[key], factor_b[key])
        val *= key ** power
    return val


def lcm(factor_a: dict, factor_b: dict):
    val = 1
    keys_a = set(list(factor_a.keys()))
    keys_b = set(list(factor_b.keys()))
    union = keys_a.union(keys_b)
    for key in union:
        if factor_a.get(key) is not None and factor_b.get(key) is not None:
            power = max(factor_a[key], factor_b[key])
            val *= key ** power
        elif factor_a.get(key) is not None:
            power = factor_a[key]
            val *= key ** power
        else:
            power = factor_b[key]
            val *= key ** power
    return val


if __name__ == '__main__':
    while True:
        try:
            a, b = list(map(int, input().split()))
        except EOFError:
            import sys
            sys.exit(0)
        factor_a = factorize(a)
        factor_b = factorize(b)

        gcd_val = gcd(factor_a, factor_b)
        lcm_val = lcm(factor_a, factor_b)
        print(f"{gcd_val} {lcm_val}")
