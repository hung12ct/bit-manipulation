def solution(n, k):
    return (n >> (k - 1) & 1) != 0


def main():
    print(solution(5, 3))
    print(solution(10, 2))
    print(solution(10, 1))


if __name__ == "__main__":
    main()
