def is_even(nums):
    ans = []
    for n in nums:
        if n & 1:
            ans.append("Odd")
        else:
            ans.append("Even")
    return ans


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = is_even(nums)
    print(f"Result {result}")


if __name__ == "__main__":
    main()
