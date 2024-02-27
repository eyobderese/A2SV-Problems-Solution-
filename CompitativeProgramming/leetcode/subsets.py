class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        store=[]
        i=0
        n=len(nums)

        def helper(nums,curr,i):
            nonlocal store
            if i>=n:
                return
            
            for j in range (i,len(nums)):
                curr.append(nums[j])
                store.append(curr[:])
                helper(nums,curr,j+1)
                curr.pop()
        helper(nums,[],0)
        store.append([])
        return store





        