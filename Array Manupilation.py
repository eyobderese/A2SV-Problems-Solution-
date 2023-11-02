def arrayManipulation(n, queries):
    # Write your code here
    pre=[0]*(n+2)
    for a,b,k in queries:
        pre[a]+=k
        
        pre[b+1]-=k
    total=0
    maxx=0
    
    for i in pre:
        total+=i
        maxx=max(total, maxx)
    return maxx