class Solution:
    def smallerNumbersThanCurrent(self, nums):
        myCounter = []
        for i in range(len(nums)):
            count = 0
            for j in nums:
                if j < nums[i]:
                    count += 1
            myCounter.append(count)
        return myCounter
