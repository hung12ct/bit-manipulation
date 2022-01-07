def bit_shifting(n):
    count = 0
    while 1 << count <= n:
        count += 1
    return count


def main():
    n = 125
    result = bit_shifting(n)
    print(f"Number of bits: {n}, is {result}")


if __name__ == "__main__":
    main()
