def solution(n):
    if n == 0:
        return 0
    ans = 0
    while n & (1 << ans) == 0:
        ans += 1
    return ans + 1


def main():
    print(solution(32))


if __name__ == "__main__":
    main()
