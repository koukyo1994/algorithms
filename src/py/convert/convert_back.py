if __name__ == "__main__":
    n = "10010"

    result = 0
    for i in range(len(n)):
        result += (2**(len(n) - i - 1)) * int(n[i])

    print(result)
