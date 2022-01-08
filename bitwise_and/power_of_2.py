def is_power_of_2(n):
    if n == 0:
        return False
    while n > 1:
        if n & 1:
            return False
        n >>= 1
    return True


def brian_kernighan_algorithm(n):
    return n > 0 and (n & (n - 1) == 0)


def main():
    print(brian_kernighan_algorithm(6))
    print(brian_kernighan_algorithm(8))


if __name__ == "__main__":
    main()
