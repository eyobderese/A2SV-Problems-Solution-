def solve():
    n, k, d, w = map(int, input().split())

    t = list(map(int, input().split()))
    when = -1
    cnt = 0
    ans = 0

    for i in range(n):
        if t[i] <= when + d and cnt > 0:
            cnt -= 1
        else:
            when = t[i] + w
            cnt = k - 1
            ans += 1

    print(ans)


testCase = int(input())
for _ in range(testCase):
    solve()
