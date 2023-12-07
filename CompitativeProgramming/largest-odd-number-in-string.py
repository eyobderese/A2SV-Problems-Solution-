class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=''
        n=len(num)
        
        
        for i in range(1,n+1):
            if int(num[-i])%2!=0:
                return num[0:n-i+1]
        return ""
    