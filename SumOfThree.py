testCase=int(input())

while testCase:
    n=int(input())
    

    isFinished=False

    for i in range(1,n+1):
        if i%3==0:
            continue
        if isFinished:
            break
        
        j=0
        k=n
        while j<k:
            if j==i or j%3==0 or j + i + k<n:
                j+=1
            elif k==i or k%3==0 or j + i + k>n:
                i
                k-=1
            elif j + i + k==n:
                print("Yes")
                print( j, i ,k)
                isFinished=True
                break
    if not isFinished:
        print('NO')
    testCase-=1

        
    

