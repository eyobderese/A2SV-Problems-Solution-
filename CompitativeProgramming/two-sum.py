class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            
            searching_number = target-nums[i]
            if (searching_number in nums and i !=nums.index(searching_number) ):
                return [i,nums.index(searching_number)]