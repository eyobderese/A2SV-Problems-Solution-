class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        store=[]
        i=0
        n=len(nums)

        def helper(nums,curr,i):
            nonlocal store
            if i>=n:
                return
            
            for j in range (i,len(nums)):
                curr.append(nums[j])
                store.append(tuple(sorted(curr[:])))
                helper(nums,curr,j+1)
                curr.pop()
        helper(nums,[],0)
        store=list(set(store))
        store.append([])
        
        return store

        