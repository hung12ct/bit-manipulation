def solution(nums):
    ans = nums[0]
    for i, n in enumerate(nums):
        ans ^= i ^ n
    return ans


def main():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(solution(nums))


if __name__ == "__main__":
    main()
