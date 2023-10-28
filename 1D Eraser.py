z = int(input())
while z > 0:
    n, k = map(int, input().split())
    s = input()
    count = 0
    i = 0
    while i < n:
        if s[i] == 'B':
            count += 1
            i += k - 1
        i += 1
    print(count)
    z -= 1
