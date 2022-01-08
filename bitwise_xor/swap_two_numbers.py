def solution(a, b):
    a = a ^ b
    b = b ^ a
    a = a ^ b

    print(f"Finally, after swapping: a = {a} , b = {b}")


def main():
    solution(-6, 10)


if __name__ == "__main__":
    main()
