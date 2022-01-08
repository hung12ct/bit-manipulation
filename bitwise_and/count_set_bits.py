def basic_solution(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count


def brian_kernighan_algorithm(n):
    count = 0
    while n > 0:
        n &= n - 1
        count += 1
    return count


def lookup_table(n):
    table = [0]

    for i in range(1, 256):
        # i >> 1 equals to i/2
        table.append((i & 1) + table[i >> 1])
    count = 0
    for i in range(4):
        count += table[n & 0xFF]
        n >>= 8

    return count


def main():
    n = 125
    result = lookup_table(n)
    print(f"SetBit Count is {result}")


if __name__ == "__main__":
    main()
