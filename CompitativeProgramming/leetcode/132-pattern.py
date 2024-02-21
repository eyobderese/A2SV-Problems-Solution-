class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        minn=nums[0]
        stack=[(nums[0],minn)]

        for i in nums[1:]:
            flag=True            
            minn=min(minn,stack[-1][0])
            while stack and stack[-1][0]<=i:
                stack.pop()
            if stack and stack[-1][0]>i and i>stack[-1][1] :
                return True
            stack.append((i,minn))
            
        return False
            









        