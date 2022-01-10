def solution(n):
    if n == 0:
        return 0
    ans = 1
    while 1:
        if n & (1 << (ans - 1)) == 0:
            ans += 1
        else:
            break
    return ans


def main():
    print(solution(32))


if __name__ == "__main__":
    main()
