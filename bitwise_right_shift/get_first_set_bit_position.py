def solution(num):
    if num == 0:
        return 0
    ans = 0
    while (num >> ans) & 1 == 0:
        ans += 1
    return ans + 1


def main():
    num = 32
    print(solution(num))


if __name__ == "__main__":
    main()
