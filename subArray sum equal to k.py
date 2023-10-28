from ast import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 0
        count = defaultdict(int)
        count[0] = 1

        for i in nums:

            total += i
            preSum = total-k

            if preSum in count:
                ans += count[preSum]
                count[total] += 1
            else:
                count[total] += 1
        print(count)
        return ans
