class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxx='000'
        flag=False
        for i in range(len(num)-2):
            if len(set(num[i:i+3]))==1:
                maxx=max(maxx,num[i:i+3])
                flag=True
        return maxx if flag else ""




       


        