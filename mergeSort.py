unNessesary=input()
firstArray = list(map(int, input().split()))
secondArray=list(map(int, input().split()))


i=0
j=0

mergedArray=[]

while i<len(firstArray) and j<len(secondArray):
    if firstArray[i]<secondArray[j]:
        mergedArray.append(firstArray[i])
        i+=1
    else:
        mergedArray.append(secondArray[j])
        j+=1
while i<len(firstArray):
    mergedArray.append(firstArray[i])
    i+=1  
while j<len(secondArray):
    mergedArray.append(secondArray[j])
    j+=1
mergedArray=list(map(str,mergedArray))
mergedArray=" ".join(mergedArray)
print(mergedArray)
