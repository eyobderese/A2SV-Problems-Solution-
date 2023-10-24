

def ans(x, y, n):
    x = min(x, n - x + 1)
    y = min(y, n - y + 1)
    return min(x, y)


def solve():
    n, x1, y1, x2, y2 = map(int, input().split())
    print(abs(ans(x1, y1, n) - ans(x2, y2, n)))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
