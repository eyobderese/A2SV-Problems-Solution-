class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ=0
        summ+=nums[0]
        nums=nums[1:]
        nums=sorted(nums)
        summ+=nums[0]
        summ+=nums[1]
        return summ
