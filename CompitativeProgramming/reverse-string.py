class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s)%2==0:
            m=len(s)//2
            n=m-1

            while m<len(s):
                s[m],s[n]=s[n],s[m]
                m+=1
                n-=1
                

            
            
        else:
            m=len(s)//2
            n=m-1
            p=m+1

            while p<len(s):
                s[n],s[p]=s[p],s[n]
                n-=1
                p+=1
        
             