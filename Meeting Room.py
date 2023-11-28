def meeting(L):
    L = sorted(L)

    for i in range(len(L)-1):
        if L[i][1] > L[i+1][0]:
            return False
    return True


print(meeting([[7, 10], [2, 4]]))
