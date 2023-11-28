# 9 6 8 4 5 2
# 4 1 5 6 3 1


def counting():
    MOOD = pow(10, 9)+7
    ans = 1
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    for i in range(len(a)):
        if a[i] < b[i]:
            print(0)
            break

    j = 0
    for i in range(len(a)):
        while j < len(b) and b[j] < a[i]:
            j += 1
        ans *= (j-i)
        ans = ans % MOOD
    print(ans)


for i in range(int(input())):
    counting()
