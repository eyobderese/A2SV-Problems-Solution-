s, n = map(int, input().split())
arr = []
flag = True

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

for i in range(n):
    if s <= arr[i][0]:
        flag = False
        break
    s += arr[i][1]

if flag:
    print("YES")
else:
    print("NO")
