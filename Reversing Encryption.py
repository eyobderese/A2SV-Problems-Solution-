s='rocesfedoc'


n=len(s)
j=1

while j<=n:
    print(s)
    if n%j==0:
        right=s[j:]
        left=s[:j][::-1]
        s=left+right
        j+=1
    else:
        j+=1
print(s)
    
# m='codeforce'
# print(m[:len(m)][::-1])