from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = []
        k = 0

        for i in range(len(nums)):
            if not nums[i] in m:
                m.append(nums[i])
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return len(m)
