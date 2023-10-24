unNessesary=input()
firstArray = list(map(int, input().split()))
secondArray=list(map(int, input().split()))


i=0
j=0

answerArray=[0]*len(secondArray)

while j<len(secondArray) and i<len(firstArray):
    if secondArray[j]>firstArray[i]:
        i+=1
    else:
        answerArray[j]=i
        j+=1
while j<len(secondArray):
    answerArray[j]=i
    j+=1






answerArray=list(map(str,answerArray))
answerArray=" ".join(answerArray)
print(answerArray)

