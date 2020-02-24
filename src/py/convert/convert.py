def convert(n, base):
    result = ""
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result


if __name__ == "__main__":
    n = 18

    print(convert(n, 8))
