firstArray = list(map(int, input().split()))
secondArray=list(map(int, input().split()))

target=firstArray[1]

summ=0
l=0
shortestSigment=float('inf')

for i in range (len(secondArray)):
    summ+=secondArray[i]

    while summ>=target:
        shortestSigment=min(shortestSigment,i-l+1)
        summ-=secondArray[l]
        l+=1
print(-1) if sum(secondArray)<target else print(shortestSigment)




