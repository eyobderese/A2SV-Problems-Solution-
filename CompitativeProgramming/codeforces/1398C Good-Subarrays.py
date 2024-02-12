from collections import defaultdict


for i in range(int(input())):
    n = int(input())
    s = input()
    arry = list(map(int, list(s)))

    j = 0
    count = 0
    pre = [arry[0]]
    for i in range(1, len(arry)):
        pre.append(pre[i-1]+arry[i])

    tracker = defaultdict(int)
    tracker[1] = 1

    for i in range(len(pre)):
        if pre[i]-i in tracker:
            count += tracker[pre[i]-i]
        tracker[pre[i]-i] += 1
    print(count)
