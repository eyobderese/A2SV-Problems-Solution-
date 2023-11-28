def meeting(L):
    L = sorted(L)
    count = 1

    for i in range(len(L)-1):
        if L[i][1] > L[i+1][0]:
            count += 1

    return count


print(meeting([[7, 10], [2, 4]]))
