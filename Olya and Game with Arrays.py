import sys


def solve():
    n, mn2, mn1 = int(input()), sys.maxsize, sys.maxsize
    v = []
    for _ in range(n):
        m = int(input())
        temp = list(map(int, input().split()))
        temp.sort()
        v.append(temp)
    for i in range(n):
        mn2 = min(v[i][1], mn2)
        mn1 = min(v[i][0], mn1)
    ans, count = 0, 0
    for i in range(n):
        if v[i][1] == mn2 and count == 0:
            count += 1
        else:
            ans += v[i][1]
    ans += mn1
    print(ans)


if __name__ == "__main__":

    t = int(input())
    for _ in range(t):
        solve()
