def hamming_distance(a, b):
    xor = a ^ b
    ans = 0
    while xor != 0:
        ans += 1
        xor &= xor - 1
    return ans


def main():
    print(hamming_distance(1, 8))


if __name__ == "__main__":
    main()
