def main():
    x11, x12, x13, x21, x22, x23, x31, x32, x33 = map(int, input().split())

    result = [
        (x11 + x12 + x21) % 2,
        (x11 + x12 + x13 + x22) % 2,
        (x12 + x13 + x23) % 2,
        (x11 + x21 + x22 + x31) % 2,
        (x12 + x21 + x22 + x23 + x32) % 2,
        (x13 + x22 + x23 + x33) % 2,
        (x21 + x31 + x32) % 2,
        (x22 + x31 + x32 + x33) % 2,
        (x23 + x32 + x33) % 2
    ]

    for i in range(0, 9, 3):
        print("".join(map(str, result[i:i+3])))


if __name__ == "__main__":
    main()
