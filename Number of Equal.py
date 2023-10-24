from collections import Counter

unNessesary=input()
firstArray = list(map(int, input().split()))
secondArray=list(map(int, input().split()))



x=Counter(firstArray)
y=Counter(secondArray)
answer=0

for i in x:
    if i in y:
        answer= answer+ (x[i]* y[i])



print(answer)