firstArray = list(map(int, input().split()))

m=firstArray[0]
n=firstArray[1]
isright=False
for i in range(m):
    
    for j in range(n):
       
        if i%2==0:
            print('#', end="")
        elif isright and j==n-1:
            print('#', end="")
           
        elif (not isright) and j==0:
            print('#', end="")
            

        
        else:
            print('.', end="")
    if i%2==0:
        isright=not(isright)

            
    print()
