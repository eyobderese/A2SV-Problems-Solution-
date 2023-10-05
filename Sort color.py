class Solution:
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]

        return nums
