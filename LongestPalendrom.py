def longestPalindrome( s):
    m=''
    for i in range(1,len(s)):
        j=i-1
        k=i+1

        while j>0 and k<len(s):
          
            if s[j]==s[k]: 
                if k-j+1>len(m):
                    m=s[j:k+1]
                else:
                    j-=1
                    k+=1
            else: break
    return m
  
print(longestPalindrome("babad"))