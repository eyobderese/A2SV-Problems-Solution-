class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        N=len(nums)
        ans=0

        for k in range(2,N):
            i=0
            j=k-1
            while j>i:
                if nums[i]+nums[j]>nums[k]:
                    ans+=j-i
                    j-=1
                else:
                    i+=1
        return ans 


        