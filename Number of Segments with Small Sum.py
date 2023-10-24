firstArray = list(map(int, input().split()))
secondArray=list(map(int, input().split()))

target=firstArray[1]

summ=0
l=0
answer=0

for i in range(len(secondArray)):
    summ+=secondArray[i]


    while summ>target:
        summ-=secondArray[l]
        l+=1
    answer=max(summ,answer)

    
    
print(answer)
