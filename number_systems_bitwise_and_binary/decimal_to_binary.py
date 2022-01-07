def stacks(n):
    result = []
    while n > 0:
        result.append(n % 2)
        # this is equivalent to (n = n >> 1) OR (n = n/2)
        n >>= 1
    result.reverse()
    return result


def main():
    n = 125
    result = stacks(n)
    print(f"Binary representaion of number: {n}, is {result}")


if __name__ == "__main__":
    main()
