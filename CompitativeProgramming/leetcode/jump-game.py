class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        need=0

        j=len(nums)-1

        while j>=0:
            if nums[j]>=need:
                need=1
            else:
                need+=1
            j-=1
        if need>1:
            return False
        return True
