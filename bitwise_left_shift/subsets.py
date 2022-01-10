def solution(nums):
    result = []
    pow_size = 2 ** len(nums)
    for i in range(pow_size):
        val = []
        for j, ele in enumerate(nums):
            if i & (1 << j) != 0:
                val.append(ele)
        result.append(val)
    return result


def main():
    nums = [1, 2, 3, 4]
    print(solution(nums))


if __name__ == "__main__":
    main()
