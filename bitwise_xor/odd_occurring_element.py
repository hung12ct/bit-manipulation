def solution(nums):
    ans = 0
    for n in nums:
        ans ^= n
    return ans


def main():
    nums = [4, 3, 3, 4, 4, 4, 5, 3, 5]
    print(solution(nums))


if __name__ == "__main__":
    main()
