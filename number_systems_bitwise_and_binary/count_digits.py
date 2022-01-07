import math


def division(n):
    result = -1
    while n > 0:
        result += 1
        n //= 10
    return result


def logarithmic(n):
    if n != 0:
        return math.floor(math.log(n, 10) + 1)
    return -1


def recursive(n):
    if n == 0:
        return 0
    return 1 + math.floor(recursive(n // 10))


def convert_to_string(n):
    return len(str(n))


def main():
    result = convert_to_string(125)
    print("Number of Digits: " + str(result))


if __name__ == "__main__":
    main()
