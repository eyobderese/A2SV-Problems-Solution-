class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''
        if len(s)<k:
            return s[::-1]
        else:
            for i in range(0, len(s),2*k):
                if len(s)>i+2*k:
                    ans+=s[i:i+k][::-1]+s[i+k:i+2*k]
                elif i+k>len(s): 
                    ans+=s[i:][::-1]
                else:
                    ans+=s[i:i+k][::-1]+s[i+k:]
            return ans


        