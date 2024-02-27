class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        store=[]
        n=len(nums)
        tracker=set()
        def helper(nums,currNums):
            nonlocal store
            if len(currNums)==n:
                store.append(currNums[:])
                return
            
            for i in nums:
                if i not in tracker:
                    currNums.append(i)
                    tracker.add(i)
                    helper(nums,currNums)
                    m=currNums.pop()
                    tracker.discard(m)
        helper(nums,[])
        return store
            


        