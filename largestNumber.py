class Solution:
    def largestNumber(self, nums):
        largest = ''

        for i in range(len(nums)):
            for h in range(len(nums)):
                if str(nums[h])+str(nums[i]) > str(nums[i])+str(nums[h]):
                    nums[h], nums[i] = nums[i], nums[h]

        for i in range(len(nums)):
            num1 = largest + str(nums[i])
            num2 = str(nums[i]) + largest
            if int(num1) > int(num2):
                largest = num1
            else:
                largest = num2

        return str(int(largest))
