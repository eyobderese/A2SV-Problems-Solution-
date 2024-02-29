class Solution:
    def longestNiceSubstring(self, s: str) -> str:

     
        def helper(s):
            
            tracker=set(list(s))        
            if len(s)<2:
                return ""
            flag=True
            for i in range(len(s)):
                if s[i].lower() not in tracker or s[i].upper() not in tracker:
                    flag=False
                    val1=helper(s[:i])
                    val2=helper(s[i+1:])
                    return val1 if len(val1)>=len(val2) else val2
            return s 

        return helper(s)
        out=""
        for i in ans:
            if len(out)<len(i):
                out=i      
        return out
        
                 


        
        
        

    



