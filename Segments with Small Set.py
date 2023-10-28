from collections import Counter


firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))

k = firstArray[1]


def sigmentWithTwo(arry, k):
    l = 0
    summ = 0
    ans = 0
    for i in range(len(arry)):
        summ += arry[i]

        while len(Counter(arry[l:i+1])) > k:
            summ -= arry[l]
            l += 1
        summ = max(summ, ans)

    print(summ)


# arry = [2, 6, 4, 3, 6, 8, 3] out 20

sigmentWithTwo(secondArray, k)
