from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = nums[0]
        i = 0
        j = 1
        minLength = 190015600

        while j < len(nums) or summ >= target:

            # print('sum: ', summ, '  minLength: ', minLength)
            if summ < target:
                summ += nums[j]
                j += 1
            else:

                minLength = min(minLength, j-i)
                summ -= nums[i]
                i += 1

        return minLength if minLength != 190015600 else 0
