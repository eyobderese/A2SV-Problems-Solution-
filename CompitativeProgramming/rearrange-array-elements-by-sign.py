class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        nagative=[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                nagative.append(i)
        ans=[]
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(nagative[i])
        return ans
  
        