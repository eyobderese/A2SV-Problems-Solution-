class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(list(set(nums)), reverse=True)
        print(nums)
        if len(nums)>2:
            return nums[2]
        else:
            return max(nums)
        