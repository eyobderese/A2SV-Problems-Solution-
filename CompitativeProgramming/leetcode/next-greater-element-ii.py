class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[] #(index,val)
        tracker={}
        N=len(nums)

        nums=nums+nums
        ans=[]
        for i in range(len(nums)):
            while stack and stack[-1][1]<nums[i]:
                index,val=stack.pop()
                tracker[index]=nums[i]
            
            stack.append((i,nums[i]))
        ans=[-1]*N
        for i in range(N):
            if i in tracker:
                ans[i]=tracker[i]
        return ans


            
            
            
            
            
            



        