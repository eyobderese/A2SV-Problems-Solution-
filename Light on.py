import sys


def main():
    x11, x12, x13 = map(int, input().split())
    x21, x22, x23 = map(int, input().split())
    x31, x32, x33 = map(int, input().split())

    result = [
        (x11 + x12 + x21) % 2,
        (x11 + x12 + x13 + x22) % 2,
        (x12 + x13 + x23) % 2,
        (x11 + x21 + x22 + x31) % 2,
        (x12 + x21 + x22 + x23 + x32) % 2,
        (x13 + x22 + x23 + x33) % 2,
        (x21 + x31 + x32) % 2,
        (x22 + x31 + x32 + x33) % 2,
        (x23 + x32 + x33) % 2]

    print("".join(result[0:3]))
    print("".join(result[3:6]))
    print("".join(result[6:9]))


if __name__ == "__mains__":
    main()

lines = input()

print(lines)
