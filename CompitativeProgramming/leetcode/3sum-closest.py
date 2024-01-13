class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        answer = None
        nums.sort()

        for i in range(len(nums)):
            j = i+1
            m = len(nums)-1
            while j < m:
                summ = nums[i]+nums[j] + nums[m]
                coll = summ-target
                colles = abs(coll)
                if colles <= ans:
                    ans = colles
                    answer = summ

                if coll > 0:
                    m -= 1
                elif coll < 0:
                    j += 1
                else: return answer
        return answer