def solution(nums):
    if nums == 0:
        return 0
    ans = 0
    while nums & (1 << ans) == 0:
        ans += 1
    return ans + 1


def main():
    nums = 32
    print(solution(nums))


if __name__ == "__main__":
    main()
