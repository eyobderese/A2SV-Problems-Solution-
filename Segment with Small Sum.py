firstArray = list(map(int, input().split()))
secondArray=list(map(int, input().split()))

target=firstArray[1]

summ=0
l=0

longestSigment=0

for i in range(len(secondArray)):
    summ+=secondArray[i]
    while summ>target:
        summ-=secondArray[l]
        l+=1
    longestSigment=max(longestSigment,i-l+1)

print(longestSigment)
    
