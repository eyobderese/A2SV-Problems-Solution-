class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]

        runningSum=0
        for i in range(len(nums)):
            runningSum+=nums[i]
            val=ceil(runningSum/(i+1))
            ans=max(ans,val)
        return int(ans)

        