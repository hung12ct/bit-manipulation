def min_flips(a, b, c):
    ans = 0
    for i in range(32):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1

        if bit_a | bit_b != bit_c:
            if bit_c == 0 and bit_a == 1 and bit_b == 1:
                ans += 2
            else:
                ans += 1
    return ans


def main():
    print(min_flips(2, 6, 5))


if __name__ == "__main__":
    main()
