class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:


        ans=[]
        temp=[]

        def helper(index,temp):
            nonlocal ans 

            if len(temp)==k and sum(temp)==n:
                ans.append(tuple(sorted(temp)))
                return 
            if len(temp)>k:
                return 
            if sum(temp)>n:
                return 
            
            for i in range(index,10):
                temp.append(i)
                helper(i+1,temp)
                temp.pop()
        helper(1,temp)
        return ans 
        