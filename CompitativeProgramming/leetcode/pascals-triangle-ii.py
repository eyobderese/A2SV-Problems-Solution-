class Solution:
    ans=[1]
    def getRow(self, rowIndex: int,ans=ans) -> List[int]:
        ans=[1]
        for i in range(rowIndex):
            newRow=[0]*(len(ans)+1)
            for j in range(len(ans)):
                newRow[j]+=ans[j]
                newRow[j+1]+=ans[j]
            ans=newRow
        return ans
                


    

        return ans
           
        

       
        

        