def goodArray(a):
    if len(a) < 2:
        print('NO')
        return
    m = []
    for i in a:
        if i > 1:
            m.append(1)
        elif i == 1:
            m.append(2)
    if sum(a) >= sum(m):
        print('YES')

    else:
        print("No")


z = int(input())
while z > 0:
    n = input()
    m = list(map(int, input().split()))
    goodArray(m)
    z -= 1
