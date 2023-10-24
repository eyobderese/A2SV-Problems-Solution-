n = int(input())
a = list(map(int, input().split()))
cs = [0] * n

for i in range(n):
    cs[i] -= 1
    cs[max(0, i - a[i])] += 1

for i in range(1, n):
    cs[i] += cs[i-1]

cnt = sum(1 for i in range(n) if cs[i] == 0)

print(cnt)
