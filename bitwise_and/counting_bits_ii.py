def counting_bits(n):
    ans = [0]
    for i in range(1, n + 1):
        ans.append((i & 1) + ans[i >> 1])
    return ans


def main():
    n = 6
    result = counting_bits(n)
    print(f"Result {result}")


if __name__ == "__main__":
    main()
