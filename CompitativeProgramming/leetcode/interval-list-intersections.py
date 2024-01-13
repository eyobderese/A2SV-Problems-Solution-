class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:


        i=0
        j=0

        ans=[]

        while i<len(firstList) and j<len(secondList):

            print(firstList[i],secondList[j])
            n=max(firstList[i][0],secondList[j][0])
            m=min(firstList[i][1],secondList[j][1])
            if n<=m:
                ans.append([n,m])

            if firstList[i][1]>secondList[j][1]:
                j+=1
            else:
                i+=1
        return ans